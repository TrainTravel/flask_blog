from flask import render_template, url_for

from blog import app
from blog.models import User, Post

posts = [
    {
        'author': 'Train',
        'title': 'Second post',
        'content': 'Keep going!',
        'date_posted': 'March 2, 2019'
    },
    {
        'author': 'Train',
        'title': 'First post',
        'content': 'Good Job!',
        'date_posted': 'March 1, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
