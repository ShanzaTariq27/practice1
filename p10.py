class Inventory:
    def __init__(self):
        # self.items dictionary: name -> (qty, price)
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        total = 0
        for qty, price in self.items.values():
            total += qty * price
        return total

    def __len__(self):
        return len(self.items)


# --- Main Program ---
inv = Inventory()

# stock.txt ko read karna aur invalid lines ko skip karna
try:
    with open("stock.txt", "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 3:
                name, qty_str, price_str = parts
                try:
                    qty = int(qty_str)
                    price = int(price_str)
                    inv.add_item(name, qty, price)
                except ValueError:
                    print(f"Skipping {name}: bad number")
except FileNotFoundError:
    print("stock.txt file not found.")

# Initial items count aur total value print karna
print(f"{len(inv)} items, total value {inv.total_value()}")

# "pen" remove karke print karna, phir "laptop" remove karke error handle karna
try:
    inv.remove_item("pen")
    print(f"{len(inv)} items, total value {inv.total_value()}")
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")
    