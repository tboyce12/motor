import sqlite3

def init():
    """Init a fresh DB."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                pk INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                status TEXT DEFAULT 'todo' CHECK (status IN ('todo', 'done'))
            );
        """)
        cx.commit()

def list_tasks():
    """Get all tasks."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("SELECT * FROM tasks;")
        return cu.fetchall()

def get_task(pk):
    """Get a task by id."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("SELECT * FROM tasks WHERE pk = ?;", (pk,))
        return cu.fetchone()

def create_task(title):
    """Insert new task."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("INSERT INTO tasks (title) VALUES (?);", (title,))
        cx.commit()

def update_task(pk, title, status):
    """Update task by id."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("UPDATE tasks SET title = ?, status = ? WHERE pk = ?;",
                   (title, status, pk,))
        cx.commit()

def delete_task(pk):
    """Delete task by id."""
    with sqlite3.connect("temp.db") as cx:
        cu = cx.cursor()
        cu.execute("DELETE FROM tasks WHERE pk = ?;", (pk,))
        cx.commit()
