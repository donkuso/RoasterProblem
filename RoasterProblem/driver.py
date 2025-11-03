import csv
from warehouse import Warehouse
from blend import Blend
from strategy import IncomeStrategy, MinimizeLeftoverStrategy

def read_in_resources(filename):
    beans = {}

    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}
            origin = row["Origin"]
            quantity = int(row["Quantity"])
            beans[origin] = quantity
    return Warehouse(
        ethiopia=beans.get("Ethiopia", 0),
        honduras=beans.get("Honduras", 0),
        rwanda=beans.get("Rwanda", 0)
    )

def read_in_recipes(filename):
    blends = []
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"].strip()
            recipe = {
                "Ethiopia": float(row["Ethiopia"]),
                "Honduras": float(row["Honduras"]),
                "Rwanda": float(row["Rwanda"])
            }
            price = float(row["Price/lb"])
            blend = Blend(name, recipe)
            blend.price_per_lb = price
            blends.append(blend)
    return blends

def ask_user():
    print("What would you like to optimize for?")
    print("1. Maximize income")
    print("2. Minimize leftover Ethiopia beans")
    print("3. Minimize leftover Honduras beans")
    print("4. Minimize leftover Rwanda beans")
    choice = input("enter the number of your choice: ").strip()
    return choice


'''
Analysis Question:
Additional budget and warehouse space
'''
def simulate_purchase(warehouse, blends, purchase):
    origin, amount = purchase
    temp = Warehouse(
        warehouse.beans["Ethiopia"], 
        warehouse.beans["Honduras"],
        warehouse.beans["Rwanda"]
    )
    temp.add_beans(origin, amount)
    strategy = IncomeStrategy(temp, blends)
    result = strategy.run()
    return result['income']

def test_purchases(warehouse, blends):
    purchases = [
        ("Rwanda", 500), 
        ("Ethiopia", 3000),
        ("Honduras" , 1200)
    ]

    outcomes = {
        p[0]: simulate_purchase(warehouse, blends, p) for p in purchases
    }

    best = max(outcomes.items(), key=lambda x:x[1])
    print("\n---Purchase Test---")
    for k, v in outcomes.items():
        print(f"{k}: ${v:.2f}")
    print(f"\n Recommended purchase:\n {best[0]} (Income = ${best[1]:.2f})")


def main():
    warehouse = read_in_resources("data/resources.csv")
    blends = read_in_recipes("data/recipes.csv")

    choice = ask_user()

    if choice == "1":
        strategy = IncomeStrategy(warehouse, blends)
        test_purchases(warehouse, blends)
    elif choice == "2":
        strategy = MinimizeLeftoverStrategy(warehouse, blends,"Ethiopia")
    elif choice == "3":
        strategy = MinimizeLeftoverStrategy(warehouse, blends, "Honduras")
    elif choice == "4":
        strategy = MinimizeLeftoverStrategy(warehouse, blends, "Rwanda")
    else:
        print("Invalid choice.")
        return
    
    result = strategy.run() #polymorphism
    
    print("\n--- Results ---")
    print("Recommended Batches:")
    for blend, num_batches in result['batches'].items():
        print(f"{blend}: {num_batches}")
    
    print(f"\nTotal income: ${result['income']}")
    print("Remaining Beans:")
    for bean, left in result['leftovers'].items():
        print(f"{bean}: {left} lbs")
        
    print("\nBatch Production History (Linked List):")
    strategy.history.display()

    print("\n"*3)
if __name__ == "__main__":
    main()