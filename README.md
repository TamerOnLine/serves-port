# 🛠️ Project Control Dashboard

## 🎯 Purpose
A dynamic web-based dashboard to manage and control multiple projects (Live Server, Flask, Node.js) via dedicated ports — all from a single unified interface on Windows.

<p align="center">
  <a href="screenshots/Screenshot.png">
    <img src="screenshots/Screenshot.png" alt="Quick clone of the indexMD repository" width="600"/>
  </a>
</p>

<p align="center">
  <img src="https://img.icons8.com/emoji/48/movie-camera.png" width="24" alt="Video Icon"/>
  <strong>Quick Clone of the <code>indexMD</code> repository in action</strong>
</p>

<br>

---

## ✅ Main Features

| Feature | Description |
|--------|-------------|
| 🔘 Start | Launch the selected project on its assigned port |
| ⏹️ Stop | Stop the running project |
| 🔄 Restart | Restart a project in one click |
| 🌐 Open | Open the running project in your browser |
| 📂 Open Folder | Open the project folder in File Explorer |
| 🔍 Logs (WIP) | View project logs (coming soon) |
| 🟢/🔴 Status | Real-time status updates per project |
| 🚫 Kill All | Stop all running projects instantly |

## 🗃️ Database (SQLite)

Database file: `projects.db`  
Table: `projects`

```sql
CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,  -- live-server / flask / node
    path TEXT NOT NULL,
    port INTEGER NOT NULL,
    entry TEXT
);
```

## 🧩 Key Files

### controller.py
- Backend logic built with Flask.
- Loads project definitions from SQLite database.
- Manages subprocesses for each project.

### templates/index.html
- Frontend interface.
- Provides action buttons for every project.
- Automatically updates project statuses every 3 seconds.

## ⚙️ How to Run

1. Install requirements:
   ```bash
   pip install flask
   ```

2. Initialize the database:
   ```bash
   python init_db.py
   ```

3. Launch the dashboard:
   ```bash
   python controller.py
   ```

Then open your browser at:
```
http://localhost:5000
```

## 📦 Supported Project Types

| Type | Description |
|------|-------------|
| `live-server` | HTML/CSS/JS project using `npx live-server` |
| `flask` | Python Flask project run using `python entry.py` |
| `node` | Node.js project run using `node entry.js` |

## 🔐 Future Enhancements

- Add user authentication (Flask-Login or custom login).
- Use PostgreSQL instead of SQLite for production.
- Integrated log viewer for subprocess output.

## 🛠️ Future Ideas

- ✅ Add new projects from the dashboard.
- ✅ Edit/delete projects from the interface.
- ✅ Support Docker containers for project isolation.
- ✅ Git integration to track project versions.
