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
        for item in customer.cart:
            total += item["product"].price * item["quantity"]

        order_id = len(customer.past_orders) + 1
        order_past = {"order": order_id, "items": customer.cart.copy(), "total": total}

        customer.past_orders.append(order_past)
        customer.cart.clear()
        print(f"Order #{order_id} placed successfully. Total: {total} THB")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order"] == order_id:
                print(f"Order #{order_id} details:")
                for item in order["items"]:
                    print(f"- {item['product'].name} x {item['quantity']}")
                print(f"Total Price: {order['total']} THB")
                return
        print("Order not found.")


my_shop = OnlineShop("GADO", "www.gadgetworld.com")
pro1 = Product("Gaming Mouse Pro X", "High DPI Gaming Mouse", 1500, my_shop)
pro2 = Product("Mech KB", "RGB Keebs", 3500, my_shop)

my_shop.products.append(pro1)
my_shop.products.append(pro2)

customer69 = Customer("Alex Brundle", "alexsib@googoo.com", "69 Helm street")

my_shop.addingItemsToCart(customer69, pro1, 2)
my_shop.addingItemsToCart(customer69, pro2, 1)

my_shop.checkOut(customer69)
my_shop.orderTracking(customer69, 1)
