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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        USERNAME = request.form.get("username").lower()
        PASSWORD = request.form.get("password")
        # check if username exists in db
        existing_user = mongo.db.Users.find_one({"username": USERNAME})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], PASSWORD):
                session["user"] = USERNAME
                flash("Welcome, {}".format(USERNAME))
            else:
                # invalid password match
                flash("Incorrect Username and\or Password")
                return redirect(url_for("login"))

        else: 
            # username doesn't exist
            flash("Incorrect Username and\or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
