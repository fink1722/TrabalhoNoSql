from crud import (
    criar_tarefa,
    listar_tarefas,
    buscar_por_id,
    buscar_por_status,
    buscar_por_tag,
    atualizar_status,
    adicionar_comentario,
    deletar_tarefa
)


id1 = criar_tarefa(
    titulo="Estudar MongoDB",
    descricao="Ler material e fazer exercícios práticos",
    tags=["estudo", "faculdade"]
)

id2 = criar_tarefa(
    titulo="Fazer compras",
    descricao="Comprar frutas e verduras",
    tags=["pessoal", "casa"]
)

id3 = criar_tarefa(
    titulo="Revisar prova",
    descricao="Revisar conteúdo de banco de dados",
    tags=["estudo", "faculdade"]
)


print("\n=== Listando todas as tarefas ===")
tarefas = listar_tarefas()
for tarefa in tarefas:
    print(f"- {tarefa['titulo']} ({tarefa['status']})")


tarefas_faculdade = buscar_por_tag("faculdade")
for tarefa in tarefas_faculdade:
    print(f"- {tarefa['titulo']}")


###atualizar_status(id1, "em andamento")