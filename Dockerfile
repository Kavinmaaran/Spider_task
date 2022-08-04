FROM python:3.8-alpine
WORKDIR /app
COPY ./data/ .
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py" ]