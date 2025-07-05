import sqlite3

conn = sqlite3.connect("projects.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    path TEXT NOT NULL,
    port INTEGER NOT NULL,
    entry TEXT
)
""")


cursor.execute("""
INSERT INTO projects (id, name, type, path, port, entry)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "my-flask-app",
    "My Flask App",
    "flask",
    "C:/Users/Tamer/Documents/my-flask-app",
    5610,
    "main.py"
))


cursor.execute("""
INSERT INTO projects (id, name, type, path, port)
VALUES (?, ?, ?, ?, ?)
""", (
    "two-column-dynamic",
    "Two Column Dynamic",
    "live-server",
    "E:/resume-templates/templates/two-column-dynamic",
    5510
))

conn.commit()
conn.close()
print("✅ projects.db created.")
