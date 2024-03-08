import grpc
import sys
import os
import json
import pika
import uuid

# Añade el directorio middleware/gRPC al path de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'middleware', 'gRPC'))

# Importa los módulos necesarios desde mensajes_pb2
from mensajes_pb2_grpc import ServidorP2PStub
from google.protobuf.empty_pb2 import Empty  # Importa Empty desde google.protobuf.empty_pb2
import mensajes_pb2  # Importa mensajes_pb2 para poder utilizar ArchivoRequest

class PCliente:
    def __init__(self, config):
        self.config = config

    def obtener_recursos(self):
        archivos_disponibles = os.listdir(os.path.join(os.path.dirname(__file__), 'archivos'))
        return archivos_disponibles

    def descargar_archivo(self, nombre_archivo):
        recursos_disponibles = self.obtener_recursos()
        if nombre_archivo in recursos_disponibles:
            # Simulamos la descarga del archivo imprimiendo un mensaje
            print(f"Descargando '{nombre_archivo}'...")
            print("Descarga exitosa.")
        else:
            print(f"El archivo '{nombre_archivo}' no está disponible para descargar.")
        return None  # Simplemente retorna None para indicar que la descarga fue exitosa

    def subir_archivo(self, nombre_archivo):
    # Verificar si el archivo está en la lista de recursos disponibles
        if nombre_archivo not in self.obtener_recursos():
            print(f"El archivo '{nombre_archivo}' no está disponible para subir.")
            return
    
        with grpc.insecure_channel(f"{self.config['middleware']['grpc']['ip']}:{self.config['middleware']['grpc']['port']}") as channel:
            stub = ServidorP2PStub(channel)
            with open(os.path.join(self.config['middleware']['grpc']['directory'], nombre_archivo), 'rb') as archivo:
                contenido = archivo.read()
            stub.SubirArchivo(mensajes_pb2.ArchivoRequest(nombre_archivo=nombre_archivo, contenido=contenido))
        print(f"El archivo '{nombre_archivo}' se ha subido correctamente.")

    def buscar_archivo(self, nombre_archivo):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config['middleware']['rabbitmq']['host']))
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
            routing_key=self.config['middleware']['rabbitmq']['queue'],
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
    with open(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')) as f:
        config = json.load(f)
    cliente = PCliente(config)
    recursos = cliente.obtener_recursos()
    print("Recursos disponibles:")
    for recurso in recursos:
        print(recurso)
    nombre_archivo = input("Ingrese el nombre del archivo que desea descargar: ")
    cliente.descargar_archivo(nombre_archivo)
    nombre_archivo_subir = input("Ingrese el nombre del archivo que desea subir: ")
    cliente.subir_archivo(nombre_archivo_subir)
