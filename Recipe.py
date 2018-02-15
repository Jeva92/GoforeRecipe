import json
from Ingredient import Ingredient

class Recipe:
    def __init__(self, data):
        self.name = data["name"]
        self.instructions = data["instructions"]
        self.ingredients = []
        i = 0
        for ii in data["ingredients"]:
            self.ingredients.append(Ingredient(ii))
            self.ingredients[i] = self.ingredients[i].__dict__
            i += 1
            
    def get(self):
        return self.__dict__
