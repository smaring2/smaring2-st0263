import uuid
import pika
import json

class RabbitMQCliente:
    def __init__(self, config):
        self.config = config

    def buscar_archivo(self, nombre_archivo):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['rabbitmq']['host']))
        channel = connection.channel()
        result = channel.queue_declare(queue='', exclusive=True)
        callback_queue = result.method.queue

        def on_response(ch, method, properties, body):
            if properties.correlation_id == self.correlation_id:
                self.response = json.loads(body)

        self.response = None
        self.correlation_id = str(uuid.uuid4())
        channel.basic_publish(
            exchange='',
            routing_key=self.config['rabbitmq']['queue'],
            properties=pika.BasicProperties(
                reply_to=callback_queue,
                correlation_id=self.correlation_id,
            ),
            body=json.dumps({'tipo': 'busqueda', 'nombre_archivo': nombre_archivo})
        )
        while self.response is None:
            connection.process_data_events()
        return self.response

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)
    cliente = RabbitMQCliente(config)
    archivos_encontrados = cliente.buscar_archivo('archivo1.txt')
    print("Archivos encontrados:", archivos_encontrados)
