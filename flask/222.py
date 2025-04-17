import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    print("✅ Connected!")
    connection.close()
except Exception as e:
    print("❌ Failed to connect:", e)