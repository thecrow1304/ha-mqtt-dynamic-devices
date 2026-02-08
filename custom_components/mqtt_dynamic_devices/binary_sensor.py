from homeassistant.components.binary_sensor import BinarySensorEntity

class DynamicBinarySensor(BinarySensorEntity):
    def __init__(self, definition):
        self._attr_name = definition["name"]
        self._attr_unique_id = definition["unique_id"]
        self._state = definition["state"]

    @property
    def is_on(self):
        return self._state
