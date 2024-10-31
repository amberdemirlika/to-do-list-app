from flask import Flask, request
from flask_cors import CORS
import db


app = Flask(__name__)
CORS(app)

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

@app.route("/tasks/<id>.json")
def show(id):
    return db.tasks_find_by_id(id)

@app.route("/tasks/<id>.json", methods=["PATCH"])
def update(id):
    category= request.form.get("category")
    date = request.form.get("date")
    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")
    return db.tasks_update_by_id(id, category, date, title, description , status)

@app.route("/tasks/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.tasks_destroy_by_id(id)