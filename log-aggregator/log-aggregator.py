import time
import sys
sys.path.insert(0, "../proto/")
import logging

import grpc

import app_pb2
import app_pb2_grpc


def read_logs():
    with open("access.log") as f:
        for line in f:
            if len(line.split()) > 0:
                yield app_pb2.AnalyseLogRequest(log = line)
            time.sleep(0.2)


def run():
    channel = grpc.insecure_channel("log-analysis:50051")
    stub = app_pb2_grpc.LogAnalysisStub(channel)
    logs = stub.AnalyseLog(read_logs())
    try:
        for log in logs:
            print(log.ipBlacklisted)
    except grpc._channel._Rendezvous as err:
        print(err)


if __name__ == "__main__":
    logging.basicConfig()
    run()
