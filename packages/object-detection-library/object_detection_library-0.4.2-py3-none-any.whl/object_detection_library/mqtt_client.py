import paho.mqtt.client as mqtt
import json

# Ubidots configuration
BROKER = 'industrial.api.ubidots.com'
PORT = 1883
TOPIC = '/v1.6/devices/nive_device'  # Replace with your actual device label
TOKEN = 'BBUS-p5jk4sjuBy5N0PiZeuOdRBVGBjc7y2'  # Replace with your Ubidots token

def publish_data(data):
    client = mqtt.Client()
    client.username_pw_set(TOKEN)

    print(f"Connecting to broker at {BROKER}:{PORT}")
    
    client.connect(BROKER, PORT, 60)
    
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    client.disconnect()
