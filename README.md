# MQTT Lab – Ahmad Derieh – 12028876

This lab demonstrates how to use the Mosquitto MQTT broker with multiple publishers and subscribers using Python and the Paho-MQTT library. All published messages include my student ID **12028876** inside the MQTT topic and also inside the JSON payload, as required by the assignment. The Mosquitto MQTT broker was installed and run locally on Windows using the default listener on port **1883**, with all publishers and subscribers connecting from the same device.

The MQTT topics used in this lab all contain my student ID:
- `iot/12028876/temperature`
- `iot/12028876/humidity`
- `iot/12028876/people_counter`

Three Python publishers were implemented using the Paho-MQTT client:
1. **temp_publisher.py** — Sends random temperature readings every **2 seconds**.
2. **humidity_publisher.py** — Sends random humidity readings every **3 seconds**.
3. **people_publisher.py** — Simulates a people counter and publishes values every **4 seconds**.

Two subscribers were created:
1. **subscriber_all.py** — Subscribes to `iot/12028876/#` and receives **all** sensor messages (temperature, humidity, people counter).
2. **subscriber_temp_only.py** — Subscribes only to `iot/12028876/temperature` and receives **only temperature** readings.

## How to Run
1. Install the MQTT Python library:
   pip install paho-mqtt
2. Open **two CMD windows** for subscribers:
   python subscriber_all.py
   python subscriber_temp_only.py
3. Open **three CMD windows** for publishers: 
   python temp_publisher.py
   python humidity_publisher.py
   python people_publisher.py
   
Below are the screenshots showing actual outputs from the running system, verifying correct publishing and subscribing:

### 🔹 subscriber_all.py  
![subscriber_all.py](https://github.com/user-attachments/assets/d39aa7f2-4ee3-48be-a4bd-68d621808fb9)

### 🔹 subscriber_temp_only.py  
![subscriber_temp_only.py](https://github.com/user-attachments/assets/927a3e6d-e132-47e1-afab-53930973e4ed)

### 🔹 temp_publisher.py  
![temp_publisher.py](https://github.com/user-attachments/assets/a17e1be3-c545-4b45-b48d-25a700463c7c)

### 🔹 humidity_publisher.py  
![humidity_publisher.py](https://github.com/user-attachments/assets/e49fe563-1155-4428-8c3a-9e9a2d0cfceb)

### 🔹 people_publisher.py  
![people_publisher.py](https://github.com/user-attachments/assets/f49d15f7-2884-4d2b-b9c3-ad7c75c87427)

✔️ **Conclusion:**  
This lab successfully demonstrates the full MQTT workflow, including running a local Mosquitto broker, creating multiple publishers, building multiple subscribers, using custom MQTT topics that include the student ID **12028876**, sending and receiving JSON-formatted sensor data, and verifying correct real-time operation through screenshots. All assignment requirements have been fully completed.
