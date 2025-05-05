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
    global tasks, tasks_pk
    data = request.json
    if not data:
        abort(400)
    title = data["title"]
    t = {"pk": tasks_pk, "title": title}
    tasks.append(t)
    tasks_pk += 1
    return {"ok": True, "task": t}

@app.put("/tasks/<int:pk>")
def update_task(pk):
    global tasks, tasks_pk
    t = next((t for t in tasks if t["pk"] == pk), None)
    data = request.json
    if not t:
        abort(404)
    if not data:
        abort(400)
    title = data.get("title", t["title"])
    t["title"] = title
    return {"ok": True, "task": t}

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    global tasks, tasks_pk
    t = next((t for t in tasks if t["pk"] == pk), None)
    if not t:
        abort(404)
    tasks = [t for t in tasks if t["pk"] != pk]
    return {"ok": True}
