# Store all the functionality in a class
# When a new party of 4 or 5 come into the bar, and we open a new tab, we'll create a new instance of this Tab object
class Tab:

  # Dictionary - will remain the same for every tab
  # Class level attribute (if it's more extensive you could create it in a separate module)
  menu = {
    'wine': 5,
    'beer': 3,
    'soft_drink': 2,
    'chicken': 10,
    'beef': 15,
    'veggie': 12,
    'dessert': 6
  }

  # Initialization Function
  # Sets up basic properties when a new instance of a Tab is made
  def __init__(self):
    # Running total cost of the bill, starts at 0
    self.total = 0
    # List of items on the bill
    self.items = [ ]

  # Adding to the bill function
  def add(self, item):
    self.items.append(item)
    # self.menu[item] returns the key value (cost)
    self.total += self.menu[item]

  # 'Instance Function' - using self as a parameter
  def print_bill(self, tax, service):
    tax = (tax/100) * self.total
    service = (service/100) * self.total
    total = self.total + tax + service

    # For loop to print each item ordered
    for item in self.items:
      # Formattic string
      print(f'{item} ${self.menu[item]}')

    # Print the total of the bill
    # .2f prints the total value at 2 decimal points
    print(f'{"Total"} ${total:.2f}')
