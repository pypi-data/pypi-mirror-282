
from asthook.dynamic.module.register import ModuleDynamicCmd, BaseModuleDynamic
from asthook.utils import *
from asthook.log import debug

@ModuleDynamicCmd("sniff_ble", "Sniff ble communication", bool)
class AntiRoot(BaseModuleDynamic):
    def _init(self):
        self.sc.append("script_frida/blemon.js")
        self.frida.load(self.sc[-1], "custom", self.on_message_print)
    
    def on_message_print(self, message, data):
        if message['type'] == 'send':
            info(f"[sniff_ble] {message['payload']}")

    @classmethod
    def auto_complete(cls, args):
        return []


