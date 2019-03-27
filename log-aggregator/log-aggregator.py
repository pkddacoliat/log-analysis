import time
import sys
sys.path.insert(0, "../proto/")
import logging

import grpc

import app_pb2
import app_pb2_grpc


def run():
    with grpc.insecure_channel("log-analysis:50051") as channel:
        stub = app_pb2_grpc.LogAnalysisStub(channel)
        with open("access.log") as f:
            for line in f:
                if len(line.split()) > 0:
                    response = stub.AnalyseLog(app_pb2.AnalyseLogRequest(log = line))
                    if response.ipBlacklisted == True:
                        print("IP address", response.log.split()[0], "is in the blacklist.")
                time.sleep(0.2)


if __name__ == "__main__":
    logging.basicConfig()
    run()
