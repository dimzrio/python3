import grpc
import multiplication_pb2
import multiplication_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = multiplication_pb2_grpc.MultiplicationStub(channel)
    response = stub.Multiplication10(multiplication_pb2.Multiplication10Request(number=12))
    
    for resp in response:
        print(resp)

if __name__ == "__main__":
    run()
