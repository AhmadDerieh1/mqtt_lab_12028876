# MQTT Lab – Ahmad Derieh – 12028876

## 📌 Overview
This lab demonstrates how to use the Mosquitto MQTT broker with multiple publishers and subscribers using Python and the Paho-MQTT library.  
Each published message includes my student ID **12028876** inside the MQTT topic and inside the JSON payload as required in the assignment.

---

# 🖥️ MQTT Broker
- Broker used: **Mosquitto**
- Running locally on Windows  
- Host: `localhost`
- Port: `1883`
- All MQTT clients connect locally from the same device

---

# 🧵 MQTT Topics Used
All topics include my Student ID: **12028876**

- `iot/12028876/temperature`
- `iot/12028876/humidity`
- `iot/12028876/people_counter`

---

# 📤 Publishers (Python – Paho MQTT)

## 1️⃣ Temperature Publisher — `temp_publisher.py`
Sends random temperature every **2 seconds**.

## 2️⃣ Humidity Publisher — `humidity_publisher.py`
Sends random humidity values every **3 seconds**.

## 3️⃣ People Counter Publisher — `people_publisher.py`
Simulates people entering/exiting every **4 seconds**.

---

# 📥 Subscribers

## 1️⃣ `subscriber_all.py`
Subscribes to:
