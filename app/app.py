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


user = UserType("user") 
admin = UserType("admin")


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


# class UserManager:
#     """
#     Manages the user authentication.
    
#     Attributes:
#         current_user (User): The currently authenticated user (optional parameter). 
#         users: Dict[str, User]: A dictionary of users.

#     Methods:
#         login(username, password): Logs in a user with the provided username and password.
#         logout(): Logs out the current user.
#         register(username, password, user_type): Registers a new user with the provided username, password, and user_type.
        
        
#     """
#     def __init__(self):
#         """
#         Generates a dictionary of users on initialization and if the User is passed as an argument (optional), it will be added as a current_user, otherwise is None.
#         """
#         self.users: Dict[str, User] = {
#             "user": User("user", "pass123", UserType.user),
#             "admin": User("admin", "admin123", UserType.admin)
#         }
#         self.current_user: Optional[User] = None

#     def login(self, username: str, password: str) -> bool:
#         """
#         Logs in a user with the provided username and password.

#         Args:
#             username (str): The username of the user to log in.
#             password (str): The password of the user to log in.

#         Returns:
#             bool: True if the login is successful, False otherwise.
#         """
#         if username in self.users:
#             user = self.users[username]
#             if user.login(password):
#                 self.current_user = user
#                 return True
#         return False

#     def logout(self):
#         """
#         Logs out the curent user.
#         """
#         if self.current_user:
#             self.current_user.logout()
#             self.current_user = None

#     def register(self, username: str, password: str, user_type: UserType = UserType.user) -> bool:
#         """
#         Registers a new user with provided username, password, and user type.

#         Args:
#             username (str): The username of the new user.
#             password (str): The password of the new user.
#             user_type (UserType): The type of the new user (default is UserType.user).
#         Returns:
#             bool: True if the user is successfully registered, False otherwise
#         """
#         # if user is already in the database, return False
#         if username in self.users:
#             return False
#         self.users[username] = User(username, password, user_type)
#         return True


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


# class ProductManager:
#     """
#     Manages the products in the shop.

#     Attributes:
#         categories (Dict[int, Category]): A dictionary of categories. Autogenerated from the pseudo database.
#         products (Dict[int, Product]): A dictionary of products. Autogenerated from the pseudo database.

#     Methods:
#         add_product(name, category_id, price): Adds a new product with the provided name, category_id, and price.
#         update_product(product_id, name=None, category_id=None, price=None): Updates the product with the provided product_id with the new name, category_id, and price.
#         remove_product(product_id): Removes the product with the provided product_id.
#         add_category(name): Adds a new category with the provided name.
#         remove_category(category_id): Removes the category with the provided category_id.
#     """

#     def __init__(self):
#         # initial data
#         self.categories: Dict[int, Category] = {
#             1: Category(1, "Shoes"),
#             2: Category(2, "Coats"),
#             3: Category(3, "Jackets"),
#             4: Category(4, "Hats"),
#         }
        
#         self.products: Dict[int, Product] = {
#             1: Product(1, "Nike Shoes", 1, 199.99),
#             2: Product(2, "Versace Coat", 2, 2499.99),
#             3: Product(3, "Levis Jacket", 3, 499.99)
#         }

#     def add_product(self, name: str, category_id: int, price: float) -> Optional[Product]:
#         """
#         Adds a new product with the provided name, category_id, and price.

#         Args:
#             name (str): The name of the product.
#             category_id (int): The ID of the category to which the product belongs.
#             price (float): The price of the product.

#         Returns:
#             Optional[Product]: The added product if successful, None otherwise.
#         """
#         if category_id not in self.categories:
#             return None
#         new_id = max(self.products.keys(), default=0) + 1
#         product = Product(new_id, name, category_id, price)
#         self.products[new_id] = product
#         return product
    
#     def update_product(self, product_id: int, name: str = None, category_id: int = None, price: float = None) -> bool:
#         """
#         Updates the product with the provided product_id with the new name, category_id, and price.

#         Args:
#             product_id (int): The ID of the product to update.
#             name (str, optional): The new name of the product.
#             category_id (int, optional): The new category ID of the product.
#             price (float, optional): The new price of the product.

#         Returns:
#             bool: True if the product is successfully updated, False otherwise.
#         """
#         if product_id not in self.products:
#             return False
#         product = self.products[product_id]
#         if name:
#             product.name = name
#         if category_id and category_id in self.categories:
#             product.category_id = category_id
#         if price is not None:
#             product.price = price
#         return True
    
#     def remove_product(self, product_id: int) -> bool:
#         """
#         Removes the product with the provided product_id.

#         Args:
#             product_id (int): The ID of the product to remove.

#         Returns:
#             bool: True if the product is successfully removed, False otherwise.
#         """
#         if product_id not in self.products:
#             return False
#         del self.products[product_id]
#         return True
    
#     def add_category(self, name: str) -> Optional[Category]:
#         """
#         Adds a new category with the provided name.

#         Args:
#             name (str): The name of the category to add.

#         Returns:
#             Optional[Category]: The added category if successful, None otherwise.
#         """
#         new_id = max(self.categories.keys(), default=0) + 1
#         category = Category(new_id, name)
#         self.categories[new_id] = category
#         return category
    
#     def remove_category(self, category_id: int) -> bool:
#         """
#         Removes the category with the provided category_id.

#         Args:
#             category_id (int): The ID of the category to remove.

#         Returns:
#             bool: True if the category is successfully removed, False otherwise.
#         """
#         if category_id not in self.categories:
#             return False
#         # Check if category is in use, then don't remove if in use
#         for product in self.products.values():
#             if product.category_id == category_id:
#                 return False
#         del self.categories[category_id]
#         return True


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