# Global configuration
SLEEP_TIME = 300
ALERT_SLEEP_TIME = 60

# WiFi configuration
WIFI_SSID = 'pasdereseau'
WIFI_PASS = 'pasdecode'

# Bluetooth configuration
BLUETOOTH_PASS = 'HUAWEI P30 Pro'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'a15dezg3bt7a6e-ats.iot.eu-central-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/AmazonRootCA1.pem'
AWS_CLIENT_CERT = '/flash/cert/9de685a8c8c9a6f632ea0dba236c7e6db9740a954a7d79cd0acc476fd6e8c3d4-certificate.pem.crt'
AWS_PRIVATE_KEY = '/flash/cert/9de685a8c8c9a6f632ea0dba236c7e6db9740a954a7d79cd0acc476fd6e8c3d4-private.pem.key'

################## Subscribe / Publish client #################
CLIENT_ID = 'bike_tracker_1'
TOPIC = 'bike-tracking/bike_tracker_1/data'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'bike-tracking'
LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowUpdater"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowEcho"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5