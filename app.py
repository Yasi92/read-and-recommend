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

@app.route("/best_seller_books")
def best_seller_books():
    
    categories = mongo.db.categories.find()
    best_sellers = mongo.db.books.find({"best_seller" : "true"})
    return render_template("home.html", best_sellers=best_sellers,
    categories=categories)
    

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



@app.route("/register", methods=["GET", "POST"])   
def register():
    register_form = RegisterForm(request.form)

    if request.method == "POST" and register_form.validate():
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username" : register_form.username.data.lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for('register'))

    
        register={
            "username" : register_form.username.data,
            "password" : generate_password_hash(str(register_form.password.data)),
            "email" : register_form.email.data,
            "location" : register_form.location.data
        }    

        mongo.db.users.insert_one(register)
        

        session["user"] = register_form.username.data.lower()
        flash("Registeration Successful!")
        return redirect(url_for('profile', username=session["user"]))

    
    return render_template("register.html", register_form=register_form) 

@app.route("/profile/<username>", methods=["GET", "POST"])   
def profile(username):
    # get the session user's username from db
    username= mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    location = mongo.db.users.find_one(
        {"username" : username})["location"] 
    email = mongo.db.users.find_one(
        {"username" : username})["email"]
    profile_pic = url_for('static',filename='images/images.jpeg') 
    
    if session["user"]:
        return render_template("profile.html", username=username,
        location=location, email=email, profile_pic=profile_pic)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #removes user from session cookies
    flash("You have been loged out")
    session.pop("user")
    return redirect(url_for('login'))






@app.route("/get_book/<book_title>", methods=["GET", "POST"])
def get_book(book_title):
    book_details = mongo.db.books.find_one({"title" : book_title})    
    

    review_form = ReviewForm(request.form)
    # it selects all the best seller books with a value of true and return a best_seller badge 
    badge= False
    
    if book_details["best_seller"] == "true":
        badge = True 



    if request.method == "POST":

        if session:
            review_details={
            "username" : session["user"],
            "review" : review_form.review.data,
            "date_created" : review_form.created_date,
            "book_title" : book_title}
            
            mongo.db.reviews.insert_one(review_details)
            flash("Thank you for your feedback!")

        else:
            pass
            flash("Please login to write a review!")



    return render_template("books.html", book_title=book_title,
                            book_details=book_details, review_form=review_form,
                            badge=badge)    




@app.route("/get_categories/<category_name>")
def get_categories(category_name):
    categories = mongo.db.categories.find()
    category_book = mongo.db.books.find({"category_name" : category_name})

    return render_template("home.html", categories=categories,
    category_name= category_name, category_book= category_book)








if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True )    