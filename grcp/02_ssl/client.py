import grpc
import greeting_pb2
import greeting_pb2_grpc

def run():

    with open("./ssl/server.crt", "rb") as f:
        cert = f.read()

    cred = grpc.ssl_channel_credentials(root_certificates=cert)
    channel = grpc.secure_channel("localhost:50051", cred)
    stub = greeting_pb2_grpc.GreetServiceStub(channel)
    response = stub.SayHello(greeting_pb2.GreetRequest(message="Dimas Rio"))
    print(response)

if __name__ == "__main__":
    run()
