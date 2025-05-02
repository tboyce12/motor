from flask import Flask

app = Flask(__name__)
tasks = [
    {"pk": 0, "title": "Task 0"},
    {"pk": 1, "title": "Task 1"},
    {"pk": 2, "title": "Task 2"},
]
task_pk = len(tasks)

@app.route("/")
@app.route("/tasks/")
def task_list():
    return tasks
