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


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):
    
    def StoreAlert(self, request, context):
        result = app_pb2.StoreAlertResult(
            stored = True,
            log = request.log
        )
        print("Log has been accepted into alert-storing server...")
        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    app_pb2_grpc.add_LogAnalysisServicer_to_server(LogAnalysisServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
