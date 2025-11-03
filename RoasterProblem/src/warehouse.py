
import csv
from blend import Blend

class Warehouse:
    def __init__(self, ethiopia, honduras, rwanda):
        self.beans = {
            "Ethiopia": ethiopia,
            "Honduras": honduras,
            "Rwanda": rwanda
        }

    def __str__(self):
        return f"Warehouse Inventory: {self.beans}"
    
    def get_quantity(self, origin):
        return self.beans.get(origin, 0)
    
    def use_beans(self, origin, amount):
        if origin in self.beans:
            if self.beans[origin] >= amount:
                self.beans[origin] -= amount
            else:
                raise ValueError(f"Not enough {origin} beans avaliable")
        else:
            KeyError(f"No beans from {origin} in warehouse")

    def add_beans(self, origin, amount):
        if origin in self.beans:
            self.beans[origin] += amount
        else:
            self.beans[origin] = amount
        
    def can_make_batch(self, blend, batches=1):
        """
        Returns True if we can make batches of given Blend given current inventory
        """
        usage = blend.usage_per_batch()
        for origin, lbs_per_batch in usage.items():
            required = lbs_per_batch * batches
            if self.get_quantity(origin) < required:
                return False
        return True