import pytest
from datetime import datetime
from ..app import (
    UserType,
    User,
    UserManager,
    Category,
    Product,
    ProductManager,
    CartItem,  # NOQA
    Cart,
    PaymentMethod,
    Payment,
)

# Test data
USERNAME = "test_user"
PASSWORD = "test_password"
ADMIN_USERNAME = "admin_user"
ADMIN_PASSWORD = "admin_password"

# regular_user
@pytest.fixture
def regular_user():
    return User(USERNAME, PASSWORD, UserType.user)

# admin_user
@pytest.fixture
def admin_user():   
    return User(ADMIN_USERNAME, ADMIN_PASSWORD, UserType.admin)

# Test cases for UserType and User class
def test_user_initialization(regular_user):
    """
    Test correct creation of a User object.
    """
    assert regular_user.username == USERNAME
    assert regular_user.password == PASSWORD
    assert regular_user.user_type == UserType.user
    assert regular_user.session_id is None

# Test cases for UserType and User class
def test_admin_user(admin_user):
    """
    Test correct creation of an admin User object.
    """

    assert admin_user.username == ADMIN_USERNAME
    assert admin_user.password == ADMIN_PASSWORD
    assert admin_user.user_type == UserType.admin
    assert admin_user.session_id is None

# Test User methods
def test_user_methods(regular_user):
    """
    Test User methods on regular_user
    """
    assert regular_user.login(PASSWORD)
    assert regular_user.is_authenticated()
    assert regular_user.is_admin() == False
    assert regular_user.session_id is not None
    assert regular_user.login("wrong_password") == False
    # check if user logged out
    regular_user.logout() 
    assert regular_user.is_authenticated() == False

def test_admin_methods(admin_user):
    """
    Test User methods on admin_user
    """
    assert admin_user.login(ADMIN_PASSWORD)
    assert admin_user.is_authenticated()
    assert admin_user.is_admin()
    assert admin_user.session_id is not None

# Test data
NEW_USER = "new_user"
NEW_PASSWORD = "new_password"
ADMIN_USER = "admin_user" 
ADMIN_PASSWORD = "admin_password"
REGULAR_USER = "user"
REGULAR_PASSWORD = "pass123"

@pytest.fixture
def user_manager():
    return UserManager()

def test_register_and_login_new_user(user_manager):
    """
    Test registering and logging in a new regular user
    """
    assert user_manager.register(NEW_USER, NEW_PASSWORD, UserType.user)
    assert user_manager.login(REGULAR_USER, REGULAR_PASSWORD)
    assert user_manager.current_user.is_authenticated()
    assert user_manager.current_user.username == REGULAR_USER
    assert user_manager.current_user.user_type == UserType.user
    assert user_manager.current_user.is_admin() == False
    user_manager.logout()
    assert user_manager.current_user == None

def test_register_and_login_admin_user(user_manager):
    """
    Test registering and logging in a new admin user
    """
    assert user_manager.register(ADMIN_USER, ADMIN_PASSWORD, UserType.admin)
    assert user_manager.login(ADMIN_USER, ADMIN_PASSWORD)
    assert user_manager.current_user.is_authenticated()
    assert user_manager.current_user.username == ADMIN_USER
    assert user_manager.current_user.user_type == UserType.admin
    assert user_manager.current_user.is_admin()
    user_manager.logout()
    assert user_manager.current_user == None

# Test Category and Product classes
def test_category_and_product():
    """
    Test Category and Product classes
    """
    category = Category(1, "Electronics")
    product = Product(1, "Laptop", category.id, 999.99)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.category_id == category.id


# Test ProductManager class and methods

