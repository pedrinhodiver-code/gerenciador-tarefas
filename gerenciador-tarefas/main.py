tarefas = []

print("=== GERENCIADOR DE TAREFAS ===")

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Estatísticas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome da tarefa: ").strip()

        if nome == "" or len(nome) < 3:
            print("Nome inválido! Digite pelo menos 3 caracteres.")
        else:
            tarefas.append({"nome": nome, "feita": False})
            print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- SUAS TAREFAS ---")
            for i, tarefa in enumerate(tarefas, start=1):
                if tarefa["feita"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(f"{i}. {status} {tarefa['nome']}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para concluir.")
        else:
            numero = input("Número da tarefa a concluir: ").strip()

            if numero.isdigit():
                n = int(numero)
                if n >= 1 and n <= len(tarefas):
                    tarefas[n - 1]["feita"] = True
                    print("Tarefa concluída!")
                else:
                    print("Número fora da lista.")
            else:
                print("Digite apenas números.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            numero = input("Número da tarefa a remover: ").strip()

            if numero.isdigit() and 1 <= int(numero) <= len(tarefas):
                removida = tarefas.pop(int(numero) - 1)
                print(f"Tarefa '{removida['nome']}' removida!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        total = len(tarefas)
        concluidas = 0

        for tarefa in tarefas:
            if tarefa["feita"]:
                concluidas += 1

        pendentes = total - concluidas

        print("\n--- ESTATÍSTICAS ---")
        print(f"Total: {total}")
        print(f"Concluídas: {concluidas}")
        print(f"Pendentes: {pendentes}")

        if total > 0:
            percentual = (concluidas / total) * 100
            print(f"Progresso: {percentual:.1f}%")

    elif opcao == "0":
        print("Até logo!")
        break

    else:
        print("Opção inválida!")