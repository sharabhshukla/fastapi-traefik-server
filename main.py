from datetime import time
from fastapi import FastAPI, status
import datetime


app = FastAPI()

@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return "Welcome from the root"


@app.get('/time', status_code=status.HTTP_200_OK)
def time_now():
    time_now = datetime.datetime.now()
    return {'time now': str(time_now)}


