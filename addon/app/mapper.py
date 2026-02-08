from translate_de import translate

def map_entity(device_id, raw_key, value):
    if "valueBoolean" in value:
        return {
            "type": "binary_sensor",
            "unique_id": f"{device_id}_{raw_key}",
            "name": translate(raw_key),
            "state": value["valueBoolean"]
        }

    if "valueNumber" in value:
        return {
            "type": "sensor",
            "unique_id": f"{device_id}_{raw_key}",
            "name": translate(raw_key),
            "state": value["valueNumber"]
        }

    return None
