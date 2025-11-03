class CoffeeProduct:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe

    def usage_per_batch(self):
        raise NotImplementedError("Sublcasses must implement usage_per_batch")

    def make(self):
        raise NotImplementedError("Subclasses must implement make()")