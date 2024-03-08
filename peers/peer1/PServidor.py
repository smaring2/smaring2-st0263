import grpc
import sys
import os
import json
import time
from concurrent import futures

# Añade el directorio middleware/gRPC al path de Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'middleware', 'gRPC'))

# Importa los módulos generados a partir de los archivos .proto
import mensajes_pb2
import mensajes_pb2_grpc

class PServidor(mensajes_pb2_grpc.ServidorP2PServicer):
    def __init__(self, config):
        self.config = config

    def ConsultarRecursos(self, request, context):
        recursos = ["recurso1", "recurso2", "recurso3"]  # Simulación de recursos disponibles
        return mensajes_pb2.RecursosResponse(recursos=recursos)

    def DescargarArchivo(self, request, context):
        # Aquí iría el código para descargar el archivo
        pass

    def SubirArchivo(self, request, context):
        # Aquí iría el código para subir el archivo
        pass

def iniciar_servidor(config):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensajes_pb2_grpc.add_ServidorP2PServicer_to_server(PServidor(config), server)
    server.add_insecure_port(f"{config['middleware']['grpc']['ip']}:{config['middleware']['grpc']['port']}")
    server.start()
    print("Servidor P2P iniciado. Escuchando en el puerto", config['middleware']['grpc']['port'])

    try:
        while True:
            time.sleep(3600)  # Se mantiene el servidor en ejecución durante una hora
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor detenido.")

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')) as f:
        config = json.load(f)
    iniciar_servidor(config)
