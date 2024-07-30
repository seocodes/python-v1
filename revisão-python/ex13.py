tarefas = []

while True:

    print("\nMenu:")
    print("1. Adicionar uma nova tarefa")
    print("2. Remover uma tarefa existente")
    print("3. Exibir todas as tarefas")
    print("4. Buscar uma tarefa específica")
    print("5. Sair do programa")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
  
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada!")

    elif opcao == "3":
  
        print("\nTarefas:")
        for i in range (len(tarefas)):
            print(f"{i+1}. {tarefas[i]}")

    elif opcao == "4":

        tarefa = input("Digite a tarefa a ser buscada: ")
        if tarefa in tarefas:
            print("Tarefa encontrada!")
        else:
            print("Tarefa não encontrada!")

    elif opcao == "5":

        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente!")