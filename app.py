from datetime import date
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import render_template

if os.path.exists("env.py"):
    import env

UPLOAD_FOLDER = 'static/img/recipes/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mongo = PyMongo(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
                # put the new user into session cookie
                session["user"] = USERNAME
                flash("Welcome {} {}".format(existing_user['Firstname'], existing_user['Lastname']))
                return redirect(url_for("myRecipes"))                
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


@app.route("/my_recipes")
def myRecipes():
    recipes = list(mongo.db.Recipes.find({"Owner": session["user"]}))
    return render_template("my_recipes.html", recipes = recipes)


@app.route("/view_recipe/<recipe_id>")
def viewRecipe(recipe_id):
    recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe = recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def addRecipe():
    if request.method == "POST":
        # Get the info from the form and add some additional info
        recipe = ({
            "Title": request.form.get("title"),
            "Description": request.form.get("description"),
            "TimesViewed": 0,
            "DateAdded": date.today().strftime("%d/%m/%Y"),
            "Owner": session["user"],
            "Ingredients": request.form.getlist('ingredients[]'),
            "CookingSteps": request.form.getlist('cookingSteps[]'),
            "TipsTricks": request.form.getlist('tipsTricks[]')
        })

        # Handle the upload of the recipe image
        # Credit for the code in README.md (flask.palletprojects.com)
        # check if the post request has the file part
        if 'recipeImage' not in request.files:
            flash('No valid file found')
            return redirect(request.url)
        file = request.files['recipeImage']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = session['user'] + "_" + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recipe.update({
                "Image": filename
            })

        mongo.db.Recipes.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("myRecipes"))

    return render_template("add_recipe.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
