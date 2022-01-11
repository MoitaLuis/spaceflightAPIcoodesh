from fastapi import FastAPI
from datetime import date


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/date")
def home():
    d = date.today()
    return {"Date": d}