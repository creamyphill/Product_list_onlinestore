class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = price
        self.online_shop = online_shop

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_orders = []

class OnlineShop:
    def __init__(self, name, url):
        self.name = str(name)
        self.url = url
        self.products = []

    def addingItemsToCart(self, customer, product, quantity):
        customer.cart.append({"product": product, "quantity": quantity})

    def checkOut(self, customer):
        if not customer.cart:
            print("Cart is empty.")
            return
        total = 0
        for things in customer.cart:
            total += things["product"].price * things["quantity"]

        order_id = len(customer.past_orders) + 1
        order_past = {"order": order_id, "items": customer.cart.copy(), "total": total}

        customer.past_orders.append(order_past)
        customer.cart.clear()
        print(f"Order #{order_id} in the cart. Total: {total} THB")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order"] == order_id:
                print(f"Order #{order_id} details:")
                for things in order["items"]:
                    print(f"- {things['product'].name} x {things['quantity']}")
                print(f"Total Price: {order['total']} THB")
                return
        print("Order not found.")


my_onlineshop = OnlineShop("GadgetWorld.com", "www.gadgetworld.com")
prod1 = Product("Gaming Headset X", "Hi-Fi Headphone W/RGB", 4500, my_onlineshop)
prod2 = Product("Mechanical Keyboard LightSpeed", "RGB Wireless Keyboard", 5000, my_onlineshop)

my_onlineshop.products.append(prod1)
my_onlineshop.products.append(prod2)

c1 = Customer("Jenson Button", "drsbutton@press.com", "22nd, Cafe Street, Manhattan")

my_onlineshop.addingItemsToCart(c1, prod1, 2)
my_onlineshop.addingItemsToCart(c1, prod2, 1)

my_onlineshop.checkOut(c1)
my_onlineshop.orderTracking(c1, 1)
