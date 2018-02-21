import paho.mqtt.client as mqtt
import os

MQTT_HOST = os.environ["MQTT"]


def on_connect(client, userdata, flags, rc):
    print("Connected with result code %s" % rc)

    client.subscribe("mini-iot/+/temperature")


def on_message(client, userdata, msg):
    print("%-40s %f" % (msg.topic, float(msg.payload)))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, 1883, 60)

client.loop_forever()
