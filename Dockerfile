FROM python:3.8-slim
WORKDIR /app
COPY app.py ./app.py
CMD [ "python", "./app.py" ]