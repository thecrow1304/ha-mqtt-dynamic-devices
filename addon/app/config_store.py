import json
from pathlib import Path

CONFIG_FILE = Path("/data/config.json")

class ConfigStore:
    def __init__(self):
        self.data = {
            "devices": {},
            "mappings": {}
        }
        self.load()

    def load(self):
        if CONFIG_FILE.exists():
            self.data = json.loads(CONFIG_FILE.read_text())

    def save(self):
        CONFIG_FILE.write_text(json.dumps(self.data, indent=2))

    def get(self):
        return self.data

    def update_mapping(self, device_id, mapping):
        self.data["mappings"][device_id] = mapping
        self.save()

config_store = ConfigStore()
