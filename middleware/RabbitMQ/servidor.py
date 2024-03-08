import os
import pika
import json
import time

class RabbitMQServidor:
    def __init__(self, config):
        self.config = config

    def iniciar_servidor(self):
        try:
            # Establecer conexión con RabbitMQ
            print("Conectando al servidor RabbitMQ...")
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['middleware']['rabbitmq']['host']))
            channel = connection.channel()
            channel.queue_declare(queue=self.config['middleware']['rabbitmq']['queue'])

            # Definir función de callback para procesar mensajes
            def callback(ch, method, properties, body):
                mensaje = json.loads(body.decode('utf-8'))
                if mensaje['tipo'] == 'busqueda':
                    archivos_encontrados = self.buscar_archivo(mensaje['nombre_archivo'])
                    respuesta = {'archivos_encontrados': archivos_encontrados}
                    channel.basic_publish(exchange='', routing_key=properties.reply_to, body=json.dumps(respuesta))

            # Configurar consumidor para recibir mensajes
            channel.basic_consume(queue=self.config['middleware']['rabbitmq']['queue'], on_message_callback=callback, auto_ack=True)
            print("Servidor RabbitMQ iniciado. Esperando mensajes...")

            # Mantener el servidor en ejecución indefinidamente
            while True:
                connection.process_data_events()  # Procesar eventos de datos para mantener la conexión activa

        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error de conexión a RabbitMQ: {e}")
            print("Asegúrate de que el servidor RabbitMQ esté en ejecución y accesible.")

    def buscar_archivo(self, nombre_archivo):
        directorio = self.config['peers'][0]['directory']
        archivos_encontrados = []
        # Verificar si el directorio de archivos existe
        if os.path.exists(directorio) and os.path.isdir(directorio):
            for archivo in os.listdir(directorio):
                if archivo == nombre_archivo:
                    archivos_encontrados.append(archivo)
        else:
            print(f"El directorio de archivos especificado ({directorio}) no existe.")
        return archivos_encontrados

if __name__ == '__main__':
    # Obtener la ruta del archivo config.json desde el directorio raíz del proyecto
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')

    with open(config_path) as f:
        config = json.load(f)
    
    servidor = RabbitMQServidor(config)
    servidor.iniciar_servidor()
