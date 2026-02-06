import json, time, random
from kafka import KafkaProducer
from datetime import datetime

# Initialize Kafka producer with connection settings
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Continuous loop to generate and send IoT sensor data
while True:
    # Create simulated sensor event with random values
    event = {
        "sensor_id": "CASA-CO2-01",
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(15, 40), 2),
        "co2": random.randint(400, 1200),
        "traffic": random.randint(10, 100)
    }

    # Send the event to the Kafka topic
    producer.send("smartcity.iot", event)

    # Wait 5 seconds before sending the next event
    time.sleep(5)
