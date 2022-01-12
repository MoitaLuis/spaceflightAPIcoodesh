from pymongo import MongoClient
import json
import requests

response_API = requests.get('https://api.spaceflightnewsapi.net/v3/articles')
cluster = MongoClient("mongodb+srv://admin:admin@codeshchallenge.q5tyw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["CodeshChallenge"]
collection = db["CodeshChallenge"]


parse_json = json.loads(response_API.text)
for i in parse_json:
    #verificar se id ja esta no banco
    if collection.find_one({"id": i["id"]}):
        print("id ja existe")
    else:
        collection.insert_one(i)
        print("id nao existe")

# retorna todos os artigos
def get_all_articles():
    r = collection.find({}).limit(5)
    for i in r:
        print(i["id"], i["title"])
    return r

# retorna um artigo com base no id
def get_article_by_id(id):
    print(id)
    r = collection.find_one({"id":id})
    print(r)

    if r:
        print(r["id"], r["title"])
        return r
    else:
        return {"Status": "404", "Mensagem": "Not Found"}

# adiciona um artigo
def add_article(article):
    print(article)
    collection.insert_one(article)
    print("Artigo adicionado")

# edita um artigo
def edit_article(id, article):
    collection.update_one({"id":id}, {"$set": article})
    print("Artigo editado")

# deleta um artigo
def delete_article(id):
    collection.delete_one({"id":id})
    print("Artigo deletado")