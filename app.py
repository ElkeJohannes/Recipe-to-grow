import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def home():
    recipes = list(mongo.db.Recipes.find())
    return render_template('home.html', recipes = recipes)


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.Recipes.find())
    return render_template('recipes.html', recipes = recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        USERNAME = request.form.get("username").lower()
        
        # check if username is already in use in db
        existing_user = mongo.db.Users.find_one(
            {"username": USERNAME})

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        register = {
            "Firstname": request.form.get('firstname'),
            "Lastname": request.form.get('lastname'),            
            "Username": USERNAME,
            "Password": generate_password_hash(request.form.get("password")),
            "IsAdmin": False
        }
        mongo.db.Users.insert_one(register)

        # put the new user into session cookie
        session["user"] = USERNAME
        flash("Registration succesful!")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        USERNAME = request.form.get("username").lower()
        PASSWORD = request.form.get("password")
        # check if username exists in db
        existing_user = mongo.db.Users.find_one({"Username": USERNAME})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["Password"], PASSWORD):
                session["user"] = USERNAME
                
                flash("Welcome {} {}".format(existing_user['Firstname'], existing_user['Lastname']))
            else:
                # invalid password match
                flash("Incorrect Username and\or Password")
                return redirect(url_for("login"))

        else: 
            # username doesn't exist
            flash("Incorrect Username and\or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove the 'user' session cookie
    session.pop('user')
    flash("You have been logged out.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
