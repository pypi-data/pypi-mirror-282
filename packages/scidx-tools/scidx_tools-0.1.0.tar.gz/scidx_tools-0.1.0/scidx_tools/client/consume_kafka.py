import threading
from typing import List
from aiokafka import AIOKafkaConsumer
import asyncio
import nest_asyncio
import json
import pandas as pd

nest_asyncio.apply()


async def _consume_kafka_messages(self, host: str, port: str, topic: str):
    """
    Consume messages from a Kafka topic continuously until stopped.

    Parameters
    ----------
    topic : str
        The Kafka topic name.
    host : str
        The Kafka host.
    port : str
        The Kafka port.

    Returns
    -------
    None
    """
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=f"{host}:{port}",
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        fetch_max_bytes=104857600,  # 100MB fetch size
        max_poll_records=1000  # Fetch up to 1000 messages per poll
    )
    await consumer.start()
    try:
        while not self._stop_event.is_set():
            msg_batch = await consumer.getmany(timeout_ms=1000)
            for tp, messages_in_tp in msg_batch.items():
                for msg in messages_in_tp:
                    self._messages.append(msg.value.decode('utf-8'))
                    await asyncio.sleep(0)  # Allow other tasks to run
    except asyncio.CancelledError:
        print("Consumption cancelled. Cleaning up...")
    finally:
        await consumer.stop()

def start_consuming(self, host: str, port: str, topic: str):
    """
    Start the message consuming coroutine in a new event loop.

    Parameters
    ----------
    host : str
        The Kafka host.
    port : str
        The Kafka port.
    topic : str
        The Kafka topic name.
    """
    self._stop_event.clear()
    self._loop = asyncio.new_event_loop()
    asyncio.set_event_loop(self._loop)
    self._consumer_task = self._loop.create_task(self._consume_kafka_messages(host, port, topic))
    self._thread = threading.Thread(target=self._loop.run_forever)
    self._thread.start()

def stop_consuming(self):
    """
    Signal the consumer to stop, wait for the task to finish, and clear the messages.
    """
    self._stop_event.set()
    if self._consumer_task:
        self._consumer_task.cancel()
        self._loop.call_soon_threadsafe(self._loop.stop)
        self._thread.join()
        self._loop.close()
    self._messages.clear()  # Clear the messages

def get_messages(self) -> pd.DataFrame:
    """
    Get the list of consumed messages as a DataFrame.

    Returns
    -------
    pd.DataFrame
        The DataFrame containing the consumed messages.
    """
    return pd.DataFrame([json.loads(msg) for msg in self._messages])