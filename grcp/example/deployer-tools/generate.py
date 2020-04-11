from grpc_tools import protoc
import os 

#library = os.path.dirname(os.__file__)
library = "../../../lib/python3.6/site-packages/"

protoc.main(
    (
        '',
        '--proto_path=.',
        '--python_out={}'.format(library),
        '--grpc_python_out={}'.format(library),
        './deployer.proto',
    )
)