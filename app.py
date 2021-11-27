import os
from flask import (
     Flask, flash, render_template, redirect,
     request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
from classes import RegisterForm, LoginForm, ReviewForm

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
@app.route("/get_books")
def get_books():
    books = mongo.db.books.find()
    categories = mongo.db.categories.find()
    return render_template("home.html", books=books, categories=categories)


@app.route("/login", methods=["GET", "POST"])   
def login():
    login_form = LoginForm(request.form)

    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username" : login_form.username.data.lower()})

        if existing_user:
            # Check hashed password matches user input
            if check_password_hash(
                existing_user["password"], login_form.password.data):
                    session["user"] = login_form.username.data.lower()
                    flash(f"Welcome {login_form.username.data}")
                    return redirect(url_for('profile', username=session["user"]))
            else:
                # invalid password match
                flash(f"Incorrect Username and/or Password")
                return redirect(url_for("login"))
        
        else:
            #username does not exist
            flash(f"Incorrect Username and/or Password")
            redirect(url_for("login"))

    return render_template("login.html", login_form=login_form)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True )    