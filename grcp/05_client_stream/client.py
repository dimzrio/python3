import grpc
import addition_pb2
import addition_pb2_grpc

def numb():
        while 1:
                i = input("\nEnter a number or 'q' to quit: ")
                if i == "q":
                        break
                
                try:
                        num = int(i)
                except ValueError:
                        continue
        
                yield addition_pb2.AdditionReq(number=num)


def run():
        channel = grpc.insecure_channel("localhost:50051")
        stub = addition_pb2_grpc.AdditionStub(channel)

        r = stub.AdditionStream(numb())
        print(r)

if __name__ == "__main__":
    run()
