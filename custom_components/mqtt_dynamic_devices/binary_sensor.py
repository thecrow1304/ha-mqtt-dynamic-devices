from homeassistant.components.binary_sensor import BinarySensorEntity

class DynamicBinarySensor(BinarySensorEntity):
    def __init__(self, definition):
        self._attr_name = definition["name"]
        self._attr_unique_id = definition["entity_id"]
        self._state = False

    @property
    def is_on(self):
        return self._state

    def set_state(self, value):
        self._state = bool(value)
        self.async_write_ha_state()
