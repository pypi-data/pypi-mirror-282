import os
import consul
import pika
from motor.motor_asyncio import AsyncIOMotorClient
from tenacity import retry, stop_after_attempt, wait_exponential


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


def register_service():
    service_name = os.getenv("SERVICE_NAME")
    if not service_name:
        raise ValueError("SERVICE_NAME environment variable is not set")

    service_id = os.getenv("SERVICE_ID")
    if not service_id:
        raise ValueError("SERVICE_ID environment variable is not set")

    service_host = os.getenv("SERVICE_HOST")
    if not service_host:
        raise ValueError("SERVICE_HOST environment variable is not set")

    service_port = os.getenv("SERVICE_PORT")
    if not service_port:
        raise ValueError("SERVICE_PORT environment variable is not set")
    service_port = int(service_port)

    consul_host = os.getenv("CONSUL_HOST")
    if not consul_host:
        raise ValueError("CONSUL_HOST environment variable is not set")

    consul_port = os.getenv("CONSUL_PORT")
    if not consul_port:
        raise ValueError("CONSUL_PORT environment variable is not set")
    consul_port = int(consul_port)

    consul_client = consul.Consul(host=consul_host, port=consul_port)

    consul_client.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=service_host,
        port=service_port,
        check=consul.Check().tcp(service_host, service_port, "10s"),
    )
