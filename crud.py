from config import colecao_tarefas
from datetime import datetime
from bson.objectid import ObjectId

def criar_tarefa(titulo, descricao, tags=[]):
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data_criacao": datetime.now(),
        "status": "pendente",
        "tags": tags,
        "comentarios": []
    }
    
    m = colecao_tarefas.insert_one(tarefa)
    print(f"Tarefa criada com ID: {m.inserted_id}")
    return m.inserted_id

def buscar_por_id(id):
    tarefa = colecao_tarefas.find_one({"_id": ObjectId(id)})
    return tarefa


def listar_tarefas():
    tarefas = colecao_tarefas.find()
    return list(tarefas)

def buscar_por_status(status):
    tarefas = colecao_tarefas.find({"status": status})
    return list(tarefas)

def buscar_por_tag(tag):
    tarefas = colecao_tarefas.find({"tag":tag})
    return list(tarefas)

def atualizar_status(id, novo):
    m = colecao_tarefas.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"status": novo}}
    )
    print(f"status da terafa: {m.modified_count} modificado para {novo} ")
    return m.modified_count

def adicionar_comentario(id, texto):
    comentario = {
        "texto": texto,
        "data": datetime.now()
    }
    m = colecao_tarefas.update_one(
        {"_id": ObjectId(id)},
        {"$push": {"comentarios": comentario}}
    )
    print(f"Comentarios adicionados: {m.modified_count}")
    return m.modified_count

def deletar_tarefa(id):
    m = colecao_tarefas.delete_one({"_id": ObjectId(id)})
    print(f"Tarefa deletada: {m.deleted_count}")
    return m.deleted_count