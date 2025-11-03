from coffeeproduct import CoffeeProduct

class Blend(CoffeeProduct):
    BATCH_SIZE = 100 # total lbs per batch

    def __init__(self, name, recipe): 
        super().__init__(name, recipe)
        self.name = name
        self.recipe = recipe
        #self.price_per_lb = price_per_lb
        
    def make(self, warehouse, quantity):

        # How many beans of each type needed?
        total_ratio = sum(self.recipe.values())
        required = {}
        for origin, ratio in self.recipe.items():
            required[origin] = (ratio / total_ratio) * quantity
        
        # checks if enough beans exist in the warehouse
        for origin, amount_needed in required.items():
            avaliable = warehouse.get_quantity(origin)
            if avaliable < amount_needed:
                raise ValueError(f"Not enough {origin} beans: need {amount_needed}, have {avaliable}")
            
        # subtracts used beans from warehouse
        for origin, amount_needed in required.items():
            warehouse.use_beans(origin, amount_needed)
        
        return required
    
    def usage_per_batch(self):
        total_ratio = sum(self.recipe.values())
        return {origin: (ratio / total_ratio) * self.BATCH_SIZE
                for origin, ratio in self.recipe.items()}
    
