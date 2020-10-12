from flask import Flask, render_template, abort, request

from .posts import posts
from .models import ContactMe

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.htm", posts=posts)


@app.route("/about")
def about():
    return render_template("about.htm")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.htm")

   
    return render_template("contact.htm", thanks_for_message=True)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = None
    for saved_post in posts:
        if saved_post.id == post_id:
            post = saved_post

    if not post:
        abort(404)

    return render_template("post.htm", post=post)
