FROM python:3.6.0-slim
ENV PYTHONUNBUFFERED=1
EXPOSE 8080:8080
VOLUME ./:/app
COPY ./requirements.txt ./app/
WORKDIR app
RUN pip3 install -r requirements.txt
