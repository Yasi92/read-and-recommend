from flask import (
     Flask, flash, render_template, redirect,
     request, session, url_for)
from datetime import timedelta, datetime  
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from classes import RegisterForm, LoginForm, ReviewForm, EditProfile, AddBook
import os
import flask
import timeago, datetime


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# The timeago method has been learned from (https://stackoverflow.com/questions/60162353/how-to-use-python-module-timeago-with-flask)
@app.template_filter('timeago')
def fromnow(date):
    '''
    Return passed time as arg to a format of timeago
    '''
    return timeago.format(date, datetime.datetime.now())


now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)


@app.route("/")
@app.route("/get_books")
def get_books():
    '''
    Gets all the books from db to display on the home page
    '''
    books = mongo.db.books.find()
    books_length = mongo.db.books.count_documents({})
    categories = list(mongo.db.categories.find())

    return render_template("home.html", books=books,
                            categories=categories, books_length=books_length)


@app.route("/search", methods=["GET", "POST"])
def search():
    '''
    It filters the queries based on the title or author name.
    '''
    query= request.form.get("query")
    books = mongo.db.books.find({"$text" : {"$search" : query}})
    books_length = mongo.db.books.count_documents({"$text" : {"$search" : query}})
    categories = mongo.db.categories.find()

    return render_template("home.html", books=books,
                             categories=categories, books_length=books_length)



@app.route("/best_seller_books")
def best_seller_books():
    '''
    Gets the best seller books from db.
    '''
    categories = list(mongo.db.categories.find())
    best_sellers = mongo.db.books.find({"best_seller" : True})
    books_length = mongo.db.books.count_documents({"best_seller" : True})

    return render_template("home.html", best_sellers=best_sellers,
    categories=categories, books_length=books_length)



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
                    # Logs out the user after a day automatically
                    app.permanent_session_lifetime = timedelta(days=1)
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

    # Passing RegisterForm class to the request form
    register_form = RegisterForm(request.form)

    if request.method == "POST" and register_form.validate():
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username" : register_form.username.data.lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for('register'))

        register={
            "username" : register_form.username.data.lower(),
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
    user = mongo.db.users.find_one({"username": username})       

    # Gets the books added by user.
    books= mongo.db.books.find({"added_by" : user["username"]})

    # Gets the reviews added by user.
    reviews = mongo.db.reviews.find({"username": user["username"]})
    reviews_length = mongo.db.reviews.count_documents(
                                {"username": user["username"]})

    # This gets the length of the books added by user.
    books_length = mongo.db.books.count_documents({"added_by" : user["username"]})
    num = []
    i = 0
    for i in range(books_length):
        i = i + 1
        num.append(i)
    

    if session["user"]:
        return render_template("profile.html",user=user, books=zip(books, num),
                                 books_length=books_length, reviews=reviews,
                                 reviews_length=reviews_length)

    return redirect(url_for("login"))


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])   
def edit_profile(user_id):
    '''
    Edits user's profile
    '''
    user = mongo.db.users.find_one({"_id" : ObjectId(user_id)})
    # Passing EditProfile class to the request form
    edit_form = EditProfile(request.form)
         
    if request.method == "POST" and edit_form.validate():

        # Checks whether data has been changed or not
        no_change = (edit_form.location.data == user["location"] and
                     edit_form.email.data == user["email"] and 
                     edit_form.username.data.lower() == user["username"])

        # Checks if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username" : edit_form.username.data.lower()})   

        # returns to profile if data is not changed
        if no_change:
            return redirect(url_for("profile", username=user["username"]))


        # Checks if the username is not being considered to be updated to an already existing username
        # Since password is not getting updated in db, "$set" is used to update the specific records.  
        elif user["username"] == edit_form.username.data.lower():
            mongo.db.users.update(
                            {"_id" : ObjectId(user_id)},
                            {'$set': {"username" : edit_form.username.data.lower(),
                            "email" : edit_form.email.data,
                            "location": edit_form.location.data}})

            # updates the username in books collection added by the user
            mongo.db.books.update_many({"added_by" : user["username"]},
                                         {'$set' : {"added_by" : edit_form.username.data.lower()}})

            # updates the username in reviews collection added by the user
            mongo.db.reviews.update_many({"username" : user['username']},
                                         {'$set' : {"username" : edit_form.username.data.lower()}}) 

            session["user"] = edit_form.username.data.lower()  
            flash("Profile Updated")
            return redirect(url_for('profile', username=session['user']))


        # clears the form if username exits in db 
        elif existing_user and existing_user["username"] == edit_form.username.data.lower():
            flash(f'Username "{edit_form.username.data}" already exists.')
            return redirect(url_for("edit_profile", user_id=user["_id"]))


        else:
            mongo.db.users.update(
                            {"_id" : ObjectId(user_id)},
                            {'$set': {"username" : edit_form.username.data.lower(),
                            "email" : edit_form.email.data,
                            "location": edit_form.location.data}})

            # updates the username in books collection added by the user
            mongo.db.books.update_many({"added_by" : user["username"]},
                                         {'$set' : {"added_by" : edit_form.username.data.lower()}})

            # updates the username in reviews collection added by the user
            mongo.db.reviews.update_many({"username" : user['username']},
                                         {'$set' : {"username" : edit_form.username.data.lower()}}) 

            session["user"] = edit_form.username.data.lower()  
            flash("Profile Updated")
            return redirect(url_for('profile', username=session['user']))


    return render_template('edit_profile.html', 
                        edit_form=edit_form,
                        user=user)


