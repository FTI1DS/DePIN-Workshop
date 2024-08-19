import brotli
import json

# Example data
data = "This is the sensor data we want to compress and decompress. " * 1000

# Sensor data
sensor_data = [
    {"timestamp": "2024-06-19T22:00:00Z", "heartbeat": 72, "sleep_status": "awake"},
    {"timestamp": "2024-06-19T22:15:00Z", "heartbeat": 70, "sleep_status": "asleep"},
    {"timestamp": "2024-06-19T22:30:00Z", "heartbeat": 68, "sleep_status": "asleep"},
    {"timestamp": "2024-06-19T22:45:00Z", "heartbeat": 67, "sleep_status": "asleep"},
    {"timestamp": "2024-06-20T07:00:00Z", "heartbeat": 75, "sleep_status": "awake"}
]

# Convert sensor data to JSON string
sensor_data_json = json.dumps(data)

# Compress data
compressed_data = brotli.compress(sensor_data_json.encode('utf-8'))
print(f"Compressed data: {compressed_data}")

# Decompress data
decompressed_data = brotli.decompress(compressed_data).decode('utf-8')
print(f"Decompressed data: {decompressed_data}")

# Size comparison
print(f"Original size: {len(sensor_data_json.encode('utf-8'))} bytes")
print(f"Compressed size: {len(compressed_data)} bytes")
