
from asthook.dynamic.module.register import ModuleDynamicCmd, BaseModuleDynamic
from asthook.utils import Output
from asthook.log import error
import os
import json


@ModuleDynamicCmd("aws", "hook or export aws secret key", bool)
class AWSHook(BaseModuleDynamic):
    """
    Class to load AWSHook

    To use:
      --aws
    """
    def _init(self):
        self.access = None
        self.secret = None
        self.session = None
        current_dir = os.path.dirname(__file__)
        hook = f"{current_dir}/hook_aws.js"
        self.sc.append(hook)
        ret, e = self.frida.load(hook, "custom", self.on_message_print, absolute=True)
        if ret == 1:
            error(f"[quickhook] file {hook} doesn't exist")
        elif ret == 2:
            error(f"[quickhook] is not a file")
        elif ret == 3:
            error(f"[quickhook] {e}")
        elif ret == 4:
            error(f"[quickhook] file not valid")


    def on_message_print(self, message, data):
        if message['type'] == 'send':
            payload = json.loads(message['payload'])
            if self.access != payload['access']:
                self.access = payload['access']
                self.secret = payload['secret']
                self.session = payload['session']
                print("AWS credential hooked:")
                print(f"access : {payload['access']}\n" \
                      f"secret : {payload['secret']}"   \
                      f"\nsession : {payload['session']}" if 'session' in payload.keys() else "")
        elif message['type'] == 'error':
            error(message['description'])
            error(message['stack'])
            self.is_alive = False
