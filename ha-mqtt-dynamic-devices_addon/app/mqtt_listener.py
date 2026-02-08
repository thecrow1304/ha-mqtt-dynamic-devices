import json
import paho.mqtt.client as mqtt
from registry import registry

MQTT_HOST = "core-mosquitto"
MQTT_PORT = 1883
TOPIC = "physec/+/+/+/+/+/+"

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    sensor = payload.get("sensor", {})
    message = payload.get("message", {})

    registry.process(sensor, message)

def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT)
    client.subscribe(TOPIC)
    client.loop_forever()
