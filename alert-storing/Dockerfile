FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 50052

CMD ["python", "alert-storing.py"]
