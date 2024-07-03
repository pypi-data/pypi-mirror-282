import pika
import json

class RabbitStore:
    @staticmethod
    def _connect(**kwargs):
        connection_params = pika.ConnectionParameters(
            host=kwargs.get('host', 'localhost'),
            port=kwargs.get('port', 5672),
            virtual_host=kwargs.get('virtual_host', '/'),
            credentials=pika.PlainCredentials(
                username=kwargs.get('username', 'guest'),
                password=kwargs.get('password', 'guest')
            )
        )
        return pika.BlockingConnection(connection_params)

    @staticmethod
    def _declare_queue(channel, key):
        channel.queue_declare(queue=key, durable=True)

    @staticmethod
    def set(key, value, **kwargs):
        connection = RabbitStore._connect(**kwargs)
        channel = connection.channel()
        RabbitStore._declare_queue(channel, key)
        if value is None:
            channel.queue_purge(queue=key)
        else:
            channel.basic_publish(
                exchange='',
                routing_key=key,
                body=json.dumps(value),
                properties=pika.BasicProperties(delivery_mode=2)
            )
        connection.close()

    @staticmethod
    def get(key, **kwargs):
        connection = RabbitStore._connect(**kwargs)
        channel = connection.channel()
        RabbitStore._declare_queue(channel, key)

        method_frame, header_frame, body = channel.basic_get(queue=key, auto_ack=False)
        
        # Ensure the message is requeued
        if method_frame:
            channel.basic_nack(delivery_tag=method_frame.delivery_tag, requeue=True)
        
        connection.close()

        if body:
            return json.loads(body)
        return None
