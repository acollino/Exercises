from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/story")
def show_story():
    return render_template("story.html")
