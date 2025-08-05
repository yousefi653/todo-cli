# Todo CLI App

A simple command-line based todo application written in Python.  
It supports task management features like add, edit, remove, complete, and list with Persian (Jalali) calendar support using `jdatetime`.

---

## Features

- [x] Add new tasks with deadlines
- [x] Edit existing tasks (name, deadline, or completion status)
- [x] Remove tasks by ID
- [x] List all tasks (with optional descending order)
- [x] Mark tasks as complete
- [x] Show tasks due today
- [x] Persian (Jalali) date support
- [x] CLI shell with custom command prompt

---

## Installation

1. Clone the repository:
git clone https://github.com/yousefi653/todo-cli.git
cd todo-cli

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

3. Install dependencies:
pip install -r requirements.txt


## How to Use
python main.py

>>> add "buy eggs" 1404/06/15
>>> list
>>> edit --id 1 --task "Buy fruits"
>>> complete --id 1
>>> today
>>> remove --id 1
>>> quit


## Date Format

Use Jalali dates in format: YYYY/MM/DD
Example: 1404/06/15

The app internally formats it as:
Saturday - 1404/06/15


## Requirements

    Python 3.x

    click

    jdatetime

You can install all with:

pip install -r requirements.txt


Author

Created by Yosuef Ghasemi.
