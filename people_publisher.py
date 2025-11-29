import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/12028876/people_counter"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="people_publisher")
client.connect(BROKER, PORT, keepalive=60)

current_count = 0

while True:
    delta = random.randint(-1, 5)
    current_count = max(0, current_count + delta)

    message = {
        "sensor": "people_counter",
        "value": current_count,
        "unit": "persons",
        "student_id": "12028876"
    }

    payload = json.dumps(message)
    client.publish(TOPIC, payload)

    print(f"[PEOPLE COUNTER] Sent → {TOPIC}: {payload}")

    time.sleep(4)
