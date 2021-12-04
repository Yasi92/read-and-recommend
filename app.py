import os
from typing import Set
from flask import (
     Flask, flash, render_template, redirect,
     request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
import wtforms 

from classes import RegisterForm, LoginForm, ReviewForm, EditProfile, AddBook

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
    best_sellers = mongo.db.books.find({"best_seller" : True})
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
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    profile_pic = url_for('static',filename='images/images.jpeg') 

    # Gets the books added by user.
    books= mongo.db.books.find({"added_by" : session['user']})

    # This gets the length of the books added by user.
    books_length = books.count()
    num = []
    i = 0
    for i in range(books_length):
        i = i + 1
        num.append(i)
    

    if session["user"]:
        return render_template("profile.html", username=username, user=user,
                                 profile_pic=profile_pic, books=zip(books, num))

    return redirect(url_for("login"))





@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])   
def edit_profile(user_id):
    user = mongo.db.users.find_one({"_id" : ObjectId(user_id)})
    edit_form = EditProfile(request.form)
    profile_pic = url_for('static',filename='images/images.jpeg') 

    if request.method == "POST" and edit_form.validate():
        # Since password is not getting updated in db, "$set" is used to update the specific records.
        mongo.db.users.update(
                            {"_id" : ObjectId(user_id)}, {'$set': {"username" : edit_form.username.data,
                             "email" : edit_form.email.data, "location": edit_form.location.data}} )
        flash("Profile Updated")
        session["user"] = edit_form.username.data.lower()
        return redirect(url_for('profile', username=session['user']))

        

    return render_template('edit_profile.html', edit_form=edit_form,
                            user=user, profile_pic=profile_pic )



@app.route("/get_book/<book_title>", methods=["GET", "POST"])
def get_book(book_title):
    book_details = mongo.db.books.find_one({"title" : book_title})    
    

    review_form = ReviewForm(request.form)

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
                            book_details=book_details, review_form=review_form)    




@app.route("/get_categories/<category_name>")
def get_categories(category_name):
    categories = mongo.db.categories.find()
    category_book = mongo.db.books.find({"category_name" : category_name})

    return render_template("home.html", categories=categories,
    category_name= category_name, category_book= category_book)



@app.route("/logout")
def logout():
    #removes user from session cookies
    flash("You have been loged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    add_book_form = AddBook(request.form)

    if request.method == "POST":
        # This gets the value(not key) of the select field and insert it to db.
        # The trick has been learned from (https://stackoverflow.com/questions/43071278/how-to-get-value-not-key-data-from-selectfield-in-wtforms/43071533)
        value = dict(add_book_form.category.choices).get(add_book_form.category.data)

        new_book = {
            "title" : add_book_form.title.data,
            "author" : add_book_form.author.data,
            "category_name" : value,
            "publisher" :add_book_form.publisher.data,
            "pages" : add_book_form.pages.data,
            "shopping_link" : add_book_form.shopping_link.data,
            "img_url" : add_book_form.image.data,
            "description" :add_book_form.desc.data,
            "best_seller" : add_book_form.best_seller.data,
            "price" : add_book_form.price.data,
            "added_by" : session['user']
        }

        mongo.db.books.insert_one(new_book)
        flash("Book Added")
        return redirect(url_for('get_book', book_title=add_book_form.title.data))

    return render_template("add_book.html", add_book_form=add_book_form)



@app.route("/edit_book/<book_id>", methods=["POST", "GET"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id" : ObjectId(book_id)})
    categories = mongo.db.categories.find()

    edit_book_form = AddBook(request.form)
   
    if request.method == "POST":
       

        new_book = {
            "title" : edit_book_form.title.data,
            "author" : edit_book_form.author.data,
            "category_name" : request.form.get("category_name"),
            "publisher" :edit_book_form.publisher.data,
            "pages" : edit_book_form.pages.data,
            "shopping_link" : edit_book_form.shopping_link.data,
            "img_url" : edit_book_form.image.data,
            "description" :request.form.get("desc"),
            "best_seller" : edit_book_form.best_seller.data,
            "price" : edit_book_form.price.data,
            "added_by" : session['user']
        }

        mongo.db.books.update_one({"_id" : ObjectId(book_id)}, {'$set' : new_book})
        flash("Book Edited")
        return redirect(url_for('get_book', book_title=edit_book_form.title.data))

    return render_template("edit_book.html", book=book, edit_book_form=edit_book_form, categories=categories)


# def edit():
#     mongo.db.books.update_many({}, {'$unset' : {"language" : 1, "added" : 1}})


# edit()    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True )    