import json
import paho.mqtt.client as mqtt

HA_TOPIC = "homeassistant/mqtt_dynamic_devices"

class Registry:
    def __init__(self):
        self.devices = {}
        self.mqtt = mqtt.Client()
        self.mqtt.connect("core-mosquitto", 1883)

    def process(self, sensor, message):
        device_id = sensor.get("deviceId")
        if not device_id:
            return

        if device_id not in self.devices:
            self.devices[device_id] = True
            self.publish_device(sensor)

        for key, value in message.items():
            self.publish_entity_and_state(device_id, key, value)

    def publish_device(self, sensor):
        payload = {
            "device_id": sensor["deviceId"],
            "name": sensor.get("alias"),
            "manufacturer": sensor.get("type"),
            "model": sensor.get("type"),
            "identifiers": [sensor["deviceId"]],
        }
        self.mqtt.publish(f"{HA_TOPIC}/device", json.dumps(payload), retain=True)

    def publish_entity_and_state(self, device_id, key, value):
        from mapper import map_entity

        entity = map_entity(device_id, key, value)
        if not entity:
            return

        self.mqtt.publish(
            f"{HA_TOPIC}/entity",
            json.dumps(entity),
            retain=True
        )

        self.mqtt.publish(
            f"{HA_TOPIC}/state",
            json.dumps({
                "entity_id": entity["entity_id"],
                "state": entity["state"]
            })
        )

registry = Registry()
