import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tasks")
cur.execute("DROP TABLE IF EXISTS users")

cur.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

conn.commit()
conn.close()
print("Database initialized.")
