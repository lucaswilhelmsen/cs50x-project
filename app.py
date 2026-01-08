from flask import Flask, request, session, render_template, redirect
from sqlalchemy import create_engine
import os 

templates = os.path.dirname(__file__)

app = Flask(__name__,
template_folder=docs)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first_project")
def first_project():
    if request.method == "GET":
        result = engine.execute("SELECT * FROM projects")
        return render_template("first_project.html", projects=result)


@app.route("/writing")
def writing():
    return render_template("writing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

