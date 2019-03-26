FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

# VOLUME [ "./proto" ]

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 50051

CMD ["python", "log-analysis.py"]
