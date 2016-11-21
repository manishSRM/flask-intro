from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# import sqlite3

app = Flask(__name__)

# config
app.config.from_object('config.DevelopmentConfig')


# create the SQLAlchemy object
db = SQLAlchemy(app)
from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    # return "Hello World!!"
    posts = db.session.query(BlogPost).all()
    return render_template("template.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != "admin":
            error = "Wrong admin!"
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash("You are just logged in!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You are just logged out!")
    return redirect(url_for('welcome'))


# def connect_db():
#     return sqlite3.connect('posts.db')



if __name__ == "__main__":
    app.run(debug=True)




