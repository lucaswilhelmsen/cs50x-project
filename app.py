from flask import Flask, request, session, render_template, redirect
from sqlalchemy import create_engine
import os 

templates = os.path.dirname(__file__)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    result = engine.execute("SELECT * FROM projects")
    return render_template("projects.html", projects=result)


@app.route("/writing")
def writing():
    return render_template("writing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

