from pymongo import MongoClient
import json
import requests

response_API = requests.get('https://api.spaceflightnewsapi.net/v3/articles')
#print(response_API.status_code)
parse_json = json.loads(response_API.text)
#print(parse_json)

cluster = MongoClient("mongodb+srv://admin:admin@codeshchallenge.q5tyw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["CodeshChallenge"]
collection = db["CodeshChallenge"]


for i in parse_json:
    #verificar se id ja esta no banco
    if collection.find_one({"id": i["id"]}):
        print("id ja existe")
    else:
        collection.insert_one(i)
        print("id nao existe")

def get_all_articles():
    r = collection.find({})
    for i in r:
        print(i["title"])
    
    return r


