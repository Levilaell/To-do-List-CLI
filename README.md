# 📋 Gerenciador de Tarefas (To-do List CLI)

Um projeto simples em Python que simula um sistema de tarefas com funcionalidades de **CRUD** utilizando um arquivo `JSON` como banco de dados.

---

## 🧠 Funcionalidades

- ✅ Adicionar nova tarefa
- 📄 Listar todas as tarefas
- ✅ Marcar tarefa como concluída
- ❌ Excluir tarefa por ID
- 🔍 Buscar tarefas por status (`pending` ou `completed`)

---

## 🗃️ Estrutura do Projeto

```
todolist/
├── main.py         # Contém toda a lógica das funções
├── data.json       # Arquivo usado como "banco de dados"
└── README.md       # Este arquivo
```

---

## 💻 Como usar

1. **Clone o repositório** ou copie os arquivos.
2. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```
3. Interaja com o menu no terminal.

---

## 🛠 Exemplo de uso das funções

```python
add_task("Estudar Python")
add_task("Fazer exercícios")

list_tasks()
# [1] Estudar Python - pending
# [2] Fazer exercícios - pending

complete_task(1)

get_by_status("completed")
# [1] Estudar Python - completed

delete_task(2)
```

---

## 📌 Observações

- Os dados são salvos no arquivo `data.json`. Ele é criado automaticamente se não existir.
- As tarefas têm IDs automáticos e únicos.
- O projeto pode ser expandido com novas funcionalidades (como editar tarefas, datas, prioridades etc).

---

## 🤝 Contribuições

Este projeto é para fins de estudo. Sinta-se à vontade para adaptar e melhorar!# To-do-List-CLI
