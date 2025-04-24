import json
import os

DATA_FILE = 'data.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_task(description):
    data = load_data()

    if data:
        max_id = max(task['id'] for task in data)
    else:
        max_id = 0

    task = {
        'id': max_id + 1,
        'description': description,
        'status': 'pending',
    }

    data.append(task)
    save_data(data)

def list_tasks():
    data = load_data()
    for task in data:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def complete_task(task_id):
    data = load_data()
    for task in data:
        if task_id == task['id']:
            task['status'] = 'completed'
            save_data(data)
            return True
    return False


def delete_task(task_id):
    data = load_data()
    new_data = [task for task in data if task_id != task['id']]

    if len(data) != len(new_data):
        save_data(new_data)
        return True
    
    return False

def get_by_status(status):
    data = load_data()

    filtered_tasks = [task for task in data if status == task['status']]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"[{task['id']}] {task['description']} - {task['status']}") 
        return True
        
    return False