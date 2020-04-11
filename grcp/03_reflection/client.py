import grpc
import greeting_pb2
import greeting_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = greeting_pb2_grpc.GreetServiceStub(channel)
    response = stub.SayHello(greeting_pb2.GreetRequest(message="Dimas Rio"))
    print(response)

if __name__ == "__main__":
    run()
