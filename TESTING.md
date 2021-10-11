
## <ins>**Testing**</ins>

---

**<details><summary>Table of contents</summary>**
  - [Code validation](#code-validation)
  - [User story tests](#user-story-tests)
  - [Manual testing script](#manual-testing-script)
  - [Feature test scripts](#feature-test-scripts)
  - [Bugs](#bugs)
</details>

---

## &rarr; **Code validation**
- Tested for valid HTML code using [w3 validator](https://validator.w3.org/nu/)<br>
<img src="static/img/html-validation.png" width="400px" height="270px" alt="Validation tests - HTML">

- Tested for valid CSS code using [Jigsaw validator](https://jigsaw.w3.org/css-validator/)<br>
<img src="static/img/css-validation.png" width="400px" height="150px" alt="Validation tests - CSS"><br>

- Tested for valid Javascript using [Jshint](https://jshint.com/)<br>
<img src="static/img/javascript-validation.png" width="500px" height="240px" alt="Validation tests - Javascript linter">

- Tested for PEP8 compliance using [pep8online](http://pep8online.com/)<br>
<img src="static/img/python-validation.png" width="500px" height="180px" alt="Validation tests - Python PEP8 validation">

---

## &rarr; **User story tests**
As a non-contributing visitor to the site I want to:
  - view all available recipes
    * When on the home page, you can click on the 'Browse recipes' button. This page is also accesible from the navigation menu.
  - view the most popular recipes
    * When on the home page, there is a carousel displaying the most popular recipes
  - view the most recently added recipes
    * When on the home page, there is a carousel displaying the most recently added recipes

As a contributing visitor to the site I want to:
  - add a recipe to the site
    * After logging in, there is an additional option available on the menu to add a recipe. The 'Add recipe' page is also accesible from the 'My recipes' page.
  - edit my own recipes
    * After logging in, you can edit your own recipes from the 'My recipes' page. To do so, you can click the edit icon behind the recipe name.
  - delete my recipes
    * After logging in, you can delete your own recipes from the 'My recipes' page. To do so, you can click the delete icon behind the recipe name.

---

## &rarr; **Manual testing script**
In all below testing actions, it is assumed you have opened the website on **any** device. 

|Test name|Actions|
|-|-|
|<ins>View highscores button</ins>|- Click on the 'View highscores' button <br>- Confirm a window opens, listing highscores|
|<ins>View highscores - Close button</ins>|- Click on the (X) button on the top right of this screen<br>- Confirm the highscores window closes|
|<ins>View highscores - Play again button</ins>|- Click on the 'View highscores' button <br>- Click on the 'Play again' button<br>- Confirm the highscores screen closes, and the game starts playing, highlighting 2 shapes|
|<ins>How to play button</ins>|- Click on the 'How to play' button<br>- Confirm the tutorial window opens, with a gif running|
|<ins>How to play - Close button</ins>|- Click on the (X) button on the top right of this screen<br>- Confirm the tutorial window closes|
|<ins>Play button</ins>|- Click on the play button<br>- Confirm the game starts running, and 2 shapes are highlighted|
|<ins>Sounds - Playing</ins>|- Click on the play button<br>- Confirm music is playing during the highlighting of the shapes<br>- Play through a number of additional rounds<br>- Confirm this music is always playing during the highlighting|
|<ins>Sounds - Correct</ins>|- Click on the play button<br>- Once possible, click on the correct shape<br>- Confirm a confirming sound is played|
|<ins>Sounds - Incorrect</ins>|- Click on the play button<br>- Once possible, click on one of the incorrect shapes<br>- Confirm a game over sound is played|
|<ins>Game results</ins>|- Click on the play button<br>- Once possible, click on on of the incorrect shapes<br>- Confirm the game results window appears|
|<ins>Game results - Close button</ins>|- Click on the play button<br>- Once possible, click on on of the incorrect shapes<br>- Once the Game results window appears, click on the (X) button on the top right of this screen<br>- Confirm the Game results windows closes|
|<ins>Game results - Submit highscore button</ins>|- Click on the play button<br>- Once possible, click on on of the incorrect shapes<br>- Once the Game results window appears, fill any name in and click on the 'Submit highscore' button<br>- Confirm you are taken to the Highscores window, and the name submitted appears|
|<ins>Footer link</ins>|- Click on the name 'Elke Harmanny' in the footer<br>- Confirm you are taken to the website: https://elkejohannes.github.io/online-resume/|

---

## &rarr; **Feature test scripts**
For testing, 2 device types are defined:
- Mobile
    * Any device with a horizontal screen width **smaller** then 567px. This can also be achieved using browser developer tools.
- Mobile+
    * Any device with a horizontal screen width **larger** then 567px

|1|Green dots on Hover|
|-|-|
- Open the website on a **mobile+** device
- Click on the play button
- After the animation finishes, hover the mouse over the individual shapes
- Confirm an outline of green dots appear around the hovered over shape when doing so

|2|Highscores|
|-|-|
- Open the website on **any** device
- Click or tap on the button that says 'View highscores'
- Confirm an overlay appears, with a screen that shows the local highscores

|3|Responsive design|
|-|-|
- Open the website on a **mobile+** device
- Confirm the 'View highscores' and 'How to play' buttons appear at the top right of the game area
- Open the browsers' developer tools (usually F12 on a windows computer)
- Toggle the device toolbar (usually 'Ctrl + shift + M' on a windows computer)
- Set the device width to a **mobile** device size
- Confirm the 'View highscores' and 'How to play' buttons appear below the game area

|4|Tutorial with gif|
|-|-|
- Open the website on **any** device for the first time (alternatively, you can delete the website's cookies)
- Confirm the tutorial is shown before you can start playing a game.

|5|Current game information|
|-|-|
- Open the website on a **mobile** device
- Confirm the Game information is visible centered above the game area
- Start playing a game, by tapping on the 'Play' button
- Tap on 1 correct shape
- Confirm the 'score' counter is incremented by 1
- Correctly finish the round, by clicking on the remaining correct shapes
- Confirm the level increases after finishing each round
- Play through several rounds
- Confirm the speed increases every 3 levels
- Open the website on a **mobile+** device
- Confirm the game information is now visible above the game area, aligned to the left side

---

## &rarr; **Bugs**
1. The main menu items are no longer displayed 
    * This is only when viewing on larger then mobile device sizes. 
---