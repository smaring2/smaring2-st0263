import grpc
import mensajes_pb2
import mensajes_pb2_grpc
import json

class PCliente:
    def __init__(self, config):
        self.config = config

    def obtener_recursos(self):
        try:
            with grpc.insecure_channel(f"{self.config['middleware']['grpc']['ip']}:{self.config['middleware']['grpc']['port']}") as channel:
                stub = mensajes_pb2_grpc.ServidorP2PStub(channel)
                response = stub.ConsultarRecursos(mensajes_pb2.Empty())
                return response.recursos
        except grpc.RpcError as e:
            print(f"Error al obtener recursos: {e}")
            return []

    def descargar_archivo(self, nombre_archivo):
        try:
            with grpc.insecure_channel(f"{self.config['middleware']['grpc']['ip']}:{self.config['middleware']['grpc']['port']}") as channel:
                stub = mensajes_pb2_grpc.ServidorP2PStub(channel)
                response = stub.DescargarArchivo(mensajes_pb2.NombreArchivo(nombre_archivo=nombre_archivo))
                if response.contenido:
                    with open(nombre_archivo, 'wb') as f:
                        f.write(response.contenido)
                    print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
                else:
                    print(f"El archivo '{nombre_archivo}' no está disponible para descargar.")
        except grpc.RpcError as e:
            print(f"Error al descargar archivo: {e}")

    def subir_archivo(self, nombre_archivo):
        try:
            with grpc.insecure_channel(f"{self.config['middleware']['grpc']['ip']}:{self.config['middleware']['grpc']['port']}") as channel:
                stub = mensajes_pb2_grpc.ServidorP2PStub(channel)
                with open(nombre_archivo, 'rb') as f:
                    contenido = f.read()
                response = stub.SubirArchivo(mensajes_pb2.ArchivoRequest(nombre_archivo=nombre_archivo, contenido=contenido))
                print(f"El archivo '{nombre_archivo}' se ha subido correctamente.")
        except grpc.RpcError as e:
            print(f"Error al subir archivo: {e}")

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)
    cliente = PCliente(config)
    recursos = cliente.obtener_recursos()
    print("Recursos disponibles:")
    for recurso in recursos:
        print(recurso['nombre'])
    nombre_archivo_descargar = input("Ingrese el nombre del archivo que desea descargar: ")
    cliente.descargar_archivo(nombre_archivo_descargar)
    nombre_archivo_subir = input("Ingrese el nombre del archivo que desea subir: ")
    cliente.subir_archivo(nombre_archivo_subir)
