from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

story_example = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route("/")
def home_page():
    return render_template("index.html", story=story_example)


@app.route("/story")
def show_story():
    user_input = request.args
    generated_story = story_example.generate_multi(user_input)
    return render_template("story.html", story=generated_story)
