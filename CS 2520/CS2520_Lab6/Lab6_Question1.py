'''
Defines a product class that manages product inventory
'''

class Product:
    def __init__(self, code = '', price = 0, count = 0):
        self.code = code
        self.price = price
        self.count = count

    def set_code(self, code):
        # - set the product code (i.e. SKU234) to parameter code
        self.code = code
      
    def get_code(self):
        # - return the product code
        return self.code
    
    def set_price(self, price):
        # - set the price to parameter price
        self.price = price

    def get_price(self):
        # - return the price
        return self.price

    def set_count(self, count):
        # - set the number of items in inventory to parameter count
        self.count = count

    def get_count(self):
        # - return the count
        return self.count

    def add_inventory(self, amt):
        # - increase inventory by parameter amt
        self.count += amt

    def sell_inventory(self, amt):
        # - decrease inventory by parameter amt
        self.count -= amt

    def print_info(self):
        print(f"Name: {self.code} \
              \nPrice: {self.get_price():.2f} \
              \nCount: {self.get_count()}")

def inventory():
    food1 = Product()
    food1.set_code('Apple')
    food1.set_price(0.40)
    food1.set_count(3)
    food1.print_info()

    food1.add_inventory(10)
    food1.sell_inventory(5)
    food1.print_info()

    food2 = Product()
    food2.set_code('Golden Delicous')
    food2.set_price(0.55)
    food2.set_count(4)
    food2.print_info()

inventory()
