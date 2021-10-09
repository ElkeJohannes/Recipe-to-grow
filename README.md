<div align="center">

![Recipe to Grow](static/img/responsive-mockup.png)

---

Recipe to grow is a website where users can share their favorite plant based recipes. Additionally, users can find links to products in my webshop (external site) for plants, that are appropriate to the recipe. 

**-- [See live site on Heroku](http://recipe-to-grow.herokuapp.com/) --**

</div>

---

## Table of contents

**<details><summary>User Experience</summary>**
  - [User stories](#user-stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
</details>

**<details><summary>Features</summary>**
  - [Existing features](#existing-features)
  - [Future features](#future-features)
</details>

**<details><summary>Technologies Used</summary>**
  - [Languages](#languages)
  - [Libraries, Frameworks and programs](#Libraries,-Frameworks-and-programs)
</details>

**<details><summary>Testing</summary>**
  - [Test documentation](#)
</details>

**<details><summary>Deployment</summary>**
  - [Deployment to GitHub pages](#deployment-to-github-pages)
  - [Forking this repository](#forking-this-repository)
  - [Local deployment](#local-deployment)
</details>

**<details><summary>Credits</summary>**
  - [Text](#text)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
</details>

---

## &rarr; **User Experience**

### **<ins>User stories</ins>**
As a non-contributing visitor to the site I want to:
  - view all available recipes
  - view the most popular recipes
  - view the most recently added recipes

As a contributing visitor to the site I want to:
  - add a recipe to the site
  - edit my own recipes
  - delete my recipes


### **<ins>Strategy</ins>**
The main purpose of the site is the sharing of plant-based recipes. The functionality to do so will be featured front and center to make it as easy as possible. Additionally the site will serve as a window, where plants the site owner sells on another website can be displayed. 

### **<ins>Scope</ins>**
The site will be feature adding, viewing, updating and deleting of own recipes. Additionally users will be able to register and login. Plants for sale will be featured alongside the recipes.

### **<ins>Structure</ins>**
 The main page will feature a button to immediatly take the visitor to all recipes. The menu will change depending on the logged-in status. The menu will be a hamburger meu on all sizes, and feature a drop down menu. The 'add recipe' and the 'edit recipe' pages are only accesible from the 'my recipes' page, all other pages are navigatable through the hamburger menu.

### **<ins>Skeleton</ins>**
The following wireframes were made using Balsamiq to give a rough idea of the project.
- [Home page](wireframes/home.png)
- [All recipes](wireframes/all_recipes.png)
- [Single recipe](wireframes/single_recipe.png)
- [Login](wireframes/login.png)
- [Register](wireframes/register.png)
- [Add recipe](wireframes/add_new_recipe.png)


### **<ins>Surface</ins>**
The page is designed around basic colours, mainly in the green spectrum. This is to emphasize the plant based nature of the site. 

---

## &rarr; **Features**

#### **<ins>Existing features</ins>**
|#|Name|Description|
|-|-|-|
|1|Add recipe|Users can add recipes when logged in|
|2|Edit recipe|Users can edit their own recipes when logged in|
|3|Delete recipe|Users can delete their own recipes when logged in|
|4|View recipe|View an individual recipe|
|5|Overview|See all recipes on the site|
|6|Search|Search through all recipes on the site|
|7|Register|Register for an account to contribute to the site|


#### **<ins>Future features</ins>**
|#|Name|Description|
|-|-|-|
|1|Social links|Allows sharing of a recipe on social media platforms|
|2|More profile content|More profile content features like an avatar and the option to change password.|
|3|Favorites|Mark a recipe as a favorite to save it to your profile|
|4|Categories|Recipes are put into categories for easier searching|


---

## &rarr; **Technologies Used**
### **<ins>Languages</ins>**

| <div align="center">HTML5</div> | <div align="center">CSS3</div> | <div align="center">Javascript</div> | <div align="center">Python</div> |
|-|-|-|-|
| ![html5](assets/images/html5.png) | ![css3](assets/images/css3.png) | ![javascript](assets/images/javascript.png) | ![python](assets/images/python.png) |


### **<ins>Libraries, Frameworks and programs</ins>**
- [JQuery 3.5.1](https://jquery.com/)
  * Used throughout the game.js file for easier DOM access.
- [Bootstrap 5.1.0](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
  * Used widely troughout the site to speed up layout design.
- [Multi device mockup generator](http://techsini.com/multi-mockup/index.php)
  * Used to create the header image of this readme file.
- [Favicon generator](https://favicon.io/favicon-generator/)
  * Used to create a custom favicon.
---

## &rarr; **Deployment** 
### **<ins>Deployment to GitHub pages</ins>**


### **<ins>Forking this repository</ins>**


### **<ins>Local deployment</ins>**


---

## &rarr; **Credits**

### **<ins>Text</ins>**
- Vegan map recipe taken from: [NY Times](https://cooking.nytimes.com/recipes/1017358-vegan-mapo-tofu)
- 

### **<ins>Media</ins>**


### **<ins>Acknowledgements</ins>** 
- Info taken from: [Flask documentation website](https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/) on how to do file uploads.
- [This stack overflow question](https://stackoverflow.com/questions/47083403/extracting-input-from-all-input-boxes-into-a-list-using-flask) on how to handle multiple input boxes into an array.