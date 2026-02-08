from translate_de import translate

def map_entity(device_id, raw_key, value, mapping):
    entity_id = mapping["entity_id"]
    platform = mapping["platform"]

    entity = {
        "device_id": device_id,
        "entity_id": entity_id,
        "platform": platform,
        "name": mapping["name"],
        "unit": mapping.get("unit"),
        "device_class": mapping.get("device_class"),
        "state_class": mapping.get("state_class"),
    }

    if "valueBoolean" in value:
        entity["state"] = value["valueBoolean"]

    if "valueNumber" in value:
        entity["state"] = value["valueNumber"]

    if "valueString" in value:
        entity["state"] = value["valueString"]

    return entity
