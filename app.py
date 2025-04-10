from flask import Flask, render_template, request, redirect, url_for

import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename
import pytz

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # Max 5 MB
bugsDirectory = "bugs"

from flask import send_from_directory

@app.route("/uploads/<filename>")
def uploadedFile(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if not os.path.exists(bugsDirectory):
    os.makedirs(bugsDirectory)
    
def get_bug_path(bug_id):
    return os.path.join(bugsDirectory, f"bug-{bug_id}.json")

def load_bug(bug_id):
    path = get_bug_path(bug_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def save_bug(bug_id, data):
    path = get_bug_path(bug_id)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/bug/view/<int:bug_id>")
def viewBug(bug_id):
    bug = load_bug(bug_id)
    if not bug:
        return "Bug not found", 404
    return render_template("viewBug.html", bug=bug)

        
@app.route("/")
def index():
    bugs = []
    for file in os.listdir(bugsDirectory):
        with open(os.path.join(bugsDirectory, file)) as f:
            bugs.append(json.load(f))
    return render_template("index.html", bugs=bugs)

@app.route("/reportBug", methods=["GET", "POST"])
def reportBug():
    if request.method == "POST":
        bugId = len(os.listdir(bugsDirectory))
        createdBy = "Lorenz"

        attachment = request.files.get("attachment")
        filename = None

        if attachment and attachment.filename != "":
            filename = f"bug-{bugId}_" + secure_filename(attachment.filename)
            attachment.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        bugData = {
            "ID": bugId,
            "Title": request.form["title"],
            "Description": request.form["description"],
            "File Name": request.form["fileName"],
            "Priority": request.form["priority"],
            "Bug Type": request.form["bugType"],
            "GitHub PR/Commit": request.form.get("githubLink", ""),
            "Attachment": filename,
            "Status": "Open",
            "Last Updated": datetime.now(pytz.timezone('US/Pacific')).isoformat(),
            "Created By": createdBy
        }

        save_bug(bugId, bugData)
        return redirect(url_for("index"))

    return render_template("reportBug.html")

@app.route("/bug/<int:bug_id>", methods=["GET", "POST"])
def updateBug(bug_id):
    bug = load_bug(bug_id)
    if not bug:
        return "Bug not found", 404

    if request.method == "POST":
        new_status = request.form["status"]
        bug["Status"] = new_status
        bug["Last Updated"] = datetime.now(pytz.timezone('US/Pacific')).isoformat()
        save_bug(bug_id, bug)
        return redirect(url_for("index"))

    return render_template("updateBug.html", bug=bug)

if __name__ == "__main__":
    app.run(debug=True)