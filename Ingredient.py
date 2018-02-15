class Ingredient:
    def __init__(self, data):
        self.name = data["name"]
        self.amount = data["amount"]
        self.unit = data["unit"]

    def get(self):
        return self.__dict__
