from homeassistant.helpers import device_registry as dr

device_registry = dr.async_get(hass)

device_registry.async_get_or_create(
    config_entry_id=None,
    identifiers={(DOMAIN, payload["device_id"])},
    name=payload["name"],
    manufacturer=payload.get("manufacturer"),
    model=payload.get("model"),
)
