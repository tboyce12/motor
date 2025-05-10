import jwt
from flask import Flask, abort, request, g
from functools import wraps
import db

SECRET_KEY = "change me!"
app = Flask(__name__)
db.init()

def require_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization")
        if not header:
            abort(401)
        token = header.split()[1]
        try:
            g.user_id = jwt.decode(
                token, SECRET_KEY, algorithms=["HS256"]
            )["user_id"]
        except:
            abort(401)
        return f(*args, **kwargs)
    return wrapper

@app.post("/login")
def user_login():
    token = jwt.encode({"user_id": "foo"}, SECRET_KEY)
    return {"token": token}

@app.get("/")
@app.get("/tasks/")
@require_login
def task_list():
    return [{"pk": t[0], "title": t[1], "status": t[2]}
            for t in db.list_tasks()]

@app.get("/tasks/<int:pk>")
@require_login
def task_get(pk):
    t = db.get_task(pk)
    if not t:
        abort(404)
    return {"pk": t[0], "title": t[1], "status": t[2]}

@app.post("/tasks")
@require_login
def task_create():
    data = request.json
    if not data:
        abort(400)
    title = data.get("title")
    if not title:
        abort(400)
    db.create_task(title)
    return {}

@app.put("/tasks/<int:pk>")
@require_login
def task_update(pk):
    data = request.json
    if not data:
        abort(400)
    title = data.get("title")
    status = data.get("status")
    if not title or not status:
        abort(400)
    db.update_task(pk, title, status)
    return {}

@app.delete("/tasks/<int:pk>")
@require_login
def task_delete(pk):
    db.delete_task(pk)
    return {}
