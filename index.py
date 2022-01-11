from fastapi import FastAPI
from requests.models import to_native_string
from mongo import get_all_articles, get_article_id


app = FastAPI()

@app.get("/")
def home():
    return {"Status": "200", "Mensagem": "Back-end Challenge 2021 🏅 - Space Flight News"}

@app.get("/articles")
def articles():
    r = get_all_articles()
    return r

@app.get("/articles/{id}")
def articles_id(id: int):
    r = get_article_id(id)
    r["_id"] = str(r["_id"])
    return r