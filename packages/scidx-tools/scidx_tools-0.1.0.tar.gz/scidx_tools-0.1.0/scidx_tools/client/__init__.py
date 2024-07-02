from .init_client import sciDXToolsClient
from .send_random_messages import send_random_messages
from .random_name import generate_unique_name
from .consume_kafka import _consume_kafka_messages, start_consuming, stop_consuming, get_messages

# Add the methods to sciDXToolsClient
sciDXToolsClient.send_random_kafka_messages = send_random_messages
sciDXToolsClient.random_name = generate_unique_name
sciDXToolsClient._consume_kafka_messages = _consume_kafka_messages
sciDXToolsClient.start_consuming = start_consuming
sciDXToolsClient.stop_consuming = stop_consuming
sciDXToolsClient.get_messages = get_messages
