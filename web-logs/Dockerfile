FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080:5000

CMD ["python", "web-logs.py"]
