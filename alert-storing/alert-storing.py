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


def time_difference(start_time, end_time):
    start = datetime.datetime.strptime(start_time, "%d/%b/%Y:%H:%M:%S")
    end = datetime.datetime.strptime(end_time, "%d/%b/%Y:%H:%M:%S")
    difference = end - start
    seconds = difference.total_seconds()
    return int(seconds)


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):
    
    def StoreAlert(self, request, context):
        ipAddress = request.log.split()[0]
        timeAnalysed = request.timeAnalysed

        result = app_pb2.StoreAlertResult(
            stored = False,
            timeAnalysed = timeAnalysed,
            log = request.log
        )

        try:
            conn = redis.StrictRedis(host="redis", port=6379)

            ipAddressFound = False
            recentAlertTime = ""
            shouldSendAlert = True

            for key in conn.scan_iter():
                if ipAddress in str(key):
                    ipAddressFound = True
                    recentAlertTime = key[:20]
            
            if ipAddressFound == True:
                if time_difference(timeAnalysed, recentAlertTime) > _ONE_DAY_IN_SECONDS:
                    conn.set(timeAnalysed + "_" + ipAddress, request.log)
                else:
                    shouldSendAlert = False
            else:
                conn.set(timeAnalysed + "_" + ipAddress, request.log)

            if shouldSendAlert == True:
                with grpc.insecure_channel("email-server:50053") as channel:
                    stub = app_pb2_grpc.LogAnalysisStub(channel)
                    response = stub.SendEmail(result)
                    
        except Exception as ex:
            print("Error:", ex)

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
