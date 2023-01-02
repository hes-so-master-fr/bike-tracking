from network import WLAN
import machine
from network import Bluetooth


class WifiManager:
    def __init__(self):
        self.wlan = WLAN(mode=WLAN.STA)
        
    def connect(self, ssid, password):
        self.wlan.connect(ssid=ssid, auth=(WLAN.WPA2, password))
        while not self.wlan.isconnected():
            machine.idle()
        
    def isconnected(self):
        return self.wlan.isconnected()
        
    def status(self):
        return self.wlan.ifconfig()
    
class BluetoothManager:
    def __init__(self):
        self.bluetooth = Bluetooth()
    
    def isconnected(self, ssid):
        self.bluetooth.start_scan(30)
        while self.bluetooth.isscanning():
            adv = self.bluetooth.get_adv()
            if adv and self.bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == ssid:
                self.bluetooth.stop_scan()
                return True
        return False