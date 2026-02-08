from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import async_add_entities

class DynamicSensor(SensorEntity):
    def __init__(self, definition):
        self._attr_name = definition["name"]
        self._attr_unique_id = definition["entity_id"]
        self._attr_native_unit_of_measurement = definition.get("unit")
        self._state = None

    @property
    def native_value(self):
        return self._state

    def set_state(self, value):
        self._state = value
        self.async_write_ha_state()
