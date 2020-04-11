from concurrent import futures
import time
import grpc
import logging
import multiplication_pb2
import multiplication_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Multiplication(multiplication_pb2_grpc.MultiplicationServicer):
    def Multiplication10(self, request, context):
        print(request)

        number = request.number

        # Loop 10
        for i in range(1,11):
            result = number * i
            yield multiplication_pb2.Multiplication10Response(number=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    multiplication_pb2_grpc.add_MultiplicationServicer_to_server(Multiplication(),server)

    server.add_insecure_port(address="0.0.0.0:50051")
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()