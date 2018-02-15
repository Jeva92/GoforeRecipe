#!/usr/bin/python
import json
from flask import Flask
from flask import request
from flask import abort
from Recipe import Recipe

Recipes = []

recipe_data=json.load(open('recipes.json'))

i = 0
for ii in recipe_data:
    Recipes.append(Recipe(ii))
    Recipes[i] = Recipes[i].__dict__
    i += 1

app = Flask(__name__)

@app.route('/recipes', methods=['GET'])
def recipes():
    return json.dumps(Recipes)
    if request.method == 'GET':
        return json.dumps(Recipes)
    elif request.method == 'POST':
        Recipes.append(request.body)
        Recipes[-1] = Recipes[-1].__dict__
        return abort(200)

@app.route('/recipe/<name>', methods=['GET', 'POST', 'DELETE'])
def recipe(name):
    if request.method == 'GET':
        for i in Recipes:
            if i["name"] == name:
                return json.dumps(i)
        return abort(404)
    elif request.method == 'POST':
        Recipes.append(json.load(request.body))
        Recipes[-1] = Recipes[-1].__dict__
        return abort (200)
    elif request.method == 'DELETE':
        for i in Recipes:
            if i["name"] == name:
                Recipes.remove(i)
                abort(200)
        return abort(404)