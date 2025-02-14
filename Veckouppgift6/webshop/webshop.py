import uuid


class Product:
    def __init__(self, name, price):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class Cart:
    def __init__(self, name):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__products = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__id

    def add_product(self, product):
        self.__products.append(product)

    def get_cart(self):
        for product in self.__products:
            print(product.get_name(), product.get_price())

    def get_products(self):
        return self.__products

    def checkout(self):
        Order(self.get_products()).place_order()


class Order:
    def __init__(self, products):
        self.__products = []
        self.__order_id = uuid.uuid4()
        self.__total_sum = sum(product.get_price() for product in products)
        self.__total_items = len(products)

    def place_order(self):
        print(f"Tack för att du har handlat!, det blir {self.__total_sum} kr.")
        return self.__total_sum
