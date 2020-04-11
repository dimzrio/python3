import grpc
import deployer_pb2
import deployer_pb2_grpc
from deployer_pb2 import Exec

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = deployer_pb2_grpc.DeployerToolsStub(channel)

    payload = []
    for i in range(3):
        payload.append(Exec(cmd="date", cwd="/"))

    response = stub.ExecCMD(deployer_pb2.DeployerRequest(shellExec=payload))

    for r in response:
        print(r)
            
    # for resp in response:
    #     print(resp)

if __name__ == "__main__":
    run()