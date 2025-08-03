import json
import os

def write_json(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def get_data():
    if not os.path.exists('tasks.json'):
        open('tasks.json', 'w').close()
        return []
    else:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    