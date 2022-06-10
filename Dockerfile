FROM python:3.10.5-slim-buster
RUN pip install selenium
RUN pip install python-dotenv
ARG BR_NAME=chrome
ENV BROWSER_NAME=$BR_NAME
COPY . .
CMD ["python", "selenium_python.py"]
