FROM python:3.8-alpine
WORKDIR /app
COPY ./data/ .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py" ]