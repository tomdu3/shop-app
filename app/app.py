import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class UserType(Enum):
    """
    UserType - Defines the type of the User

    Parameters:
        type (str): The user type. Possible values are "user" and "admin".
    
    Returns:
        type (str): gives type of the User as output

    Example:
        user = UserType("user")
        print(user)  # output: `UserType.user`
    """

    user = "user"
    admin = "admin"


class User:
    """
    Defines the User class.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        user_type (UserType): The type of the user (user or admin).
        session_id (Optional[str]): The session ID of the user (default is None).

    Methods:
        login(password): Checks if the provided password matches the user's password.
        logout(): Logs out the user by setting the session ID to None.
        is_authenticated(): Returns True if the user is authenticated (session ID is not None), False otherwise.
        is_admin(): Returns True if the user is an admin, False otherwise.
    """
    def __init__(self, username: str, password: str, user_type: UserType):
        self.username = username
        self.password = password
        self.user_type = user_type
        self.session_id: Optional[str] = None

    def login(self, password: str) -> bool:
        """
        Checks if the provided password matches the user's password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
            """

        if self.password == password:
            self.session_id = str(uuid.uuid4())
            return True
        return False

    def logout(self):
        self.session_id = None

    def is_authenticated(self) -> bool:
        return self.session_id is not None

    def is_admin(self) -> bool:
        return self.user_type == UserType.admin


