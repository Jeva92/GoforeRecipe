#!/usr/bin/python
import json
from flask import Flask
from flask import request
from flask import abort
from Recipe import Recipe

Recipes = []

recipe_data=json.load(open('recipes.json'))

for i in recipe_data:
    Recipes.append(Recipe(i).__dict__)

app = Flask(__name__)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    if request.method == 'GET':
        data = []
        for i in Recipes:
            data.append(i["name"])
        return json.dumps(data)
    elif request.method == 'POST':
        Recipes.append(json.load(request.body).__dict__)
        return abort(200)

@app.route('/recipe/<name>', methods=['GET', 'DELETE'])
def recipe(name):
    if request.method == 'GET':
        for i in Recipes:
            if i["name"] == name:
                return json.dumps(i)
        return abort(404)
    elif request.method == 'DELETE':
        for i in Recipes:
            if i["name"] == name:
                Recipes.remove(i)
                abort(200)
        return abort(404)

@app.route('/ingredient/<name>', methods=['GET'])
def ingredient(name):
    data = []
    for i in Recipes:
        for ii in i["ingredients"]:
            if ii["name"] == name:
                print i
                data.append(i)
    if len(data) < 1:
        return abort(404)
    else:
        return json.dumps(data)
