from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1>MQTT Dynamic Devices</h1><p>Läuft ✅</p>"

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8099)
