from flask import Flask, request, jsonify
import json
from pathlib import Path

app = Flask(__name__)

@app.route('/recursos', methods=['GET'])
def obtener_recursos():
    directorio = app.config['DIRECTORY']
    archivos = [archivo.name for archivo in Path(directorio).iterdir() if archivo.is_file()]
    return jsonify(archivos)

@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    directorio = app.config['DIRECTORY']
    ruta_archivo = Path(directorio) / nombre_archivo
    if ruta_archivo.is_file():
        with open(ruta_archivo, 'rb') as archivo:
            contenido = archivo.read()
        return contenido, 200, {'Content-Type': 'application/octet-stream'}
    else:
        return jsonify({'mensaje': 'Archivo no encontrado'}), 404

@app.route('/subir', methods=['POST'])
def subir_archivo():
    archivo = request.files['archivo']
    directorio = app.config['DIRECTORY']
    archivo.save(Path(directorio) / archivo.filename)
    return jsonify({'mensaje': 'Archivo subido correctamente'})

if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)['api_rest']
    app.config['DIRECTORY'] = config['directory']
    app.run(host=config['host'], port=config['port'])
