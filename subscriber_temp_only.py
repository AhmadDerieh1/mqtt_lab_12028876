import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/12028876/temperature"

def on_connect(client, userdata, flags, rc):
    print("[SUB TEMP] Connected with code", rc)
    client.subscribe(TOPIC)
    print(f"[SUB TEMP] Subscribed → {TOPIC}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        print(f"[SUB TEMP] Message → {data}")
    except:
        print(f"[SUB TEMP] Raw → {payload}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="subscriber_temp_only")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
