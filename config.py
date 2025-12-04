from pymongo import MongoClient

url = "mongodb+srv://cauaevaristo00_db_user:qzWOV6diWQPKTfwl@trabalho-tarefas.b8wzl6i.mongodb.net/?appName=trabalho-tarefas"



cliente = MongoClient(url)

db = cliente["lista_tarefas"]

colecao_tarefas = db["tarefas"]
