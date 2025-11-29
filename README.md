# MQTT Lab – Ahmad Derieh – 12028876

## Broker
- Mosquitto running locally on `localhost:1883` (Windows).
- Clients connect from the same machine.

## Topics
All topics include my student ID `12028876`:

- `iot/12028876/temperature`
- `iot/12028876/humidity`
- `iot/12028876/people_counter`

## Publishers (Paho MQTT – Python)

1. `temp_publisher.py`
   - Publishes random temperature values in °C every 2 seconds.
   - Payload (JSON): `{ "sensor": "temperature", "value": X, "unit": "C", "student_id": "12028876" }`

2. `humidity_publisher.py`
   - Publishes random humidity percentages every 3 seconds.
   - Payload (JSON): `{ "sensor": "humidity", "value": X, "unit": "%", "student_id": "12028876" }`

3. `people_publisher.py`
   - Simulates a people counter, sending the current count every 4 seconds.
   - Payload (JSON): `{ "sensor": "people_counter", "value": N, "unit": "persons", "student_id": "12028876" }`

## Subscribers

1. `subscriber_all.py`
   - Subscribes to: `iot/12028876/#`
   - Receives all messages (temperature, humidity, people_counter).
   - Prints topic and JSON payload.

2. `subscriber_temp_only.py`
   - Subscribes only to: `iot/12028876/temperature`
   - Prints only temperature messages.

## How to Run

1. Install dependencies:
   ```bash
   pip install paho-mqtt

<img width="1641" height="678" alt="humidity_publisher py" src="https://github.com/user-attachments/assets/e49fe563-1155-4428-8c3a-9e9a2d0cfceb" />
<img width="1457" height="618" alt="temp_publisher py" src="https://github.com/user-attachments/assets/9e45642f-d462-43ed-848d-52a419b87766" />
<img width="1451" height="748" alt="subscriber_temp_only py" src="https://github.com/user-attachments/assets/8088da94-4a4e-4223-9114-7666d5bf9ccd" />
<img width="1542" height="970" alt="subscriber_all py" src="https://github.com/user-attachments/assets/f8207159-34eb-4841-9279-7748a326a5d9" />
<img width="1718" height="902" alt="people_publisher py" src="https://github.com/user-attachments/assets/f49d15f7-2884-4d2b-b9c3-ad7c75c87427" />
