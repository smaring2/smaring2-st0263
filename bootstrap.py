import os
import subprocess
import json
import time

# Constantes
PEERS_DIR = "peers"
CONFIG_FILE = "config.json"
MIDDLEWARE_DIR = "middleware"

def iniciar_peer(peer_name, peer_config):
    """Inicia el servidor y cliente del peer."""
    peer_dir = os.path.join(PEERS_DIR, peer_name)
    subprocess.Popen(['python', 'PServidor.py'], cwd=peer_dir)
    subprocess.Popen(['python', 'PCliente.py'], cwd=peer_dir)

def iniciar_servicios(config):
    """Inicia los servicios gRPC y RabbitMQ."""
    grpc_servidor_process = subprocess.Popen(['python', os.path.join(MIDDLEWARE_DIR, 'gRPC', 'servidor.py')], cwd=MIDDLEWARE_DIR)
    rabbitmq_servidor_process = subprocess.Popen(['python', os.path.join(MIDDLEWARE_DIR, 'RabbitMQ', 'servidor.py')], cwd=MIDDLEWARE_DIR)
    return grpc_servidor_process, rabbitmq_servidor_process

def main():
    # Cargar la configuración desde el archivo config.json
    with open(CONFIG_FILE) as f:
        config = json.load(f)

    # Iniciar los servicios gRPC y RabbitMQ
    grpc_servidor_process, rabbitmq_servidor_process = iniciar_servicios(config['middleware'])

    # Iniciar cada peer
    for peer in config['peers']:
        iniciar_peer(peer['name'], peer)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Detener los procesos cuando se interrumpe con Ctrl+C
        grpc_servidor_process.terminate()
        rabbitmq_servidor_process.terminate()

if __name__ == "__main__":
    main()
