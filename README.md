# info de la materia: st0263 Topicos especiales en Telematica
#
# Estudiante(s): Sebastián Marín Gallego, email: smaring2@eafit.edu.co
#
# Profesor: Juan Carlos Montoya
#
# P2P - Comunicación entre procesos mediante API REST, RPC y MOM
#
# 1. breve descripción de la actividad
#
<La actividad se centra en implementar una comunicación entre procesos (P2P) utilizando diferentes mecanismos como API REST, RPC (Remote Procedure Call) y MOM (Message-Oriented Middleware). El objetivo es desarrollar un sistema distribuido donde los procesos (peers) puedan comunicarse entre sí para compartir recursos y realizar consultas.>
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Implementación de comunicación entre procesos utilizando API REST, RPC y MOM.
Estructura de red P2P no estructurada.
Desarrollo de módulos de servidor (PServidor) y cliente (PCliente) para cada peer.
Punto de acceso al servicio a través de cualquier peer en la red.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Algunas funcionalidades como la carga de un recurso dummy no fueron implementadas.
# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
El sistema está diseñado utilizando una arquitectura distribuida P2P, donde cada peer actúa como cliente y servidor. Se siguen prácticas de desarrollo de software y se implementan patrones de diseño para mantener la modularidad y la escalabilidad del sistema.
# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Lenguaje de Programación: Python
Librerías y Paquetes: gRPC, RabbitMQ, Flask, etc.
Detalles de Desarrollo: Compilación, Ejecución, Detalles Técnicos, Configuración de Parámetros del Proyecto.

/*La propuesta para utilizar múltiples middlewares en un sistema P2P no estructurado y descentralizado incluye:

Comunicación Cliente-Servidor con gRPC:

Se emplea gRPC para facilitar una comunicación eficiente y de alto rendimiento entre el cliente y el servidor.
Se definen servicios y mensajes gRPC para llevar a cabo las operaciones principales, como consultas de recursos, descarga y carga de archivos.
Los métodos del servidor gRPC se implementan para manejar las solicitudes del cliente y proporcionar las respuestas correspondientes.
Comunicación entre Nodos con RabbitMQ (MOM):

Se utiliza RabbitMQ como middleware de mensajería para posibilitar la comunicación entre los nodos.
Se establecen colas de mensajes para la búsqueda de recursos y la difusión de información sobre la ubicación de archivos entre los nodos.
Cuando un nodo requiere buscar un recurso en la red, publica un mensaje en la cola correspondiente, y los nodos que poseen dicho recurso responden con su ubicación.
Interfaz de Usuario y Exposición de Servicios con API REST:

Se emplea API REST para exponer la funcionalidad del sistema a través de una interfaz de usuario web o móvil.
Se definen endpoints REST para las operaciones principales, como búsqueda de recursos, descarga y carga de archivos.
El cliente de consola (PCliente) también puede interactuar con el sistema mediante estos endpoints REST./*
## como se compila y ejecuta.
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto
