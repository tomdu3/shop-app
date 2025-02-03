import pytest
from ..app import UserType, User, UserManager

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
    assert user_manager.current_user.is_admin() == False
    user_manager.logout()
    assert user_manager.current_user == None
