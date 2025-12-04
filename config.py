from pymongo import MongoClient

url = 



cliente = MongoClient(url)

db = cliente["lista_tarefas"]

colecao_tarefas = db["tarefas"]
