# https://realpython.com/blog/python/instance-class-and-static-methods-demystified/#delicious-pizza-factories-with-classmethod

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):    
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
