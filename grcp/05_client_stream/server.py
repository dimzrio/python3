from concurrent import futures
import time
import grpc
import logging
import addition_pb2
import addition_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Addition(addition_pb2_grpc.AdditionServicer):
    def AdditionStream(self, request, context):
        result = 0
        for req in request:
            print("Request => {}".format(req))
            n = req.number
            result = result + n
        
        return addition_pb2.AdditionResp(number=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    addition_pb2_grpc.add_AdditionServicer_to_server(Addition(),server)

    server.add_insecure_port(address="0.0.0.0:50051")
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()