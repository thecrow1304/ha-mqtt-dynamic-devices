from mapper import map_entity

class Registry:
    def __init__(self):
        self.devices = {}

    def process(self, sensor, message):
        device_id = sensor.get("deviceId")
        if not device_id:
            return

        if device_id not in self.devices:
            self.devices[device_id] = sensor
            self.publish_device(sensor)

        for key, value in message.items():
            entity = map_entity(device_id, key, value)
            if entity:
                self.publish_entity(entity)

    def publish_device(self, sensor):
        print("Neues Gerät:", sensor.get("alias"))

    def publish_entity(self, entity):
        print("Entity Update:", entity)

registry = Registry()

from config_store import config_store

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

        # hier später: nur gemappte Felder weiterreichen

registry = Registry()
