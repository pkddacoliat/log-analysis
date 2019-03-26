from concurrent import futures
import time
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

    def AnalyseLog(self, request, context):
        blacklisted_ips = get_blacklisted_ips()
        if request.log.split()[0] in blacklisted_ips:
            return app_pb2.AnalyseLogResult (
                ipBlacklisted = True, 
                ipAddress = request.log.split()[0], 
                timeProcessed = request.log.split()[3]
            )
        else:
            return app_pb2.AnalyseLogResult (
                ipBlacklisted = False, 
                ipAddress = request.log.split()[0], 
                timeProcessed = request.log.split()[3]
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    app_pb2_grpc.add_LogAnalysisServicer_to_server(LogAnalysisServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("SERVER RUNNING...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
