from flask import Flask, abort, request
import db

app = Flask(__name__)

db.init()

@app.get("/")
@app.get("/tasks/")
def list_tasks():
    return [{"pk": t[0], "title": t[1], "status": t[2]}
            for t in db.list_tasks()]

@app.get("/tasks/<int:pk>")
def get_task(pk):
    t = db.get_task(pk)
    return {"pk": t[0], "title": t[1], "status": t[2]}

@app.post("/tasks")
def create_task():
    data = request.json
    if not data:
        abort(400)
    title = data.get("title")
    if not title:
        abort(400)
    db.create_task(title)
    return {"ok": True}

@app.put("/tasks/<int:pk>")
def update_task(pk):
    data = request.json
    if not data:
        abort(400)
    title = data.get("title")
    status = data.get("status")
    if not title or not status:
        abort(400)
    db.update_task(pk, title, status)
    return {"ok": True}

@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    db.delete_task(pk)
    return {"ok": True}
