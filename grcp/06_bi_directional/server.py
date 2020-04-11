import grpc
import encryption_pb2
import encryption_pb2_grpc
import time
import hashlib
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Encrypt(encryption_pb2_grpc.EncryptServicer):

    def md5(self, request, context):
        
        for req in request:
            txt = req.text
            print("Request => {}".format(txt))
            getHash = hashlib.md5(txt.encode("utf-8")).hexdigest()
            yield encryption_pb2.EncryptResponse(encrypted=getHash, text=txt)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    encryption_pb2_grpc.add_EncryptServicer_to_server(Encrypt(),server)

    server.add_insecure_port(address="0.0.0.0:50051")
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()

