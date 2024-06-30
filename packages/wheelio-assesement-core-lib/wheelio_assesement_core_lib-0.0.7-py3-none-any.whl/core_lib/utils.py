import os
import pika
from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient
from tenacity import retry, stop_after_attempt, wait_exponential


def get_current_username(request: Request):
    return request.session.get("user")


async def get_mongo_db(DATABASE_URL: str):
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client.get_default_database()
    try:
        yield db
    finally:
        client.close()


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")


class BaseRabbit:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(RABBITMQ_HOST)
        )
        self.channel = self.connection.channel()

    def close_connection(self):
        self.connection.close()

    @retry(
        stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def publish_message(self, queue, message):
        self.channel.basic_publish(exchange="", routing_key=queue, body=message)

    def start_consuming(self, queue, callback):
        self.channel.queue_declare(queue=queue)
        self.channel.basic_consume(queue=queue, on_message_callback=callback)
        self.channel.start_consuming()
