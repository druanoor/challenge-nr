FROM python:3-alpine

ADD app.py /app/app.py
WORKDIR /app

CMD [ "python3", "/app/app.py","-h" ]