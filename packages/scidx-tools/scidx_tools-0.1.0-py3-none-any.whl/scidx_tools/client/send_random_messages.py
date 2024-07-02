import random
import string
from aiokafka import AIOKafkaProducer


async def send_random_messages(self, host, port, topic, num_messages):
    producer = AIOKafkaProducer(bootstrap_servers=f"{host}:{port}")
    await producer.start()
    try:
        for _ in range(num_messages):
            message = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            await producer.send_and_wait(topic, message.encode('utf-8'))
    finally:
        print(f"{num_messages} messages sent.")
        await producer.stop()
