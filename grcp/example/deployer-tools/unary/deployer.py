import grpc
import deployer_pb2
import deployer_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = deployer_pb2_grpc.DeployerToolsStub(channel)
    # payload = [
    #     {
    #         "cwd": "/",
    #         "command": "ls -lah",
    #     },
    #     {
    #         "cwd": "/",
    #         "command": "date",
    #     }
    # ]
    payload = {
        "cwd": "/",
        "command": "ls -lah",
        }
    response = stub.ExecCMD(deployer_pb2.DeployerRequest(shellExec=payload))

    print(response.stdout.status)
    print(response.stdout.result)
    
    # for resp in response:
    #     print(resp)

if __name__ == "__main__":
    run()