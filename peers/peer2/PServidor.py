import grpc
import os
import json
import time
from concurrent import futures
from pathlib import Path
from mensajes_pb2 import ArchivoResponse, ArchivoRequest, RecursosResponse, NombreArchivo
import mensajes_pb2_grpc

class PServidor(mensajes_pb2_grpc.ServidorP2PServicer):
    def __init__(self, config):
        self.config = config

    def ConsultarRecursos(self, request, context):
        directorio = self.config['directory']
        recursos = []
        for archivo in Path(directorio).iterdir():
            if archivo.is_file():
                recursos.append(archivo.name)
        return RecursosResponse(recursos=recursos)

    def DescargarArchivo(self, request, context):
        directorio = self.config['directory']
        ruta_archivo = Path(directorio) / request.nombre_archivo
        if ruta_archivo.is_file():
            with open(ruta_archivo, 'rb') as archivo:
                contenido = archivo.read()
            return ArchivoResponse(contenido=contenido)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Archivo no encontrado')
            return ArchivoResponse()

    def SubirArchivo(self, request, context):
        directorio = self.config['directory']
        ruta_archivo = Path(directorio) / request.nombre_archivo
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(request.contenido)
        return ArchivoResponse()

def iniciar_servidor(config):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensajes_pb2_grpc.add_ServidorP2PServicer_to_server(PServidor(config), server)
    server.add_insecure_port(f"{config['ip']}:{config['port']}")
    server.start()
    print(f"Servidor P2P iniciado. Escuchando en el puerto {config['port']}")

    try:
        while True:
            time.sleep(3600)  # Se mantiene el servidor en ejecución durante una hora
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor detenido.")

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)['middleware']['grpc']
    iniciar_servidor(config)
