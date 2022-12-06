class ShoppingItem:
  def __init__(self, name, unit_price, quantity):
    self.name = name
    self.unit_price = unit_price
    self.quantity = quantity
    self.total_cost = self.unit_price * self.quantity

  def print_item(self):
    print(f"{self.name}: ${self.total_cost:.2f} ({self.quantity} x ${self.unit_price:.2f})")

class ShoppingList:
  def __init__(self):
    self.items = []
    self.total_amount = 0

  def add_item(self, item):
    self.items.append(item)
    self.total_amount += item.total_cost

  def print_list(self):
    for item in self.items:
      item.print_item()
    print(f"Total: ${self.total_amount:.2f}")

# Create a new shopping list
shopping_list = ShoppingList()

# Add some items to the shopping list
shopping_list.add_item(ShoppingItem("Bread", 3.49, 1))
shopping_list.add_item(ShoppingItem("Milk", 2.79, 2))
shopping_list.add_item(ShoppingItem("Butter", 4.29, 1))
shopping_list.add_item(ShoppingItem("Eggs", 3.99, 12))
shopping_list.add_item(ShoppingItem("Cheese", 6.99, 1))
shopping_list.add_item(ShoppingItem("Apples", 2.49, 5))

# Print the shopping list
shopping_list.print_list()
 