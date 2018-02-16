from paho.mqtt.client import Client
from sense_hat import SenseHat
import logging
import sys
import time
import configparser

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('mini-iot-sender-config.ini')
print(config.sections())
device_identifier = config['DEFAULT']['device_identifier']
mqtt_broker = config['DEFAULT']['mqtt_broker']

logging.info("Using device-id " + device_identifier)

topic_root = "mini-iot/" + device_identifier + "/"

client = Client("Mini-IOT client: " + device_identifier)
logging.info("Connecting to broker at " + mqtt_broker)
client.connect(mqtt_broker)
logging.info("Connected to broker")

# get the data from sense hat
hat = SenseHat()
hat.clear()

logging.info("Starting sensor value sending loop")
try:
  while True:
    temperature = hat.get_temperature()
    client.publish(topic_root + "temperature", temperature)

    humidity = hat.get_humidity()
    client.publish(topic_root + "humidity", humidity)

    pressure = hat.get_pressure()
    client.publish(topic_root + "pressure", pressure)

    orientation = hat.get_orientation_degrees()
    client.publish(topic_root + "/orientation/pitch", orientation['pitch'])
    client.publish(topic_root + "/orientation/roll", orientation['roll'])
    client.publish(topic_root + "/orientation/yaw", orientation['yaw'])

    time.sleep(.200)
except KeyboardInterrupt:
    pass
