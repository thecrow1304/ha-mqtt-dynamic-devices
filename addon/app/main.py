from mqtt_listener import start_mqtt
from api import start_api
import threading

if __name__ == "__main__":
    threading.Thread(target=start_api, daemon=True).start()
    start_mqtt()
