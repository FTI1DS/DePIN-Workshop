import brotli
import json
import random
from datetime import datetime, timedelta

# Function to generate random sensor data
def generate_random_sensor_data(base_data, count):
    random_data = []
    for i in range(count):
        for entry in base_data:
            # Modify timestamp by adding a random number of seconds
            timestamp = datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            random_seconds = random.randint(-300, 300)  # Random offset up to 5 minutes
            new_timestamp = timestamp + timedelta(seconds=random_seconds)

            # Randomly vary the heartbeat slightly
            heartbeat_variation = random.randint(-3, 3)
            new_heartbeat = entry["heartbeat"] + heartbeat_variation

            # Create a new entry with modified values
            new_entry = {
                "timestamp": new_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "heartbeat": new_heartbeat,
                "sleep_status": entry["sleep_status"],
            }
            random_data.append(new_entry)
    return random_data

# Base sensor data
base_sensor_data = [
    {"timestamp": "2024-06-19T22:00:00Z", "heartbeat": 72, "sleep_status": "awake"},
    {"timestamp": "2024-06-19T22:15:00Z", "heartbeat": 70, "sleep_status": "asleep"},
    {"timestamp": "2024-06-19T22:30:00Z", "heartbeat": 68, "sleep_status": "asleep"},
    {"timestamp": "2024-06-19T22:45:00Z", "heartbeat": 67, "sleep_status": "asleep"},
    {"timestamp": "2024-06-20T07:00:00Z", "heartbeat": 75, "sleep_status": "awake"}
]

# Generate varied sensor data
sensor_data = generate_random_sensor_data(base_sensor_data, 1000)

# Convert sensor data to JSON string
sensor_data_json = json.dumps(sensor_data)

# Compress data
compressed_data = brotli.compress(sensor_data_json.encode('utf-8'))
print(f"Compressed data: {compressed_data}")

# Decompress data
decompressed_data = brotli.decompress(compressed_data).decode('utf-8')
print(f"Decompressed data: {decompressed_data}")

# Size comparison
print(f"Original size: {len(sensor_data_json.encode('utf-8'))} bytes")
print(f"Compressed size: {len(compressed_data)} bytes")
