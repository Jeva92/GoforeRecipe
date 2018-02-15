#!/usr/bin/python
import json
from flask import Flask
from flask import request
from flask import abort
from Recipes.Recipe import Recipe

#Lets save all recipes in a list, so that the data structure is similar to the original JSON
#Dict would have been easier to seach from, but I wanted to keep the data structure
Recipes = []

#Get recipe data from JSON file
recipe_data = json.load(open('recipes.json'))

#Append the recipe data to the list
for i in recipe_data:
    #Lets make every value in list to dict type so that it is easier to make it JSON later
    Recipes.append(Recipe(i).__dict__)

#Flask stuff, documentatiot said to use it like this (I've never used Flask before)
app = Flask(__name__)

#Route for recipes, allows GET and POST
@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    #GET all the names of the recipes
    if request.method == 'GET':
        data = []
        for i in Recipes:
            data.append(i["name"])
        #Return data in JSON format
        #Earlier I made the Recipe objects dict type so that this is easier
        return json.dumps(data)
    #POST new recipe
    elif request.method == 'POST':
        #We assume the data in the body is valid, there was no restrictions given in the assignment
        Recipes.append(json.load(request.body).__dict__)
        #I don't know if this is valid way to return 200
        return abort(200)

#Route for single recipe, allows GET and DELETE
@app.route('/recipe/<name>', methods=['GET', 'DELETE'])
def recipe(name):
    #GET one specific recipe with <name>
    #We assume that there is only one recipe for each name
    if request.method == 'GET':
        for i in Recipes:
            if i["name"] == name:
                return json.dumps(i)
        #Recipe with given name was not found
        return abort(404)
    #DELETE one specific recipe with <name>
    #Again we assume recipe name exists only once
    elif request.method == 'DELETE':
        for i in Recipes:
            if i["name"] == name:
                Recipes.remove(i)
                return abort(200)
        #Recipe with given name was not found
        return abort(404)

#Route for ingredients, allows only GET
@app.route('/ingredient/<name>', methods=['GET'])
def ingredient(name):
    #We try to find reciped that include this ingredient.
    #This time multiple results are possible
    data = []
    for i in Recipes:
        for ii in i["ingredients"]:
            if ii["name"] == name:
                data.append(i)
    #If no recipes were found, return 404
    if len(data) < 1:
        return abort(404)
    #Else return gathered data
    else:
        return json.dumps(data)