class Category:
    """
    Category class.

    Attributes:
        id (int): The ID of the category.
        name (str): The name of the category.
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class Product:
    """
    Product class.

    Attributes:
        id (int): The ID of the product.
        name (str): The name of the product.
        category_id (int): The ID of the category to which the product belongs.
        price (float): The price of the product.
    """

    def __init__(self, id: int, name: str, category_id: int, price: float):
        self.id = id
        self.name = name
        self.category_id = category_id
        self.price = price


class CartItem:
    """
    CartItem class.

    Attributes:
        product (Product): The product in the cart.
        quantity (int): The quantity of the product in the cart.
        subtotal (float): The subtotal of the product in the cart.
    """
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property  # make subtotal method a read-only property
    def subtotal(self) -> float:
        return self.product.price * self.quantity


class Cart:
    """
    Cart class.

    Attributes:
        items (Dict[int, CartItem]): A dictionary of cart items. Empty at initialization.

    Methods:
        add_item(product, quantity): Adds a new item to the cart with the provided product and quantity.
        remove_item(product_id): Removes the item with the provided product_id from the cart.
        get_total(): Calculates and returns the total price of all items in the cart.
        clear(): Clears the cart by removing all items.
    """
    def __init__(self):
        self.items: Dict[int, CartItem] = {}

    def add_item(self, product: Product, quantity: int):
        """
        Adds a new item to the cart with the provided product and quantity.

        Args:
            product (Product): The product to add to the cart.
            quantity (int): The quantity of the product to add to the cart.
        """

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)

    def remove_item(self, product_id: int):
        """
        Removes the item with the provided product_id from the cart.

        Args:
            product_id (int): The ID of the product to remove from the cart.
        """
        if product_id not in self.items:
            raise ValueError("Product not in cart")
        if product_id in self.items:
            del self.items[product_id]
    
    def update_item(self, product_id: int, quantity: int):
        """
        Updates the quantity of the item with the provided product_id in the cart.

        Args:
            product_id (int): The ID of the product to update in the cart.
            quantity (int): The new quantity of the product in the cart.
        """
        if product_id not in self.items:
            raise ValueError("Product not in cart")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        if product_id in self.items:
            if quantity == 0:
                del self.items[product_id]
                return
            self.items[product_id].quantity = quantity

    def get_total(self) -> float:
        """
        Calculates and returns the total price of all items in the cart.
        """
        return sum(item.subtotal for item in self.items.values())

    def clear(self):
        """
        Clears the cart by removing all items.
        """
        self.items.clear()


class PaymentMethod(Enum):
    """
    PaymentMethod enum class.
    """
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    UPI = "UPI"
    NET_BANKING = "Net Banking"
    PAYPAL = "PayPal"


class Payment:
    def __init__(self, amount: float, method: PaymentMethod):
        """
        Payment class.

        Attributes:
            amount (float): The amount to be paid.
            method (PaymentMethod): The payment method to be used.
            timestamp (datetime): The timestamp of the payment.
            status (str): The status of the payment.
        
        Methods:
            process() -> bool: Simulates the payment process.
        """
        self.amount = amount
        self.method = method
        self.timestamp = datetime.now()
        self.status = "pending"

    def process(self) -> bool:
        # Simulate payment processing
        self.status = "completed"
        return True


class ShoppingApp:
    """
    ShoppingApp class.

    Attributes:
        categories (Dict[int, Category]): A dictionary of categories. Empty at initialization.
        products (Dict[int, Product]): A dictionary of products. Empty at initialization.
        users (Dict[str, User]): A dictionary of users. Empty at initialization.
        carts (Dict[str, Cart]): A dictionary of carts. Empty at initialization.
        current_user (User): The current user. None at initialization.
        next_product_id (int): The next ID to be assigned to a new product. 5 at initialization.
        next_category_id (int): The next ID to be assigned to a new category. 5 at initialization.
        payments (List[Payment]): A list of payments. Empty at initialization.

    Methods:
        login(username, password) -> bool: Logs in the user with the provided username and password.
        logout(): Logs out the current user.
        check_user_privileges() -> bool: Checks if the current user has user privileges.
        check_admin_privileges() -> bool: Checks if the current user has admin privileges.
        add_to_cart(product_id, quantity) -> bool: Adds a product to the cart with the provided product_id and quantity.
        remove_from_cart(product_id) -> bool: Removes a product from the cart with the provided product_id.
        checkout() -> bool: Simulates the checkout process by processing the payment and clearing the cart.
    """

    def __init__(self):
        # DB simulated data
        self.categories: Dict[int, Category] = {
            1: Category(1, "Boots"),
            2: Category(2, "Coats"),
            3: Category(3, "Jackets"),
            4: Category(4, "Caps"),
        }
        
        self.products: Dict[int, Product] = {
            1: Product(1, "Leather Boots", 1, 199.99),
            2: Product(2, "Winter Coat", 2, 249.99),
            3: Product(3, "Denim Jacket", 3, 99.99),
            4: Product(4, "Sports Cap", 4, 29.99),
        }

        self.users = {
            "user1": User("user1", "pass123", UserType.user),
            "admin": User("admin", "admin123", UserType.admin),
        }
        self.carts: Dict[str, Cart] = {}
        self.current_user: Optional[User] = None
        self.next_product_id = 5
        self.next_category_id = 5

    def login(self, username: str, password: str) -> bool:
        # Simulate login
        if username in self.users and self.users[username].login(password):
            self.current_user = self.users[username]
            if not self.current_user.is_admin():
                self.carts[self.current_user.session_id] = Cart()
            return True
        return False

    def logout(self):
        # Simulate logout
        if self.current_user:
            self.current_user.logout()
            self.current_user = None

    def check_user_privileges(self) -> bool:
        # Check if the current user has user privileges
        if not self.current_user:
            print("Please log in first.")
            return False
        if self.current_user.is_admin():
            print("Admin cannot perform user operations.")
            return False
        return True

    def check_admin_privileges(self) -> bool:
        # Check if the current user has admin privileges
        if not self.current_user:
            print("Please log in first.")
            return False
        if not self.current_user.is_admin():
            print("Only admin can perform this operation.")
            return False
        return True

    def add_to_cart(self, product_id: int, quantity: int) -> bool:
        # Simulate adding product to cart
        if not self.check_user_privileges():
            return False
        if product_id not in self.products:
            print("Invalid product ID.")
            return False
        cart = self.carts[self.current_user.session_id]
        try:
            cart.add_item(self.products[product_id], quantity)
            print("Item added to cart successfully!")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def remove_from_cart(self, product_id: int) -> bool:
        # Simulate removing product from cart
        if not self.check_user_privileges():
            return False
        cart = self.carts[self.current_user.session_id]
        try:
            cart.remove_item(product_id)
            print("Item removed from cart successfully!")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def add_product(self, name: str, category_id: int, price: float) -> bool:
        # Simulate adding product
        if not self.check_admin_privileges():
            return False
        if category_id not in self.categories:
            print("Invalid category ID.")
            return False
        self.products[self.next_product_id] = Product(self.next_product_id, name, category_id, price)
        self.next_product_id += 1
        print("Product added successfully!")
        return True

    def update_product(self, product_id: int, name: str, category_id: int, price: float) -> bool:
        # Simulate updating product
        if not self.check_admin_privileges():
            return False
        if product_id not in self.products:
            print("Invalid product ID.")
            return False
        if category_id not in self.categories:
            print("Invalid category ID.")
            return False
        self.products[product_id] = Product(product_id, name, category_id, price)
        print("Product updated successfully!")
        return True

    def remove_product(self, product_id: int) -> bool:
        # Simulate removing product
        if not self.check_admin_privileges():
            return False
        if product_id not in self.products:
            print("Invalid product ID.")
            return False
        del self.products[product_id]
        print("Product removed successfully!")
        return True

    def add_category(self, name: str) -> bool:
        # Simulate adding category
        if not self.check_admin_privileges():
            return False
        self.categories[self.next_category_id] = Category(self.next_category_id, name)
        self.next_category_id += 1
        print("Category added successfully!")
        return True

    def remove_category(self, category_id: int) -> bool:
        # Simulate removing category
        if not self.check_admin_privileges():
            return False
        if category_id not in self.categories:
            print("Invalid category ID.")
            return False
        # Check if category has products
        for product in self.products.values():
            if product.category_id == category_id:
                print("Cannot remove category with existing products.")
                return False
        del self.categories[category_id]
        print("Category removed successfully!")
        return True

    def display_catalog(self):
        # Simulate displaying catalog
        print("\nProduct Catalog:")
        print("-" * 60)
        print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10}")
        print("-" * 60)
        for pid, product in self.products.items():
            category = self.categories[product.category_id].name
            print(f"{pid:<5} {product.name:<20} {category:<15} ${product.price:<10.2f}")

    def display_categories(self):
        # Simulate displaying categories
        print("\nCategories:")
        print("-" * 30)
        print(f"{'ID':<5} {'Name':<20}")
        print("-" * 30)
        for cid, category in self.categories.items():
            print(f"{cid:<5} {category.name:<20}")

    def checkout(self, payment_method: PaymentMethod) -> bool:
        # Simulate checkout
        if not self.check_user_privileges():
            return False
        cart = self.carts[self.current_user.session_id]
        if not cart.items:
            print("Cart is empty.")
            return False
        total = cart.get_total()
        payment = Payment(total, payment_method)
        if payment.process():
            print(f"You will be redirected to {payment_method.value} portal to make a payment of ${total:.2f}")
            print("Your order has been successfully placed!")
            cart.clear()
            return True
        return False
    
    def get_cart(self) -> Optional[Cart]:
        # Simulate getting cart
        if not self.current_user or not self.current_user.session_id:
            return None
        return self.carts.get(self.current_user.session_id)

    def remove_from_cart(self, product_id: int) -> bool:
        # Simulate removing product from cart
        if not self.check_user_privileges():
            return False
        
        cart = self.carts.get(self.current_user.session_id)
        if not cart:
            print("Cart not found.")
            return False
            
        try:
            cart.remove_item(product_id)
            print("Item removed from cart successfully!")
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False


def main():
    # Create an instance of the ShoppingApp
    shop = ShoppingApp()
    
    # Welcome message
    print("=" * 50)  
    print("Welcome to the Demo Marketplace!")
    print("=" * 50)
    
    # Main loop - User Menu
    while True:
        print("\n1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            
            if shop.login(username, password):
                print("Login successful!")
                
                if shop.current_user.is_admin():
                    # Admin Menu
                    while True:
                        print("\nAdmin Menu:")
                        print("1. View Catalog")
                        print("2. Add Product")
                        print("3. Update Product")
                        print("4. Remove Product")
                        print("5. View Categories")
                        print("6. Add Category")
                        print("7. Remove Category")
                        print("8. Logout")
                        
                        choice = input("Enter your choice: ")
                        
                        if choice == "1":
                            shop.display_catalog()
                        elif choice == "2":
                            name = input("Enter product name: ")
                            shop.display_categories()
                            category_id = int(input("Enter category ID: "))
                            price = float(input("Enter price: "))
                            shop.add_product(name, category_id, price)
                        elif choice == "3":
                            shop.display_catalog()
                            product_id = int(input("Enter product ID to update: "))
                            name = input("Enter new name: ")
                            shop.display_categories()
                            category_id = int(input("Enter new category ID: "))
                            price = float(input("Enter new price: "))
                            shop.update_product(product_id, name, category_id, price)
                        elif choice == "4":
                            shop.display_catalog()
                            product_id = int(input("Enter product ID to remove: "))
                            shop.remove_product(product_id)
                        elif choice == "5":
                            shop.display_categories()
                        elif choice == "6":
                            name = input("Enter category name: ")
                            shop.add_category(name)
                        elif choice == "7":
                            shop.display_categories()
                            category_id = int(input("Enter category ID to remove: "))
                            shop.remove_category(category_id)
                        elif choice == "8":
                            shop.logout()
                            print("Logged out successfully!")
                            break
                        else:
                            print("Invalid choice.")
                else:
                    # User Menu
                    while True:
                        print("\nUser Menu:")
                        print("1. View Products")
                        print("2. Add to Cart")
                        print("3. Remove from Cart")
                        print("4. View Cart")
                        print("5. Checkout")
                        print("6. Logout")
                        
                        choice = input("Enter your choice: ")
                        
                        if choice == "1":
                            shop.display_catalog()
                        elif choice == "2":
                            shop.display_catalog()
                            try:
                                product_id = int(input("Enter product ID: "))
                                quantity = int(input("Enter quantity: "))
                                shop.add_to_cart(product_id, quantity)
                            except ValueError:
                                print("Invalid input.")
                        elif choice == "3":
                            cart = shop.get_cart()
                            if cart and cart.items:
                                print("\nCart Contents:")
                                for item in cart.items.values():
                                    print(f"[{item.product.id}] {item.product.name}: {item.quantity}")
                                try:
                                    product_id = int(input("Enter product ID to remove: "))
                                    shop.remove_from_cart(product_id)
                                except ValueError:
                                    print("Invalid input.")
                            else:
                                print("Cart is empty.")
                        elif choice == "4":
                            cart = shop.carts.get(shop.current_user.session_id)
                            if cart and cart.items:
                                print("\nCart Contents:")
                                for item in cart.items.values():
                                    print(f"{item.product.name}: {item.quantity} x ${item.product.price:.2f} = ${item.subtotal:.2f}")
                                print(f"Total: ${cart.get_total():.2f}")
                            else:
                                print("Cart is empty.")
                        elif choice == "5":
                            print("\nAvailable Payment Methods:")
                            for i, method in enumerate(PaymentMethod, 1):
                                print(f"{i}. {method.value}")
                            try:
                                method_choice = int(input("Choose payment method: "))
                                if 1 <= method_choice <= len(PaymentMethod):
                                    payment_method = list(PaymentMethod)[method_choice-1]
                                    shop.checkout(payment_method)
                                else:
                                    print("Invalid payment method.")
                            except ValueError:
                                print("Invalid input.")
                        elif choice == "6":
                            shop.logout()
                            print("Logged out successfully!")
                            break
                        else:
                            print("Invalid choice.")
            else:
                print("Login failed. Invalid credentials.")
        elif choice == "2":
            print("Thank you for visiting Demo Marketplace!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()