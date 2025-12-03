import json
import os


def write_json(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
    return True


def get_data():
    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
        with open("tasks.json", "r") as file:
            return json.load(file)
    with open("tasks.json", "w") as file:
        json.dump([], file)
        return []