@app.route("/get_book/<book_id>", methods=["GET", "POST"])
def get_book(book_id):
    '''
    Gets book details 
    '''
    book_details = mongo.db.books.find_one({"_id": ObjectId(book_id)})  

    # Passing ReviewForm class to the request form
    review_form = ReviewForm(request.form)

    if request.method == "POST":
        # Checks if there is session to insert the review
        if session:
            review_details={
            "username" : session["user"],
            "review" : review_form.review.data,
            "date_created" : datetime.datetime.now(),
            "book_title" : book_details["title"]
            }
            
            mongo.db.reviews.insert_one(review_details)
            flash("Thank you for your feedback!")
            return redirect(url_for("get_book", book_id=book_id))

        # Returns users to login page if there is no session to login first.
        else:
            flash("Please login to write a review!")
            return redirect(url_for("login"))

    # Gets all the reviews of the book
    reviews = mongo.db.reviews.find({"book_title" : book_details["title"]})
    reviews_length = mongo.db.reviews.count_documents(
                                    {"book_title" : book_details["title"]})

    return render_template("books.html",book_details=book_details,
                            review_form=review_form,
                            reviews=reviews, reviews_length=reviews_length)    


@app.route("/get_books/get_categories/<category_name>")
def get_categories(category_name):
    '''
    Filters books based on their category.
    '''
    categories = list(mongo.db.categories.find())

    category_book = mongo.db.books.find({"category_name" : category_name})
    books_length = mongo.db.books.count_documents({"category_name" : category_name})

    return render_template("home.html", categories=categories,
                        category_name= category_name,
                        category_book=category_book ,
                        books_length=books_length)



@app.route("/logout")
def logout():
    #removes user from session cookies
    flash("You have been loged out")
    session.pop("user")

    return redirect(url_for('login'))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    '''
    Add books to db by user
    '''
    # Passing AddBook class to the request form
    add_book_form = AddBook(request.form)

    if request.method == "POST":
        # Checks if the book exists in db
        existing_book = mongo.db.books.find_one(
                                {"title" : add_book_form.title.data.lower()})

        if existing_book:
            flash("The Book Title Exists In Our Collection")
            return redirect(url_for("add_book"))
            
        elif session["user"]:
            # This gets the value(not key) of the select field and insert it to db.
            ''' The trick has been learned from 
            (https://stackoverflow.com/questions/43071278/how-to-get-value-not-key-data-from-selectfield-in-wtforms/43071533)'''
            value = dict(add_book_form.category.choices).get(add_book_form.category.data)

            new_book = {
                "title" : add_book_form.title.data.lower(),
                "author" : add_book_form.author.data.lower(),
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
            return redirect(url_for('get_book', book_id=new_book['_id']))

    return render_template("add_book.html", add_book_form=add_book_form)


@app.route("/edit_book/<book_id>", methods=["POST", "GET"])
def edit_book(book_id):
    '''
    Edits the book added by the user.
    '''
    book = mongo.db.books.find_one({"_id" : ObjectId(book_id)})
    categories = mongo.db.categories.find()

    # Passing AddBook class to the request form
    edit_book_form = AddBook(request.form)
   
    if request.method == "POST":
        # Checks if the book title already exists in db.
        existing_book = mongo.db.books.find_one(
                {"title" : edit_book_form.title.data.lower()})
          

        # If the title is not being updated but the other fields are, it updates the other fields.
        if book["title"] == edit_book_form.title.data.lower():
            new_book = {
                "title" : edit_book_form.title.data.lower(),
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
            return redirect(url_for('get_book', book_id=book["_id"]))



        # If the title is being updated to an exsisting title in db
        elif existing_book and existing_book["title"] == edit_book_form.title.data.lower():
            flash("Book title already exists.")
            return redirect(url_for('edit_book', book_id=book["_id"]))


        else:
            new_book = {
                "title" : edit_book_form.title.data.lower(),
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
            return redirect(url_for('get_book', book_id=book["_id"]))




    return render_template("edit_book.html", book=book,
                        edit_book_form=edit_book_form,
                        categories=categories)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    '''
    Deletes books added by the user from db.
    '''
    mongo.db.books.delete_one({"_id" : ObjectId(book_id)})
    flash("Book Successfuly Deleted")
    return redirect(url_for("profile", username=session['user']))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    '''
    Deletes reviews added by user from db.
    '''
    mongo.db.reviews.delete_one({"_id" : ObjectId(review_id)})
    flash("Review Successfuly Deleted")
    return redirect(url_for("profile", username=session['user'])) 
      

# The custome 404 page has been learned from my mentor "Richard Wills"
@app.errorhandler(404)
def page_not_found(e):
    """
    On 404 error passes user to custom 404 page
    """
    return render_template('404.html'), 404


# The custome 500 page has been learned from my mentor "Richard Wills"
@app.errorhandler(500)
def internal_error(err):
    """
    On 500 error passes user to custom 500 page
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)    