# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastro e visualização de tarefas, empacotada com Docker.
Projeto do **Bootcamp II — CEUB**.

**Autor:** Thiago Seabra Aquino da Silva — RA 22600589 — Ciência da Computação — Polo [Asa Norte/Taguatinga]

## Funcionalidades
- Cadastrar tarefa com título, descrição, prioridade e data limite
- Visualizar todas as tarefas com total de pendentes e concluídas
- Validações:
  - título obrigatório (rejeita vazio ou apenas espaços)
  - prioridade aceita somente **Alta**, **Média** (ou Media) ou **Baixa**
- Status definido automaticamente como **Pendente**

## Tecnologias
- Python 3
- Git e GitHub
- Docker e Docker Compose

## Estrutura
```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Executando com Python
Pré-requisito: Python 3 instalado.

```bash
git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
cd tasktracker-projeto
python3 src/main.py
```

## Executando com Docker
Pré-requisito: Docker instalado. Execute na raiz do projeto.

### 1. Construir a imagem
```bash
docker build -t tasktracker-app .
```

### 2. Rodar o container em modo isolado (interativo)
```bash
docker run -it --rm tasktracker-app
```

### 3. Rodar via orquestração (recomendado)
```bash
docker compose run --rm tasktracker
```

> A aplicação usa `input()`, então precisa de terminal interativo: `-it` no `docker run`, e `stdin_open`/`tty` no `docker-compose.yml`.
