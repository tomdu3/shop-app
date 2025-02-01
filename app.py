import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

class UserType(Enum):
    user = "user"
    admin = "admin"

# test UserType

user = UserType("user") 
admin = UserType("admin")

print(user)
print(admin)
