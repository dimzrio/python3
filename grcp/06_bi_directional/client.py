import grpc
import encryption_pb2
import encryption_pb2_grpc
import time
import sys

def getHash():
    while True:
        getText = input("\nPlease input string, or press \"q\" to quit: ")
        
        if getText.lower() == "q":
            break
        
        yield encryption_pb2.EncryptRequest(text=getText)
        time.sleep(1)
        
def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = encryption_pb2_grpc.EncryptStub(channel)
    response = stub.md5(getHash())

    try:
        for resp in response:
            print("Response => Text: {0}, Hash: {1}".format(resp.text, resp.encrypted))
    except KeyboardInterrupt:
        pass
        sys.exit(0)

if __name__ == "__main__":
    run()