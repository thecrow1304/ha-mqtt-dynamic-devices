from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from registry import registry
from config_store import config_store
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return open("webui/index.html").read()

@app.get("/api/devices")
def devices():
    return registry.devices

@app.get("/api/fields/{device_id}")
def fields(device_id: str):
    return registry.last_messages.get(device_id, {})

@app.get("/api/config")
def get_config():
    return config_store.get()

@app.post("/api/mapping/{device_id}")
def set_mapping(device_id: str, mapping: dict):
    config_store.update_mapping(device_id, mapping)
    return {"status": "ok"}

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8099)
