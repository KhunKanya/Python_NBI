
# products = [
#     webshop.Product(name="Hammare", price=100),
#     webshop.Product(name="Skruvmejsel", price=50),
#     webshop.Product(name="Borrmaskin",price=1200),
#     webshop.Product(name="Såg",price=300),
#     webshop.Product(name="Måttband", price=80),
#     webshop.Product(name="Skiftnyckel", price=150),
#     webshop.Product(name="Tång", price=90),
#     webshop.Product(name="Spiklåda", price=200),
#     webshop.Product(name="Skruvset",  price=120),
#     webshop.Product(name="Slipmaskin", price=1800),
# ]

from webshop import Product, Order, Cart


def test_product_creation():
    product = Product("Hammer", 199.99)

    assert product.get_name() == "Hammer"
    assert product.get_price() == 199.99


def test_cart_add_product():
    cart = Cart("MyCart")
    product1 = Product("Screwdriver", 89.50)
    product2 = Product("Saw", 249.00)

    cart.add_product(product1)
    cart.add_product(product2)

    products = cart.get_products()
    assert len(products) == 2
    assert products[0].get_name() == "Screwdriver"
    assert products[1].get_name() == "Saw"


def test_cart_checkout():
    cart = Cart("MyCart")
    product1 = Product("Drill",  899.00)
    product2 = Product("Tape Measure", 76.00)

    cart.add_product(product1)
    cart.add_product(product2)

    # Call checkout and check if it places an order correctly
    order = Order(cart.get_products())

    assert order.place_order() == 975.00  # 899 + 79


def test_order_total():
    products = [
        Product("Wrench", 199.00),
        Product("Pliers", 159.50)
    ]

    order = Order(products)

    assert order.place_order() == 358.50  # 199 + 159.50