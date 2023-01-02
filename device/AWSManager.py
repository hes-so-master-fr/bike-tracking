import machine
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class MQTTClient:
    def __init__(self, config):
        self.client = AWSIoTMQTTClient(config.CLIENT_ID)
        
        self.client.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
        self.client.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_CLIENT_CERT)

        self.client.configureOfflinePublishQueueing(config.OFFLINE_QUEUE_SIZE)
        self.client.configureDrainingFrequency(config.DRAINING_FREQ)
        self.client.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
        self.client.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)
        self.client.configureLastWill(config.LAST_WILL_TOPIC, config.LAST_WILL_MSG, 1)
    def connect(self):
        while not self.client.connect():
            print('AWS connection failed')
            time.sleep(1)
        print('AWS connection succeeded')
            
    def printCallback(client, userdata, message):
        print("Received a new message: ")
        print(message.payload)
        print("from topic: ")
        print(message.topic)
        print("--------------\n\n")
    
    def send(self,topic,type,latitude,longitude,altitude):
        data = '{{"msg_type": "{0}", "position": {{ "latitude": {1}, "longitude": {2}, "altitude": {3} }} }}'.format(type,latitude,longitude,altitude)
        print("Send {0} on {1}".format(data, topic))
        self.client.publish(topic, data, 1)