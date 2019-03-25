# Log Analysis - Microservices

An application of a microservices architecture to a log analysis system that detects a blacklisted IP.

## Generate the proto file:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. app.proto
```
