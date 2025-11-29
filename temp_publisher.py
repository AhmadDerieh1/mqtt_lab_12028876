import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/12028876/temperature"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="temp_publisher")
client.connect(BROKER, PORT, keepalive=60)

while True:
    temperature = round(random.uniform(20.0, 30.0), 2)

    message = {
        "sensor": "temperature",
        "value": temperature,
        "unit": "C",
        "student_id": "12028876"
    }

    payload = json.dumps(message)
    client.publish(TOPIC, payload)

    print(f"[TEMP PUBLISHER] Sent → {TOPIC}: {payload}")

    time.sleep(2)
