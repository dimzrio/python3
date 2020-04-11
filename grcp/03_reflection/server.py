from concurrent import futures
import time
import grpc
import logging
import greeting_pb2
import greeting_pb2_grpc
from grpc_reflection.v1alpha import reflection

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class GreetService(greeting_pb2_grpc.GreetServiceServicer):
    def SayHello(self, request, context):
        print(request)
        msg = "Hi, {}".format(request.message)
        return greeting_pb2.GreetResponse(message=msg)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    greeting_pb2_grpc.add_GreetServiceServicer_to_server(GreetService(),server)
    SERVICE_NAMES = (
        greeting_pb2.DESCRIPTOR.services_by_name['GreetService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(address="0.0.0.0:50051")
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()