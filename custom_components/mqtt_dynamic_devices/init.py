import json
import asyncio
from homeassistant.components import mqtt
from .const import DOMAIN

async def async_setup(hass, config):
    hass.data.setdefault(DOMAIN, {
        "devices": {},
        "entities": {}
    })

    async def handle_device(msg):
        payload = json.loads(msg.payload)
        hass.data[DOMAIN]["devices"][payload["device_id"]] = payload

    async def handle_entity(msg):
        payload = json.loads(msg.payload)
        await create_entity(hass, payload)

    async def handle_state(msg):
        payload = json.loads(msg.payload)
        entity_id = payload["entity_id"]
        state = payload["state"]
        hass.states.async_set(entity_id, state)

    await mqtt.async_subscribe(
        hass,
        "homeassistant/mqtt_dynamic_devices/device",
        handle_device
    )
    await mqtt.async_subscribe(
        hass,
        "homeassistant/mqtt_dynamic_devices/entity",
        handle_entity
    )
    await mqtt.async_subscribe(
        hass,
        "homeassistant/mqtt_dynamic_devices/state",
        handle_state
    )

    return True
