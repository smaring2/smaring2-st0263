import requests
import json

def obtener_recursos(url):
    response = requests.get(url + '/recursos')
    return response.json()

def descargar_archivo(url, nombre_archivo):
    response = requests.get(url + f'/descargar/{nombre_archivo}')
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f"El archivo '{nombre_archivo}' se ha descargado correctamente.")
    else:
        print(f"No se pudo descargar el archivo '{nombre_archivo}'.")
        
def subir_archivo(url, nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        files = {'archivo': archivo}
        response = requests.post(url + '/subir', files=files)
    print(response.json())

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)
    url = f"http://{config['ip']}:{config['port']}"
    recursos = obtener_recursos(url)
    print("Recursos disponibles:")
    for recurso in recursos:
        print(recurso)
    nombre_archivo = input("Ingrese el nombre del archivo que desea descargar: ")
    descargar_archivo(url, nombre_archivo)
    nombre_archivo_subir = input("Ingrese el nombre del archivo que desea subir: ")
    subir_archivo(url, nombre_archivo_subir)
