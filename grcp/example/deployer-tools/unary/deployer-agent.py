from concurrent import futures
import time
import grpc
import subprocess
import deployer_pb2
import deployer_pb2_grpc

ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DeployerTools(deployer_pb2_grpc.DeployerToolsServicer):

    def shell_exec(self, execute):
        cmd = execute["command"]
        cwd = execute["cwd"]

        shellexec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        stdout, stderr = shellexec.communicate()

        stdout_exec = {}

        if stderr:
            stdout_exec['result'] = "{0}".format(stderr.decode("utf-8"))
            stdout_exec['status'] = 'failed'
        else:
            stdout_exec['result'] = "{0}".format(stdout.decode("utf-8"))
            stdout_exec['status'] = 'success'

        return stdout_exec

        #data = {}
        # try:
        #     cmd = cmd["command"]
        #     cwd = cmd["cwd"]

        #     cmd = cmd.strip()
        #     shellexec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        #     stdout, stderr = shellexec.communicate()

        #     stdout_exec = {}
            
        #     if stderr:
        #         stdout_exec[cmd] = "{0}".format(stderr.decode("utf-8"))
        #         data['status'] = 'failed'
        #     else:
        #         stdout_exec[cmd] = "{0}".format(stdout.decode("utf-8"))
        #         data['status'] = 'success'

        #     data["result"] = stdout_exec
            
        # except Exception as e:
        #     data['status'] = 'failed'
        #     data['result'] = '{0}'.format(e)

        # return data


    def ExecCMD(self, request, context):

        execute = {
            "command": request.shellExec.command,
            "cwd": request.shellExec.cwd
        }
        stdout = self.shell_exec(execute)

        return deployer_pb2.DeployerResponse(stdout=stdout)

        # for r in request:
        #     stdout = self.shell_exec(r)
        #     yield deployer_pb2.DeployerResponse(stdout=stdout)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    deployer_pb2_grpc.add_DeployerToolsServicer_to_server(DeployerTools(),server)

    server.add_insecure_port(address="0.0.0.0:50051")
    server.start()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()

        
# from concurrent impor futures
# import time
# import grpc
# import logging
# import deployer_pb2
# import deployer_pb2_grpc

# _ONE_DAY_IN_SECONDS = 60 * 60 * 24

# class Multiplication(deployer_pb2_grpc.DeployerToolsService):
#     def Multiplication10(self, request, context):
#         print(request)

#         number = request.number

#         # Loop 10
#         for i in range(1,11):
#             result = number * i
#             yield multiplication_pb2.Multiplication10Response(number=result)

# def serve():
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
#     multiplication_pb2_grpc.add_MultiplicationServicer_to_server(Multiplication(),server)

#     server.add_insecure_port(address="0.0.0.0:50051")
#     server.start()

#     try:
#         while True:
#             time.sleep(_ONE_DAY_IN_SECONDS)
#     except KeyboardInterrupt:
#         server.stop(0)
        
# if __name__ == '__main__':
#     serve()