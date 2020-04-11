from concurrent import futures
import time
import grpc
import greeting_pb2
import greeting_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class GreetService(greeting_pb2_grpc.GreetServiceServicer):
    def SayHello(self, request, context):
        print(request)
        msg = "Hi, {}".format(request.message)
        return greeting_pb2.GreetResponse(message=msg)

def serve():

    with open("./ssl/server.key", "rb") as f:
        private_key = f.read()

    with open("./ssl/server.crt","rb") as f:
        cert = f.read()

    cred = grpc.ssl_server_credentials(
        private_key_certificate_chain_pairs=((private_key,cert,),)
        )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    greeting_pb2_grpc.add_GreetServiceServicer_to_server(GreetService(),server)
    server.add_secure_port("0.0.0.0:50051", cred)
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()