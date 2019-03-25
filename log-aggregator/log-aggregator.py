import sys
sys.path.insert(0, "../proto/")

import grpc

import app_pb2
import app_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = app_pb2_grpc.LogAnalysisStub(channel)
        with open("access.log") as f:
            for line in f:
                if len(line.split()) > 0:
                    print(line)


if __name__ == "__main__":
    run()
