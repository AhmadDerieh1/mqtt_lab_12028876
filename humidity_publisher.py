import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/12028876/humidity"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="humidity_publisher")
client.connect(BROKER, PORT, keepalive=60)

while True:
    humidity = round(random.uniform(40.0, 70.0), 2)

    message = {
        "sensor": "humidity",
        "value": humidity,
        "unit": "%",
        "student_id": "12028876"
    }

    payload = json.dumps(message)
    client.publish(TOPIC, payload)

    print(f"[HUMIDITY PUBLISHER] Sent → {TOPIC}: {payload}")

    time.sleep(3)
