"""TaskTracker - gerenciador de tarefas via linha de comando (Bootcamp II - CEUB)."""

PRIORIDADES = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}

tarefas = []


def ler_titulo():
    """Regra: título obrigatório. Repete até receber um valor não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio. Digite novamente.")


def ler_prioridade():
    """Regra: aceita apenas Alta, Média (ou Media) e Baixa."""
    while True:
        valor = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if valor in PRIORIDADES:
            return PRIORIDADES[valor]
        print("Erro: prioridade inválida. Use apenas Alta, Média ou Baixa.")


def cadastrar_tarefa():
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição (opcional): ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite (DD/MM/AAAA, opcional): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa['titulo']}' cadastrada com sucesso!")


def listar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for i, t in enumerate(tarefas, start=1):
        print(f"\n[{i}] {t['titulo']}")
        print(f"    Descrição:   {t['descricao'] or '-'}")
        print(f"    Prioridade:  {t['prioridade']}")
        print(f"    Data limite: {t['data_limite'] or '-'}")
        print(f"    Status:      {t['status']}")
    pendentes = sum(1 for t in tarefas if t["status"] == "Pendente")
    print(f"\nTotal: {len(tarefas)} | Pendentes: {pendentes} | Concluídas: {len(tarefas) - pendentes}")


def main():
    print("=== TaskTracker ===")
    while True:
        print("\n1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando o TaskTracker.")
