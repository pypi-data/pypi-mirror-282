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


class BaseRabbit:
    def __init__(self, RABBITMQ_HOST: str):
        self.connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_HOST))
        self.channel = self.connection.channel()

    def close_connection(self):
        self.connection.close()

    # TODO The below two functions should be more flexible to
    # allow for different queue declaration parameters in the future
    @retry(
        stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def publish(self, exchange, queue, message, declare_queue=True):
        if declare_queue:
            self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_publish(exchange=exchange, routing_key=queue, body=message)

    def start_consuming(self, queue, callback, declare_queue=True, auto_ack=True):
        if declare_queue:
            self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=auto_ack
        )
        self.channel.start_consuming()

    def stop_consuming(self):
        if self.channel.is_open:
            self.channel.stop_consuming()
