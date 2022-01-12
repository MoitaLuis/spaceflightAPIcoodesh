from fastapi import FastAPI
from requests.models import to_native_string
from mongo import get_all_articles, get_article_by_id, add_article, edit_article, delete_article
from models import artigo

app = FastAPI()

# Retornar um Status: 200 e uma Mensagem "Back-end Challenge 2021 🏅 - Space Flight News"
@app.get("/")
def home():
    return {"Status": "200", "Mensagem": "Back-end Challenge 2021 🏅 - Space Flight News"}

# Listar todos os artigos da base de dados, utilizar o sistema de paginação para não sobrecarregar a REQUEST
@app.get("/articles")
def articles():
    r = get_all_articles()
    return r

# Obter a informação somente de um artigo
@app.get("/articles/{id}")
def articles_id(id: int):
    r = get_article_by_id(id)
    r["_id"] = str(r["_id"])
    return r

# Adicionar um artigo
@app.post("/new-article")
def articles_post(article: artigo):
    add_article(article.__dict__)
    return {"Status": "200", "Mensagem": "Artigo adicionado"}

""""
# Atualizar um artigo baseado no id
@app.put("/articles/{id}")
def articles_put(id: int, article):
    edit_article(id, article)
    return {"Status": "200", "Mensagem": "Artigo editado"}
"""
# Remover um artigo baseado no id
@app.delete("/delete-article/{id}")
def articles_delete(id: int):
    delete_article(id)
    return {"Status": "200", "Mensagem": "Artigo deletado"}