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

# Define the constants needed for the recipe image uploads
UPLOAD_FOLDER = 'static/img/recipes/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

# Configure our app to run with the needed environment variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mongo = PyMongo(app)


def allowed_file(filename):
    # Checks if a filename is of an allowed file type
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    # Gets most recent recipes and most popular recipes 
    # Passes it through to be used for the carousels
    mostPopularRecipes = list(mongo.db.Recipes.find().limit(5).sort("TimesViewed",-1))
    mostRecentRecipes = list(mongo.db.Recipes.find().limit(5))
    return render_template('home.html', mostPopularRecipes=mostPopularRecipes,
                           mostRecentRecipes=mostRecentRecipes)


@app.route("/recipes")
def recipes():
    # Gets all recipes and renders the recipes page
    recipes = list(mongo.db.Recipes.find())
    return render_template('recipes.html', recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    # Either show the registration form or perform the registration
    if request.method == "POST":
        USERNAME = request.form.get("username").lower()

        # Check if username is already in use in db
        existing_user = mongo.db.Users.find_one(
            {"username": USERNAME})
        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))
        register = {
            # Get the form values
            "Firstname": request.form.get('firstname'),
            "Lastname": request.form.get('lastname'),
            "Username": USERNAME,
            "Password": generate_password_hash(request.form.get("password")),
            "IsAdmin": False
        }
        mongo.db.Users.insert_one(register)

        # Put the new user into session cookie
        session["user"] = USERNAME
        flash("Registration succesful!")
        return redirect(url_for("myRecipes"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        USERNAME = request.form.get("username").lower()
        PASSWORD = request.form.get("password")
        # Check if username exists in db
        existing_user = mongo.db.Users.find_one({"Username": USERNAME})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(existing_user["Password"], PASSWORD):
                # Put the new user into session cookie
                session["user"] = USERNAME
                flash("Welcome {} {}".format(existing_user['Firstname'],
                                             existing_user['Lastname']))
                return redirect(url_for("myRecipes"))
            else:
                # Invalid password match
                flash("Incorrect Username and\or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and\or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Remove the 'user' session cookie
    session.pop('user')
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/my_recipes")
def myRecipes():
    # Gets recipes owned by the logged in user
    recipes = list(mongo.db.Recipes.find({"Owner": session["user"]}))
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/view_recipe/<recipe_id>")
def viewRecipe(recipe_id):
    # Gets the recipe based on provided ID. Add sellable products,
    # by searching through the ingredients
    recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    products = []
    for ingredient in recipe["Ingredients"]:
        products += mongo.db.Products.find({"$text": {"$search": ingredient}})

    # Ups the counter for TimesViewed
    timesViewed = recipe["TimesViewed"] + 1
    recipe.update({"TimesViewed":timesViewed})
    mongo.db.Recipes.update({"_id": ObjectId(recipe["_id"])}, recipe)

    return render_template("view_recipe.html", recipe=recipe,
                           products=products)


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
        # Credit for below code snippet in README.md (flask.palletprojects.com)
        # Check if the post request has the file part
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


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def editRecipe(recipe_id):
    if request.method == "POST":
        recipeToEdit = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
        # Get the info from the form and add some additional info
        recipe = ({
            "Title": request.form.get("title"),
            "Description": request.form.get("description"),
            "TimesViewed": 0,
            "DateAdded": date.today().strftime("%d/%m/%Y"),
            "Owner": session["user"],
            "Ingredients": request.form.getlist('ingredients[]'),
            "CookingSteps": request.form.getlist('cookingSteps[]'),
            "TipsTricks": request.form.getlist('tipsTricks[]'),
            "Image": recipeToEdit["Image"]
        })

        # Handle the upload of the recipe image
        # Credit for below code snippet in README.md (flask.palletprojects.com)
        # If there's a new file, upload it, else just keep the original
        file = request.files['recipeImage']
        if file.filename != '' and allowed_file(file.filename):
            filename = session['user'] + "_" + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recipe.update({
                "Image": filename
            })

        mongo.db.Recipes.update({"_id": ObjectId(recipe_id)}, recipe)
        flash("Recipe saved!")
        return redirect(url_for("myRecipes"))

    recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def deleteRecipe(recipe_id):
    # Delete the recipe specified by the provided ID
    mongo.db.Recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("myRecipes"))


@app.route("/search", methods=["GET", "POST"])
def search():
    # Text based search on Recipes document
    query = request.form.get("query")
    recipes = list(mongo.db.Recipes.find({"$text": {"$search": query}}))
    return render_template('recipes.html', recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
