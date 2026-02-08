from homeassistant.components.sensor import SensorEntity

class DynamicSensor(SensorEntity):
    def __init__(self, definition):
        self._attr_name = definition["name"]
        self._attr_unique_id = definition["unique_id"]
        self._state = definition["state"]

    @property
    def native_value(self):
        return self._state
