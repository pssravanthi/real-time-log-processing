from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]

while True:
    log_data = {
        "timestamp": time.time(),
        "level": random.choice(log_levels),
        "message": "System event logged",
        "service": "API-Gateway"
    }
    producer.send('logs_topic', log_data)
    time.sleep(1)  # Simulating log generation
