class Ingredient:
    def __init__(self, data):
        self.name = data["name"]
        self.amount = data["amount"]
        self.unit = data["unit"]
