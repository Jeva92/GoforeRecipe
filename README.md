# GoforeRecipe

# Installation
This application requires following:
 - Python 2.7
 - Pip

 Using Pip you need to install flask http://flask.pocoo.org
 ```sh
 PC:~$: pip install Flask
 ```

# Usage
Run the application using the following:
```sh
PC:~$: export FLASK_APP=app.py
PC:~$: flask run
```
The app will run in http://localhost:5000

## API

### GET /recipes  
Return all the recipes in the app

### POST /recipes  
Add a new recipe. Assumes the body of the request is valid type os Recipe

### GET /recipe/\<name\>  
Return recipe with \<name\>

### DELETE /recipe/\<name\>  
Deletes recipe with \<name\>
