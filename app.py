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
        return self.user_type == UserType.ADMIN
