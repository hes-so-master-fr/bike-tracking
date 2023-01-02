import time
import socket
import pycom
from NetworkManager import WifiManager
from NetworkManager import BluetoothManager
from AWSManager import MQTTClient
from GPSManager import GPSManager
import config

wifi = WifiManager()
wifi.connect(config.WIFI_SSID, config.WIFI_PASS)
print("WiFi connected succesfully")
print(wifi.status())

bt = BluetoothManager()

gps = GPSManager()

AWSClient = MQTTClient(config)
AWSClient.connect()

lastpos = (None, None)
watching = False
alert = False
    
while(True):
    
    if not watching and not alert:
        notconn = not bt.isconnected(config.BLUETOOTH_PASS)
        print("PHONE NOT CONNECTED" if notconn else "Phone connected")
        if notconn:
            watching = True
            lastpos = gps.getposition()
            if lastpos[0] == None or lastpos[1] == None:
                print("No gps position found")
                watching = False
            else:
                AWSClient.send("test", "info", lastpos[0], lastpos[1], 0)
                
        time.sleep(config.SLEEP_TIME)
  
    elif watching and not alert:
        notconn = not bt.isconnected(config.BLUETOOTH_PASS)
        print("PHONE NOT CONNECTED" if notconn else "Phone connected")
        if not notconn:
            watching = False
            time.sleep(config.SLEEP_TIME)
        else:
            currpos = gps.getposition()
            if currpos[0] != None and currpos[1] != None:
                if round(currpos[0],5) != round(lastpos[0],5) or round(currpos[1],5) != round(lastpos[1],5):
                    alert = True
                    lastpos = currpos
                    print("ALERT BIKE IS MOVING")
                    AWSClient.send("test", "alert", lastpos[0], lastpos[1], 0)
                    time.sleep(config.ALERT_SLEEP_TIME)
                    continue
            else:
                print("No gps position found")
        time.sleep(config.SLEEP_TIME)
        
    elif alert:
        print("ALERT BIKE IS MOVING")
        currpos = gps.getposition()
        if currpos[0] != None and currpos[1] != None:
            lastpos = currpos
        else:
            print("No gps position found, send last")
        AWSClient.send("test", "alert", lastpos[0], lastpos[1], 0)
        time.sleep(config.ALERT_SLEEP_TIME)
        