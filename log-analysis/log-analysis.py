from concurrent import futures
import time
import datetime
import sys
sys.path.insert(0, "../proto/")
import logging

import grpc

import app_pb2
import app_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_blacklisted_ips():
    blacklisted_ips = []
    f = open("blacklist.txt", "r")
    lines = f.readlines()
    for x in lines:
        blacklisted_ips.append(x.rstrip())
    return blacklisted_ips


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):

    def AnalyseLog(self, request_iterator, context):
        blacklisted_ips = get_blacklisted_ips()

        for request in request_iterator:
            ipAddress = request.log.split()[0]
            result = app_pb2.AnalyseLogResult(
                ipBlacklisted = False,
                timeAnalysed = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S"),
                log = request.log
            )
            if ipAddress in blacklisted_ips:
                result.ipBlacklisted = True
                channel = grpc.insecure_channel("alert-storing:50052")
                stub = app_pb2_grpc.LogAnalysisStub(channel)
                response = stub.StoreAlert(result)
                
            yield result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    app_pb2_grpc.add_LogAnalysisServicer_to_server(LogAnalysisServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("log-analysis server running...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
