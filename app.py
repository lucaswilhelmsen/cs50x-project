from flask import Flask, request, session, render_template, redirect
import flask_sqlalchemy
import os 

templates = os.path.dirname(__file__)

app = Flask(__name__,
template_folder=docs)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/writing")
def writing():
    return render_template("writing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")
