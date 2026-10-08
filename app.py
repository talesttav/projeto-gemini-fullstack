import json

tarefas = []


def salvar_tarefas():
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def carregar_tarefas():
    global tarefas
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tarefas = []


def adicionar_tarefa(titulo, descricao):
    novo_id = max([tarefa['id'] for tarefa in tarefas], default=0) + 1
    nova_tarefa = {
        'id': novo_id,
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    print(f"Tarefa ID: {novo_id} adicionada com sucesso!")


def editar_tarefa(tarefa_id, novo_titulo=None, nova_descricao=None):
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            if novo_titulo:
                tarefa['titulo'] = novo_titulo
            if nova_descricao:
                tarefa['descricao'] = nova_descricao
            print(f"Tarefa ID: {tarefa_id} editada com sucesso!")
            return
    print(f"Tarefa ID: {tarefa_id} não encontrada.")


def remover_tarefa(tarefa_id):
    global tarefas
    tamanho_inicial = len(tarefas)
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
    
    if len(tarefas) < tamanho_inicial:
        print(f"Tarefa ID: {tarefa_id} removida com sucesso!")
    else:
        print(f"Tarefa ID: {tarefa_id} não encontrada.")


def concluir_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            print(f"Tarefa ID: {tarefa_id} concluída com sucesso!")
            return
    print(f"Tarefa ID: {tarefa_id} não encontrada.")


def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada no momento.")
        return

    print("\n--- Lista de Tarefas ---")
    for tarefa in tarefas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"ID: {tarefa['id']:02d} | Título: {tarefa['titulo']} | Status: {status}")
        if tarefa.get('descricao'):
            print(f"   Descrição: {tarefa['descricao']}")


carregar_tarefas()

while True:
    print('\n' + '=' * 30)
    print("     Gerenciador de Tarefas")
    print('=' * 30)
    print("[1]. Adicionar Tarefa")
    print("[2]. Editar Tarefa")
    print("[3]. Remover Tarefa")
    print("[4]. Concluir Tarefa")
    print("[5]. Listar Tarefas")
    print("[6]. Sair")
    print('=' * 30)

    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        titulo = input("Digite o título da tarefa (ou 0 para cancelar): ").strip()
        if titulo == '0' or not titulo:
            print("Operação cancelada.")
            continue
        descricao = input("Digite a descrição da tarefa: ").strip()
        adicionar_tarefa(titulo, descricao)
        salvar_tarefas()

    elif opcao == '2':
        try:
            tarefa_id = int(input("Digite o ID da tarefa a ser editada (ou 0 para cancelar): "))
        except ValueError:
            print("ID inválido! Digite apenas números inteiros.")
            continue

        if tarefa_id == 0:
            print("Operação cancelada.")
            continue
            
        novo_titulo = input("Digite o novo título (ou Enter para manter): ").strip()
        nova_descricao = input("Digite a nova descrição (ou Enter para manter): ").strip()
        editar_tarefa(tarefa_id, novo_titulo or None, nova_descricao or None)
        salvar_tarefas()

    elif opcao == '3':
        try:
            tarefa_id = int(input("Digite o ID da tarefa a ser removida (ou 0 para cancelar): "))
        except ValueError:
            print("ID inválido! Digite apenas números inteiros.")
            continue

        if tarefa_id == 0:
            print("Operação cancelada.")
            continue
            
        remover_tarefa(tarefa_id)
        salvar_tarefas()

    elif opcao == '4':
        try:
            tarefa_id = int(input("Digite o ID da tarefa a ser concluída (ou 0 para cancelar): "))
        except ValueError:
            print("ID inválido! Digite apenas números inteiros.")
            continue

        if tarefa_id == 0:
            print("Operação cancelada.")
            continue
            
        concluir_tarefa(tarefa_id)
        salvar_tarefas()

    elif opcao == '5':
        listar_tarefas()

    elif opcao == '6':
        print("Saindo do gerenciador de tarefas...")
        salvar_tarefas()
        break

    else:
        print("Opção inválida. Tente novamente.")