from concurrent import futures
import time
import datetime
import sys
sys.path.insert(0, "../proto/")
import logging

import grpc

import app_pb2
import app_pb2_grpc

import smtplib


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class LogAnalysisServicer(app_pb2_grpc.LogAnalysisServicer):

    def SendEmail(self, request, context):

        # Account for testing purposes
        user = "pkdd.microservices@gmail.com"
        password = "4j&=@:AgTC#"

        from_email = "pkdd.microservices@gmail.com"
        to_email = "patrick.dacoliat@mycit.ie"
        subject = "ALERT: Security Breach!!!"
        text = "The system was breached by the following IP address: " + request.log.split()[0]
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (from_email, to_email, subject, text)
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, password)
            server.sendmail(from_email, to_email, message)
            server.close()
            return app_pb2.SendEmailResult(sent = True)
        except:
            return app_pb2.SendEmailResult(sent = False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    app_pb2_grpc.add_LogAnalysisServicer_to_server(LogAnalysisServicer(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
