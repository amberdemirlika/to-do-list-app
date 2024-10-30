from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/tasks.json")
def index():
    return db.tasks_all()

@app.route("/tasks.json", methods=["POST"])
def create():
    category= request.form.get("category")
    date = request.form.get("date")
    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")
    return db.tasks_create(category, date, title, description , status)