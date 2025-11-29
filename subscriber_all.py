import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/12028876/#"   

def on_connect(client, userdata, flags, rc):
    print("[SUB ALL] Connected with code", rc)
    client.subscribe(TOPIC)
    print(f"[SUB ALL] Subscribed → {TOPIC}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        print(f"[SUB ALL] {msg.topic} → {data}")
    except:
        print(f"[SUB ALL] Raw message → {payload}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id="subscriber_all")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
