from config_store import config_store
from mapper import map_entity
import json

class Registry:
    def __init__(self):
        self.devices = {}
        self.last_messages = {}

     def process(self, sensor, message):
        device_id = sensor.get("deviceId")
        if not device_id:
            return

        self.devices[device_id] = sensor
        self.last_messages[device_id] = message

        for key, value in message.items():
            if not config_store.is_enabled(device_id, key):
                continue

            mapping = config_store.get_mapping(device_id, key)
            entity = map_entity(device_id, key, value, mapping)

            if entity:
                self.publish_entity(entity)
                self.publish_state(entity)

registry = Registry()
