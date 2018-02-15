import json
from Ingredient import Ingredient

class Recipe:
    def __init__(self, data):
        self.name = data["name"]
        self.instructions = data["instructions"]
        self.ingredients = []
        for i in data["ingredients"]:
            self.ingredients.append(Ingredient(i).__dict__)

    def get(self):
        return self.__dict__
