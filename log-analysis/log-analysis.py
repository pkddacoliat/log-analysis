from concurrent import futures
import time
import sys
sys.path.insert(0, "../proto/")

import grpc

import app_pb2
import app_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def read_file():
    blacklisted_ips = []
    f = open("blacklist.txt", "r")
    lines = f.readlines()
    for x in lines:
        blacklisted_ips.append(x.rstrip())
    return blacklisted_ips


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):

    def AnalyseLog(self, request, context):
        blacklisted_ips = read_file()
        return app_pb2.Result(bool=request.ipAddress in blacklisted_ips)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
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
    serve()