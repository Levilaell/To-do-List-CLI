# 📋 Task Manager (To-do List CLI)

A simple Python project that simulates a task system with **CRUD** functionalities using a `JSON` file as the database.

---

## 🧠 Features

- ✅ Add a new task  
- 📄 List all tasks  
- ✅ Mark task as completed  
- ❌ Delete task by ID  
- 🔍 Search tasks by status (`pending` or `completed`)

---

## 🗃️ Project Structure

```
todolist/
├── main.py         # Contains all the function logic
├── data.json       # File used as a "database"
└── README.md       # This file
```

---

## 💻 How to Use

1. **Clone the repository** or copy the files.  
2. Run the `main.py` file:  
   ```bash
   python main.py
   ```  
3. Interact with the menu in the terminal.

---

## 🛠 Example Usage

```python
add_task("Study Python")
add_task("Do exercises")

list_tasks()
# [1] Study Python - pending
# [2] Do exercises - pending

complete_task(1)

get_by_status("completed")
# [1] Study Python - completed

delete_task(2)
```

---

## 📌 Notes

- Data is saved in the `data.json` file. It is automatically created if it doesn't exist.
- Tasks have unique and auto-generated IDs.
- The project can be expanded with new features (such as editing tasks, adding dates, priorities, etc).

---

## 🤝 Contributions

This project is for educational purposes. Feel free to adapt and improve it!
