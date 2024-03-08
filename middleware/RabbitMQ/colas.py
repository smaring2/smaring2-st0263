import pika
import json

class ColaRabbitMQ:
    def __init__(self, config):
        self.config = config

    def enviar_mensaje(self, mensaje):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['rabbitmq']['host']))
        channel = connection.channel()
        channel.queue_declare(queue=self.config['rabbitmq']['queue'])
        channel.basic_publish(exchange='', routing_key=self.config['rabbitmq']['queue'], body=json.dumps(mensaje))
        connection.close()

    def recibir_mensaje(self, callback):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['rabbitmq']['host']))
        channel = connection.channel()
        channel.queue_declare(queue=self.config['rabbitmq']['queue'])
        
        def on_message(ch, method, properties, body):
            mensaje = json.loads(body.decode('utf-8'))
            callback(mensaje)

        channel.basic_consume(queue=self.config['rabbitmq']['queue'], on_message_callback=on_message, auto_ack=True)
        channel.start_consuming()

if __name__ == '__main__':
    config = {
        "rabbitmq": {
            "host": "localhost",
            "queue": "busqueda_archivos"
        }
    }
    cola_rabbitmq = ColaRabbitMQ(config)
    cola_rabbitmq.recibir_mensaje(print)
