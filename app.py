from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/tasks.json")
def index():
    return db.tasks_all()