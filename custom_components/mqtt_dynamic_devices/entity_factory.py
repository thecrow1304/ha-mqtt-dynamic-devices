from .sensor import DynamicSensor
from .binary_sensor import DynamicBinarySensor

async def create_entity(hass, definition):
    platform = definition["platform"]

    if platform == "sensor":
        entity = DynamicSensor(definition)
        hass.add_job(
            hass.helpers.entity_platform.async_add_entities,
            [entity]
        )

    if platform == "binary_sensor":
        entity = DynamicBinarySensor(definition)
        hass.add_job(
            hass.helpers.entity_platform.async_add_entities,
            [entity]
        )
