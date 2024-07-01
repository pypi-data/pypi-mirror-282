"""
IA Parc Inference service
Support for inference of IA Parc models
"""
from json import dumps
from math import e
import os
import asyncio
from re import T
import uuid
from inspect import signature
import logging
import logging.config
import nats
from nats.errors import TimeoutError as NATSTimeoutError
from iaparc_inference.config import Config
from iaparc_inference.data_decoder import decode
from iaparc_inference.data_encoder import DataEncoder

Error = ValueError | None

LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LEVEL,
    force=True,
    format="%(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger("Inference")
LOGGER.propagate = True


class IAPListener():
    """
    Inference Listener class
    """

    def __init__(self,
                 callback,
                 decode=True,
                 batch:int=-1,
                 inputs:str = "",
                 outputs:str = "",
                 config_path:str= "/opt/pipeline/pipeline.json",
                 url:str="",
                 queue:str=""
                 ):
        """
        Constructor
        Arguments:
        - callback:     Callback function to proccess data
                        callback(data: Any | list[Any], parameters: Optional[dict])
        Optional arguments:
        - inputs:       Input queue name
        - outputs:      Output queue name
        - decode:       Set wether data should be decoded before calling the callback function (default: True)
        - batch:        Batch size for inference (default: -1)
                        If your model do not support batched input, set batch to 1
                        If set to -1, batch size will be determined by the BATCH_SIZE 
                        environment variable
        - config_path:  Path to config file (default: /opt/pipeline/pipeline.json)
        - url:          Url of inference server (default: None)
                        By default determined by the NATS_URL environment variable,
                        however you can orverride it here
        - queue:        Name of queue (default: None)
                        By default determined by the NATS_QUEUE environment variable,
                        however you can orverride it here
        """
        # Init internal variables
        self.decode = decode
        self._subs_in = []
        self._subs_out = []
        self._dag = Config(config_path)
        if inputs:
            self._dag.inputs = inputs
        self._inputs_name = self._dag.inputs.split(",")
        self._outputs_name = self._dag.outputs.split(",")
        
        self.lock = asyncio.Lock()
        self.callback = callback
        sig = signature(callback)
        self.callback_args = sig.parameters
        nb_params = len(self.callback_args)
        if nb_params == 1:
            self.callback_has_parameters = False
        else:
            self.callback_has_parameters = True
        
        if url:
            self.url = url
        else:
            self.url = os.environ.get("NATS_URL", "nats://localhost:4222")
        if queue:
            self.queue = queue.replace("/", "-")
        else:
            self.queue = os.environ.get(
                "NATS_QUEUE", "inference").replace("/", "-")
        if batch > 0:
            self.batch = batch
        else:
            self.batch = int(os.environ.get("BATCH_SIZE", 1))
        if self.batch > 1:
            self.is_batch = True
        else:
            self.is_batch = False
        
        self.error_queue = self.queue + ".ERROR"
        self.inputs = {}
        self.outputs = {}
        self.encoders = {}        
        for entity in self._dag.pipeline:
            for item in entity.input_def:
                if "name" in item and item["name"] in self._inputs_name:
                    self.inputs[item["name"]] = item
            for item in entity.output_def:
                if "name" in item and item["name"] in self._outputs_name:
                    self.outputs[item["name"]] = item
                    self.encoders[item["name"]] = DataEncoder(item)
        if outputs and outputs in self._outputs_name:
            self.default_output = self.outputs[outputs]["link"]
        else:
            self.default_output = self.outputs[self._outputs_name[0]]["link"]

    @property
    def dag(self) -> Config:
        """ Input property """
        return self._dag

    @property
    def inputs_name(self) -> list:
        """ Input property """
        return self._inputs_name

    @property
    def outputs_name(self) -> list:
        return self._outputs_name

    def run(self):
        """
        Run inference service
        """
        asyncio.run(self._run_async())

    async def _run_async(self):
        """ Start listening to NATS messages
        url: NATS server url
        batch_size: batch size
        """
        self.nc = await nats.connect(self.url)
        self.js = self.nc.jetstream()
        
        for q_name in self.inputs_name:
            item = self.inputs[q_name]  
            queue_in = self.queue + "." + item["link"]
            print("Listening on queue:", queue_in)
            js_in = await self.js.subscribe("js."+queue_in+".>",
                                             queue=self.queue+"-"+item["link"],
                                             stream=self.queue)
            self._subs_in.append((item["link"], js_in))
            nc_in = await self.nc.subscribe("nc."+queue_in+".*.*")
            self._subs_in.append((item["link"], nc_in))
        
        print("Default queue out:", self.default_output)
        self.data_store = await self.js.object_store(bucket=self.queue+"-data")
       
        os.system("touch /tmp/running")
        tasks = []
        for name, sub_in in self._subs_in:
            tasks.append(self.wait_msg(name, sub_in))
        await asyncio.gather(*tasks)
        await self.nc.close()

    async def wait_msg(self, name, sub_in):
        # Fetch and ack messagess from consumer.
        if sub_in.subject[:7] == "_INBOX.":
            subject = sub_in.subject[7:]
            is_js = True
        else:
            subject = sub_in.subject
            is_js = False
        while True:
            try:
                pending_msgs = sub_in.pending_msgs
                if not self.is_batch or pending_msgs == 0:
                    msg = await sub_in.next_msg(timeout=600)
                    await asyncio.gather(
                        self.handle_msg(subject, name, [msg]),
                        self.term_msg([msg], is_js)
                    )
                else:
                    if pending_msgs >= self.batch:
                        _batch = self.batch
                    else:
                        _batch = pending_msgs
                    msgs = []
                    done = False
                    i = 0
                    while not done:
                        try:
                            msg = await sub_in.next_msg(timeout=0.01)
                            msgs.append(msg)
                        except TimeoutError:
                            done = True
                        i += 1
                        if i == _batch:
                            done = True
                        p = sub_in.pending_msgs
                        if p == 0:
                            done = True
                        elif p < _batch - i:
                            _batch = p + i

                    await asyncio.gather(
                        self.handle_msg(subject, name, msgs),
                        self.term_msg(msgs, is_js)
                    )
            except NATSTimeoutError:
                continue
            except TimeoutError:
                continue
            except Exception as e:  # pylint: disable=W0703
                LOGGER.error("Fatal error message handler: %s",
                             str(e), exc_info=True)
                break

    async def handle_msg(self, subject, name, msgs):
        async with self.lock:
            if self.is_batch:
                uids, sources, batch, params_lst, content_types = zip(*[await self.get_data(subject, msg) for msg in msgs])
                batch = list(batch)
                await self._process_data(name, uids, sources, batch, content_types, params_lst)
            else:
                for msg in msgs:
                    uid, source, data, params, content_type = await self.get_data(subject, msg)
                    await self._process_data(name, [uid], [source], [data], [content_type], [params])

        return

    async def term_msg(self, msgs, is_js=False):
        if is_js:
            for msg in msgs:
                await msg.ack()

    async def get_data(self, subject, msg):
        l_sub = len(subject) + 1
        uid = msg.subject[(l_sub):]
        source = msg.headers.get("DataSource", "")
        params_lst = msg.headers.get("Parameters", "")
        params = {}
        if params_lst:
            for p in params_lst.split(","):
                args = p.split("=")
                if len(args) == 2:
                    k, v = args
                    params[k] = v
        content_type = msg.headers.get("ContentType", "")
        data = None
        if source == "object_store":
            obj_res = await self.data_store.get(msg.data.decode())
            data = obj_res.data
        else:
            data = msg.data

        return (uid, source, data, params, content_type)

    async def send_msg(self, out, uid, source, data, parameters={}, error=""):
        if error is None:
            error = ""
        _params = dumps(parameters)
        breply = "".encode()
        contentType = ""
        if out != self.error_queue:
            _out = self.queue + "." + out + "." + uid
            #print("Sending reply to:", _out)
            if data is not None:
                if source == "object_store":
                    store_uid = str(uuid.uuid4())
                    breply = store_uid.encode()
                    err = None
                    if isinstance(data, (bytes, bytearray)):
                        bdata = data
                    else:
                        bdata, contentType, err = self.encoders[out].encode(data)
                        if err:
                            _out = self.error_queue + "." + uid
                            breply = str(err).encode()
                            error = "Error encoding data"
                    if not err:
                        await self.data_store.put(store_uid, bdata)
                else :
                    if isinstance(data, (bytes, bytearray)):
                        breply = data
                    else:
                        breply, contentType, err = self.encoders[out].encode(data)
                        if err:
                            _out = self.error_queue + "." + uid
                            breply = str(err).encode()
                            error = "Error encoding data"
                    if len(breply) > 8388608: # 8MB
                        store_uid = str(uuid.uuid4())
                        source = "object_store"
                        bdata = breply
                        breply = store_uid.encode()
                        await self.data_store.put(store_uid, bdata)
        else:
            _out = self.error_queue + "." + uid
            breply = data.encode()
        
        headers = {"ProcessError": error,
                   "ContentType": contentType,
                   "DataSource": source,
                   "Parameters": _params}
        
        _sent = False
        if out != self.error_queue:
            try:
                await self.nc.publish(_out, breply, headers=headers)
                _sent = True
            except Exception as e: # pylint: disable=W0703
                LOGGER.error("Error sending message: %s", str(e), exc_info=True)
        if not _sent:
            await self.js.publish(_out, breply, headers=headers)

    async def _process_data(self, name: str,
                      uids: list,
                      sources: list,
                      raw_datas: list,
                      content_types: list,
                      reqs_parameters: list):
        """
        Process data
        Arguments:
        - requests:   list of data to process
        - is_batch:   is batched data
        """
        LOGGER.debug("handle request")
        queue_out = self.default_output
        p_datas = []
        p_sources = []
        p_uids = []
        p_params = []
        tasks = []
        for uid, src, raw, ctype, params in zip(uids, sources, raw_datas, content_types, reqs_parameters):
            if self.decode:
                data, error = decode(raw, ctype, self.inputs[name])
                if error:
                    task = asyncio.create_task(self.send_msg(self.error_queue, 
                                                               uid, 
                                                               src,
                                                               str(error), 
                                                               params, 
                                                               "Wrong input"))
                    tasks.append(task)
                    continue
                p_datas.append(data)
            else:
                p_datas.append(raw)
            p_sources.append(src)
            p_uids.append(uid)
            p_params.append(params)
        if len(tasks) > 0:
            await asyncio.gather(*tasks)
        
        tasks = []
        try_error = ""      
        if len(p_datas) > 0:
            try_err = ""
            try:
                error = ""
                if self.is_batch:
                    if self.callback_has_parameters:
                        res = self.callback(p_datas, p_params)
                    else:
                        res = self.callback(p_datas)           
                    if isinstance(res, tuple):
                        if len(res) == 2:
                            result, error = res
                        if len(res) == 3:
                            result, out, error = res
                            if out in self.outputs_name:
                                queue_out = self.outputs_name[out]['link']
                    else:
                        result = res
                    if not isinstance(result, list):    
                        error = "batch reply is not a list"
                    if len(p_datas) != len(result):
                        error = "batch reply has wrong size"
                    if error:
                        for uid, source, params in zip(p_uids, p_sources, p_params):
                            task = asyncio.create_task(self.send_msg(queue_out, 
                                                                       uid, 
                                                                       source, 
                                                                       error, 
                                                                       params, 
                                                                       error))
                            tasks.append(task)
                    else:
                        for uid, source, res, params in zip(p_uids, p_sources, result, p_params):
                            task = asyncio.create_task(self.send_msg(queue_out, 
                                                                       uid, 
                                                                       source, 
                                                                       res,
                                                                       params))
                            tasks.append(task)
                        
                else:
                    if len(p_params) > 0:
                        _params = p_params[0]
                    else:
                        _params = {}
                    if self.callback_has_parameters:
                        res = self.callback(p_datas[0], _params)
                    else:
                        res = self.callback(p_datas[0])
                    if isinstance(res, tuple):
                        if len(res) == 2:
                            result, error = res
                        if len(res) == 3:
                            result, out, error = res
                            if out in self.outputs_name:
                                queue_out = out
                    else:
                        result = res
                    task = asyncio.create_task(self.send_msg(queue_out, 
                                                               p_uids[0], 
                                                               p_sources[0], 
                                                               result, 
                                                               _params,
                                                               error=error))
                    tasks.append(task)
                
            except ValueError:
                LOGGER.error("Fatal error message handler", exc_info=True)
                try_error  = "Wrong input"
            except Exception as e: # pylint: disable=W0703
                LOGGER.error("Fatal error message handler", exc_info=True)
                try_error = f'Fatal error: {str(e)}'
            if try_error:
                for uid, source in zip(p_uids, p_sources):
                    task = asyncio.create_task(self.send_msg(
                            self.error_queue, uid, src, try_error, "Wrong input"))
                    tasks.append(task)
        
        if len(tasks) > 0:
            await asyncio.gather(*tasks)