from concurrent import futures
import time
import datetime
import sys
sys.path.insert(0, "../proto/")
import logging

import grpc

import app_pb2
import app_pb2_grpc

import redis


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_blacklisted_ips():
    blacklisted_ips = []
    f = open("blacklist.txt", "r")
    lines = f.readlines()
    for x in lines:
        blacklisted_ips.append(x.rstrip())
    return blacklisted_ips


def time_difference(start_time, end_time):
    start = datetime.datetime.strptime(start_time, "%d/%b/%Y:%H:%M:%S")
    end = datetime.datetime.strptime(end_time, "%d/%b/%Y:%H:%M:%S")
    difference = end - start
    seconds = difference.total_seconds()
    return int(seconds)


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):

    def AnalyseLog(self, request, context):
        blacklisted_ips = get_blacklisted_ips()
        result = app_pb2.AnalyseLogResult(
            ipBlacklisted = False, 
            ipAddress = request.log.split()[0], 
            timeProcessed = request.log.split()[3].strip("[")
        )
        if request.log.split()[0] in blacklisted_ips:
            result.ipBlacklisted = True
            with grpc.insecure_channel('email-server:50052') as channel:
                stub = app_pb2_grpc.LogAnalysisStub(channel)
                response = stub.SendEmail(result)
        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    app_pb2_grpc.add_LogAnalysisServicer_to_server(LogAnalysisServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
