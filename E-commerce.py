class Product:
    def __init__(self, id, name, stock, price):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - ${self.price} | Stock: {self.stock}"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item["product"].id != product_id]

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                product = item["product"]
                print(f"{product.name} (ID: {product.id}) - ${product.price} * {item['quantity']}")

    def get_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)


class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items
        self.total = total

    def __str__(self):
        return f"Order Total: ${self.total} | Items: {len(self.items)}"


class EcommerceSystem:
    def __init__(self):
        self.products = []
        self.users = []
        self.orders = []
        self.current_user = None
        self.cart = Cart()

    def add_product(self, product):
        self.products.append(product)

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        return user

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def place_order(self, user, items, total):
        order = Order(user, items, total)
        self.orders.append(order)
        user.add_order(order)

    def run(self):
        self.add_product(Product(1, "Laptop", 10, 35000))
        self.add_product(Product(2, "Tablet", 5, 10500))
        self.add_product(Product(3, "Phone", 3, 5600))

        while True:
            print("\n=== Simple E-commerce System ===")
            if not self.current_user:
                print("1. Register\n2. Login\n3. Exit")
            else:
                print(f"Logged in as {self.current_user.username}")
                print("1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Logout")

            choice = input("Enter your choice: ")

            if not self.current_user:
                if choice == "1":
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    self.register_user(username, password)
                    print("User registered successfully!")

                elif choice == "2":
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    self.current_user = self.login_user(username, password)
                    if self.current_user:
                        print("Login successful!")
                    else:
                        print("Invalid username or password.")

                elif choice == "3":
                    break
                else:
                    print("Invalid choice.")

            else:
                if choice == "1":
                    print("\nAvailable Products:")
                    for product in self.products:
                        print(product)

                elif choice == "2":
                    product_id = int(input("Enter product ID: "))
                    quantity = int(input("Enter quantity: "))
                    product = next((p for p in self.products if p.id == product_id), None)
                    if product and product.stock >= quantity:
                        self.cart.add_item(product, quantity)
                        print(f"{product.name} added to cart.")
                    else:
                        print("Invalid product ID or insufficient stock.")

                elif choice == "3":
                    print("\nYour Cart:")
                    self.cart.view_cart()

                elif choice == "4":
                    total = self.cart.get_total()
                    if total > 0:
                        self.place_order(self.current_user, self.cart.items, total)
                        print(f"Order placed successfully! Total: ${total}")
                        self.cart = Cart()  # Clear the cart after checkout
                    else:
                        print("Your cart is empty.")

                elif choice == "5":
                    self.current_user = None
                    self.cart = Cart()
                    print("Logged out successfully.")

                else:
                    print("Invalid choice.")


# Run the e-commerce system
system = EcommerceSystem()
system.run()