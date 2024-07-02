# scidx-tools

scidx-tools is a complementary Python library to scidx that provides additional functionalities for managing data and testing some functionalities in full. This library offers extended tools and utilities to enhance your experience in managing datasets and organizations.

## Features

- Send data to a Kafka topic
- Retrieve data from a Kafka topic

## Installation

To install the library, you can use pip:

```
pip install scidx_tools
```

For detailed installation instructions and dependencies, see [installation](docs/installation.md).

## Configuration

To configure the library, you need to set the API URL for your sciDX REST API instance. This can be done by initializing the sciDXToolsClient with the appropriate URL:

```python
from scidx_tools.client import sciDXToolsClient

api_url = "http://your-api-url.com"
KAFKA_HOST = 'placeholder'
KAFKA_PORT = 'placeholder'
OWNER_ORG = "placeholder"
client = sciDXToolsClient(api_url)
```

For detailed configuration instructions, see [Configuration](docs/configuration.md).

## Usage

Here is a quick example of how to use the library:

```python
import asyncio
import random
import time
from scidx.client import sciDXClient
from scidx_tools.client import sciDXToolsClient

# Constants
API_URL = "http://localhost:8000"
KAFKA_HOST = 'placeholder'
KAFKA_PORT = 'placeholder'
OWNER_ORG = "placeholder"

# Initialize sciDXClient and sciDXToolsClient
client = sciDXClient(API_URL)
tools_client = sciDXToolsClient(API_URL)

# Generate a unique Kafka topic name and a producer
kafka_topic = tools_client.generate_unique_kafka_topic()
producer = tools_client.producer(KAFKA_HOST, KAFKA_PORT, kafka_topic)

# Send random messages to Kafka topic
asyncio.run(await producer.send_random_messages(num_messages=15))

# Register Kafka topic as dataset
dataset_data = {
    "dataset_name": kafka_topic,
    "dataset_title": "Random Topic Example",
    "owner_org": OWNER_ORG,
    "kafka_topic": kafka_topic,
    "kafka_host": KAFKA_HOST,
    "kafka_port": KAFKA_PORT,
    "dataset_description": "This is a randomly generated Kafka topic registered as a CKAN dataset."
}
client.register_kafka(**dataset_data)

# Add a delay to ensure the dataset is indexed
time.sleep(2)

# Retrieve Kafka dataset information from API
kafka_datasets = client.search_kafka(kafka_topic=kafka_topic, kafka_host=KAFKA_HOST, kafka_port=KAFKA_PORT)

# Ensure that at least one dataset is returned
assert len(kafka_datasets) > 0, "No Kafka datasets found"

dataset_info = next((ds for ds in kafka_datasets if ds['resources'][0]['kafka_topic'] == kafka_topic), None)
assert dataset_info is not None, f"Kafka topic {kafka_topic} not found in datasets"

# Show Kafka connection details
print(dataset_info['resources'][0])

# Consume messages from Kafka topic using retrieved information
print(f"Starting to consume messages from topic: {kafka_topic}")

messages = await tools_client.consume_kafka_messages(topic=kafka_topic, host=KAFKA_HOST, port=KAFKA_PORT)
assert len(messages) > 0, f"No messages received from topic {kafka_topic}"
```

For more usage examples and detailed explanations, see [Usage](docs/usage.md).

## Testing

To run the tests for this project, you can use pytest:

```bash
pytest
```

For detailed testing instructions, see [Testing](docs/testing.md).

## Contributing

We welcome contributions to the scidx-tools project. To contribute, please follow the guidelines in  [Contributing](docs/contributing.md).

## License

This project is licensed under the MIT License. See [LICENSE.md](docs/LICENSE.md) for more details.

## Contact

For any questions or suggestions, please open an [issue](/docs/issues.md) on GitHub.
