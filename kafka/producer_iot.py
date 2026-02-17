import json, time, random
from kafka import KafkaProducer
from datetime import datetime

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("🚀 Producer started. Sending events to Kafka...")

# Send a dummy record at startup (guarantees at least one message per run)
dummy_event = {
    "sensor_id": "DUMMY-INIT",
    "timestamp": datetime.utcnow().isoformat(),
    "temperature": 0.0,
    "co2": 0,
    "traffic": 0
}
producer.send("smartcity.iot", dummy_event)
producer.flush()
print(f"✅ Sent dummy: {dummy_event}")

# Continuous loop to generate and send IoT sensor data
while True:
    event = {
        "sensor_id": "CASA-CO2-01",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(15, 40), 2),
        "co2": random.randint(400, 1200),
        "traffic": random.randint(10, 100)
    }
    producer.send("smartcity.iot", event)
    print(f"✅ Sent: {event}")
    time.sleep(5)