def test_product_manager():
    """
    Test ProductManager class and its methods
    """
    # add product
    product_manager = ProductManager()
    category = product_manager.add_category("Electronics")
    product = product_manager.add_product("Laptop", category.id, 999.99)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.category_id == category.id
    
    # update product
    product_manager.update_product(product.id, name="Updated Laptop", price=999.99)
    product = product_manager.products[product.id]
    assert product.name == "Updated Laptop"
    assert product.price == 999.99
    assert product.category_id == category.id

    # remove product
    product_manager.remove_product(product.id)
    assert product.id not in product_manager.products
    # remove category
    product_manager.remove_category(category.id)
    assert category.id not in product_manager.categories

    # remove category that is in use
    category = product_manager.remove_category(1)  # remove Shoes
    assert category is False  # category is in use if False

    # remove product that is in use
    product = product_manager.remove_product(1)  # remove Shoes
    assert product is True  # product removed if True
    # remove category with all products removed
    category = product_manager.remove_category(1) 
    assert category is True  # category removed if True

# Test CartItem and Cart classes

def test_cart():
    """
    Test CartItem and Cart classes
    """
    cart = Cart()
    # add item
    category = Category(5, "Electronics")
    product = Product(1, "Laptop", 5, 999.99)
    cart.add_item(product, 2)
    assert cart.items[product.id].quantity == 2
    assert cart.get_total() == 1999.98
    cart.remove_item(product.id)
    assert product.id not in cart.items
    # add multiple items
    product2 = Product(2, "Phone", 5, 499.99)
    product3 = Product(3, "Tablet", 5, 299.99)
    cart.add_item(product, 2)
    cart.add_item(product2, 1)
    cart.add_item(product3, 3)
    assert cart.items[product.id].quantity == 2
    assert cart.items[product2.id].quantity == 1
    assert cart.items[product3.id].quantity == 3
    assert cart.get_total() == 3399.94
    # remove item
    cart.remove_item(product.id)
    assert product.id not in cart.items
    assert cart.get_total() == 1399.96

    # clear cart
    cart.clear()
    assert cart.items == {}
    assert cart.get_total() == 0

    # update quantity
    cart.add_item(product, 2)
    assert cart.items[product.id].quantity == 2
    cart.update_item(product.id, 3)
    assert cart.items[product.id].quantity == 3

    # update quantity to 0
    cart.update_item(product.id, 0)
    assert product.id not in cart.items

    # update quantity to negative
    cart.add_item(product, 2)
    with pytest.raises(ValueError) as context:
        cart.update_item(product.id, -1)

    # Optional: Check the error message
    assert str(context.value) == "Quantity must not be negative"



def test_payment_method_enum():
    """
    Test PaymentMethod enum values
    """
    assert PaymentMethod.CREDIT_CARD.value == "Credit Card"
    assert PaymentMethod.DEBIT_CARD.value == "Debit Card" 
    assert PaymentMethod.UPI.value == "UPI"
    assert PaymentMethod.NET_BANKING.value == "Net Banking"
    assert PaymentMethod.PAYPAL.value == "PayPal"

def test_payment_initialization():
    """
    Test Payment class initialization
    """
    payment = Payment(100.0, PaymentMethod.CREDIT_CARD)
    assert payment.amount == 100.0
    assert payment.method == PaymentMethod.CREDIT_CARD
    assert isinstance(payment.timestamp, datetime)
    assert payment.status == "pending"

def test_payment_processing():
    """
    Test payment processing
    """
    payment = Payment(50.0, PaymentMethod.DEBIT_CARD)
    assert payment.status == "pending"
    assert payment.process() == True
    assert payment.status == "completed"

def test_payment_with_different_methods():
    """
    Test payment with different payment methods
    """
    methods = [
        PaymentMethod.CREDIT_CARD,
        PaymentMethod.DEBIT_CARD,
        PaymentMethod.UPI,
        PaymentMethod.NET_BANKING,
        PaymentMethod.PAYPAL
    ]
    
    for method in methods:
        payment = Payment(75.0, method)
        assert payment.method == method
        assert payment.status == "pending"
        assert payment.process() == True
        assert payment.status == "completed"