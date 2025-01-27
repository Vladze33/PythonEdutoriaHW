import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if self.quantity < amount:
            raise ValueError(f'Amount ({amount}) too large to decrease products count ({self.quantity})')
        self.quantity -= amount

    def get_total_value(self):
        return self.price * self.quantity


class Warehouse:
    def __init__(self):
        self.products = dict()

    # Product price already exist
    def add_product(self, product_name, amount):
        try:
            self.products[product_name].increase_quantity(amount)
            logging.info(f'{amount} units of product "{product_name}" have been added to the warehouse')
        except KeyError:
            raise ValueError(f'Product "{product_name}" not found in warehouse')

    def remove_product(self, product_name, amount):
        try:
            self.products[product_name].decrease_quantity(amount)
            logging.info(f'{amount} units of product "{product_name}" have been removed from warehouse')
        except KeyError:
            raise ValueError(f'Product "{product_name}" not found in warehouse')

    def add_new_product(self, product):
        # Impossible to add product with different price
        if product.name in self.products:
            raise ValueError(f'Product "{product.name}" is already in warehouse')
        self.products[product.name] = product
        logging.info(f'New product "{product.name}" in quantity of {product.quantity} units added to warehouse')

    def get_total_value(self):
        return sum(product.get_total_value() for product in self.products)


class Seller:
    def __init__(self, name):
        self.name = name
        self.get_sales_history = list()

    def sell_product(self, warehouse, product_name, amount):
        if product_name in warehouse.products:
            product = warehouse.products[product_name]
            warehouse.products[product_name].decrease_quantity(amount)
            revenue = amount * product.price

            report_str = f'Seller {self.name} sold {amount} units of product "{product_name}" for revenue of {revenue}"'
            self.sales_history.append(report_str)
            logging.info(report_str)
        else:
            raise ValueError(f'Product "{product_name}" not found in warehouse')

    def get_sales_report(self):
        return self.sales_history
