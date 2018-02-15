#Class Ingredient
class Ingredient:
    def __init__(self, data):
        #All the data is stored here, not much to see
        self.name = data["name"]
        self.amount = data["amount"]
        self.unit = data["unit"]
