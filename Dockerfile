FROM python:3.10.5-slim-buster

RUN pip install -y selenium

COPY . .

CMD python selenium_python.py
