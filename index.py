from fastapi import FastAPI
from mongo import get_all_articles 


app = FastAPI()

@app.get("/")
def home():
    return {"Status": "200", "Mensagem": "Back-end Challenge 2021 🏅 - Space Flight News"}

@app.get("/articles")
def articles():
    r = get_all_articles()
    return r
