# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import mensajes_pb2 as mensajes__pb2


class ServidorP2PStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConsultarRecursos = channel.unary_unary(
                '/p2p.ServidorP2P/ConsultarRecursos',
                request_serializer=mensajes__pb2.RecursosRequest.SerializeToString,
                response_deserializer=mensajes__pb2.RecursosResponse.FromString,
                )
        self.DescargarArchivo = channel.unary_unary(
                '/p2p.ServidorP2P/DescargarArchivo',
                request_serializer=mensajes__pb2.ArchivoRequest.SerializeToString,
                response_deserializer=mensajes__pb2.ArchivoResponse.FromString,
                )
        self.SubirArchivo = channel.unary_unary(
                '/p2p.ServidorP2P/SubirArchivo',
                request_serializer=mensajes__pb2.ArchivoRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ServidorP2PServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConsultarRecursos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescargarArchivo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubirArchivo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServidorP2PServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConsultarRecursos': grpc.unary_unary_rpc_method_handler(
                    servicer.ConsultarRecursos,
                    request_deserializer=mensajes__pb2.RecursosRequest.FromString,
                    response_serializer=mensajes__pb2.RecursosResponse.SerializeToString,
            ),
            'DescargarArchivo': grpc.unary_unary_rpc_method_handler(
                    servicer.DescargarArchivo,
                    request_deserializer=mensajes__pb2.ArchivoRequest.FromString,
                    response_serializer=mensajes__pb2.ArchivoResponse.SerializeToString,
            ),
            'SubirArchivo': grpc.unary_unary_rpc_method_handler(
                    servicer.SubirArchivo,
                    request_deserializer=mensajes__pb2.ArchivoRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.ServidorP2P', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServidorP2P(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConsultarRecursos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.ServidorP2P/ConsultarRecursos',
            mensajes__pb2.RecursosRequest.SerializeToString,
            mensajes__pb2.RecursosResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescargarArchivo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.ServidorP2P/DescargarArchivo',
            mensajes__pb2.ArchivoRequest.SerializeToString,
            mensajes__pb2.ArchivoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubirArchivo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.ServidorP2P/SubirArchivo',
            mensajes__pb2.ArchivoRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
