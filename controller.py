# controller.py
import os
import subprocess
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, jsonify
import webbrowser
import platform

app = Flask(__name__)


def load_projects():
    conn = sqlite3.connect("projects.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    return cursor.fetchall()

projects = load_projects()
running_processes = {}  # { project_id: subprocess.Popen }

@app.route("/")
def index():
    return render_template("index.html", projects=projects)

@app.route("/start/<project_id>", methods=["POST"])
def start_project(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404

    if project_id in running_processes:
        return "Already running", 400

    command = []
    env = os.environ.copy()

    if project["type"] == "live-server":
        command = ["npx", "live-server", project["path"], f"--port={project['port']}"]
    elif project["type"] == "flask":
        command = ["python", project.get("entry", "app.py")]
    elif project["type"] == "node":
        command = ["node", project["entry"]]
    else:
        return "Unknown project type", 400

    process = subprocess.Popen(command, cwd=project["path"], env=env, shell=True)
    running_processes[project_id] = process
    return redirect(url_for("index"))

@app.route("/stop/<project_id>")
def stop_project(project_id):
    process = running_processes.get(project_id)
    if process:
        process.terminate()
        process.wait()
        del running_processes[project_id]
        return redirect(url_for("index"))
    return "Project not running", 400

@app.route("/restart/<project_id>")
def restart_project(project_id):
    stop_project(project_id)
    return start_project(project_id)

@app.route("/status")
def status():
    statuses = {}
    for project in projects:
        statuses[project["id"]] = project["id"] in running_processes
    return jsonify(statuses)

@app.route("/open-folder/<project_id>")
def open_folder(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404

    path = project["path"]
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

    return redirect(url_for("index"))

@app.route("/logs/<project_id>")
def logs(project_id):
    return f"Logs not implemented yet for project: {project_id}"  # placeholder

@app.route("/kill-all", methods=["POST"])
def kill_all():
    for project_id, process in list(running_processes.items()):
        process.terminate()
        process.wait()
        del running_processes[project_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)