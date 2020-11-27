from python:3.8.1-slim-buster
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
RUN pip install -r /app/requirements.txt
WORKDIR /app/
EXPOSE 5000
ENTRYPOINT uvicorn main:app --host=0.0.0.0 --port=5000