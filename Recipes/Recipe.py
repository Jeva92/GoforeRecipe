import json
from Ingredient import Ingredient

#Class Recipe
class Recipe:
    def __init__(self, data):
        #All the data is stored in init
        self.name = data["name"]
        self.instructions = data["instructions"]
        #Ingredients have their own list
        self.ingredients = []
        for i in data["ingredients"]:
            #Lets make this one dict type also, easier that way
            self.ingredients.append(Ingredient(i).__dict__)
