from batch_list import BatchList

class Strategy: 
    def __init__(self, warehouse, blends):
        self.warehouse = warehouse
        self.blends = blends
        self.history = BatchList()
    
    def run(self):
        raise NotImplementedError("Subclasses must implement this method")

    def maximize_income(self, results=None, income=0):
        if results is None:
            results = {blend.name: 0 for blend in self.blends}

        possible = [b for b in self.blends if self.warehouse.can_make_batch(b)]
        if not possible:
            return {"batches": results,
                    "income": income,
                    "leftovers": self.warehouse.beans
            }
        
        best_blend = max(possible, key=lambda b:b.price_per_lb)

        best_blend.make(self.warehouse, 100)
        results[best_blend.name] += 1
        income += best_blend.price_per_lb * 100
        
        self.history.add_batch(best_blend.name)

        return self.maximize_income(results, income)
    
    def minimize_leftover(self, target_origin, results=None, income=0):
        if results is None:
            results = {blend.name: 0 for blend in self.blends}
        
        possible = [b for b in self.blends if self.warehouse.can_make_batch(b)]
        
        # # --- DEBUG: show current target and per-blend usage/efficiency ---
        # print(f"\n[DEBUG] minimize_leftover called with target_origin = {target_origin}")
        # print(f"[DEBUG] Warehouse inventory: {self.warehouse.beans}")
        # print("[DEBUG] Possible blends and their target usage / recipe:")
        # for b in possible:
        #     target_use = b.recipe.get(target_origin, 0)
        #     print(f"  - {b.name}: uses {target_use} of {target_origin} per ratio-unit; recipe = {b.recipe}")
        # # ----------------------------------------------------------------

        if not possible:
            return {"batches": results,
                    "income": income,
                    "leftovers": self.warehouse.beans
            }
        
        def efficency(blend):
            target_use = blend.recipe.get(target_origin, 0)
            if target_use == 0:
                return 0
            other_ratio = sum(
                blend.recipe.get(o, 0) / self.warehouse.get_quantity(o)
                for o in self.warehouse.beans if o != target_origin and self.warehouse.get_quantity(o)
            )
            return target_use / (1 + other_ratio)

        
        best_blend = max(possible, key=efficency)

        if best_blend.recipe.get(target_origin, 0) == 0:
            return {"batches": results,
                    "income": income,
                    "leftovers": self.warehouse.beans
            }
        
        best_blend.make(self.warehouse, 100)
        results[best_blend.name] += 1
        income += best_blend.price_per_lb * 100

        self.history.add_batch(best_blend.name)
        
        return self.minimize_leftover(target_origin, results, income)
        

class IncomeStrategy(Strategy):
    def run(self):
        return self.maximize_income()
    
    def maximize_income(self, results=None, income=0):
        return super().maximize_income(results, income)
    

class MinimizeLeftoverStrategy(Strategy):
    def __init__(self, warehouse, blends, target_origin):
        super().__init__(warehouse, blends)
        self.target_origin = target_origin
    
    def run(self):
        return self.minimize_leftover(self.target_origin)
    
    def minimize_leftover(self, target_origin, results=None, income=0):
        return super().minimize_leftover(target_origin, results, income)
    