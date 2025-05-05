from flask import Flask, abort, request

app = Flask(__name__)
tasks = [
    {"pk": 0, "title": "Task 0"},
    {"pk": 1, "title": "Task 1"},
    {"pk": 2, "title": "Task 2"},
]
tasks_pk = len(tasks)

@app.get("/")
@app.get("/tasks/")
def list_tasks():
    return tasks

@app.get("/tasks/<int:pk>")
def get_task(pk):
    t = next((t for t in tasks if t["pk"] == pk), None)
    if not t:
        abort(404)
    return t

@app.post("/tasks")
def create_task():
    title = request.form["title"]
    global tasks, tasks_pk
    tasks.append({"pk": tasks_pk, "title": title})
    tasks_pk += 1
    return {"ok": True}
