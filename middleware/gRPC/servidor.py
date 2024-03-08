import shutil
import os
import grpc
import mensajes_pb2
import mensajes_pb2_grpc
import json
from concurrent import futures
from pathlib import Path

class ServidorP2P(mensajes_pb2_grpc.ServidorP2PServicer):
    def __init__(self, config):
        self.config = config

    def ConsultarRecursos(self, request, context):
        directorio = self.config['directory']
        recursos = []
        for archivo in Path(directorio).iterdir():
            if archivo.is_file():
                nombre_archivo = archivo.name
                url_archivo = f"http://{self.config['middleware']['grpc']['ip']}:{self.config['middleware']['grpc']['port']}/{nombre_archivo}"
                recursos.append({'nombre': nombre_archivo, 'url': url_archivo})
        return mensajes_pb2.RecursosResponse(recursos=recursos)

    def DescargarArchivo(self, request, context):
        directorio = self.config['directory']
        ruta_archivo = Path(directorio) / request.nombre_archivo
        if ruta_archivo.is_file():
            with open(ruta_archivo, 'rb') as archivo:
                contenido = archivo.read()
            return mensajes_pb2.ArchivoResponse(contenido=contenido)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Archivo no encontrado')
            return mensajes_pb2.ArchivoResponse()

    def SubirArchivo(self, request, context):
        directorio = self.config['directory']
        ruta_archivo = Path(directorio) / request.nombre_archivo
        try:
            with open(ruta_archivo, 'wb') as archivo:
                archivo.write(request.contenido)
            return mensajes_pb2.Empty()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Error al subir el archivo: {str(e)}')
            return mensajes_pb2.Empty()

def iniciar_servidor(config):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensajes_pb2_grpc.add_ServidorP2PServicer_to_server(ServidorP2P(config), server)
    server.add_insecure_port(f"{config['ip']}:{config['port']}")
    server.start()
    print("Servidor gRPC iniciado...")
    server.wait_for_termination()

if __name__ == '__main__':
    # Copiar el archivo config.json al directorio del servidor gRPC
    shutil.copy('config.json', 'directorio_del_servidor_gRPC')  # Reemplaza 'directorio_del_servidor_gRPC' con el directorio real
    # Cargar la configuración del archivo config.json
    with open('config.json') as f:
        config = json.load(f)['middleware']['grpc']
    iniciar_servidor(config)
