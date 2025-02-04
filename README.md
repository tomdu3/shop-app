# Shopping App Project

A comprehensive Python-based shopping application implementing a dual-role system with separate functionalities for users and administrators.

## Table of Contents
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Data Models](#data-models)
- [Access Control](#access-control)
- [Implementation Details](#implementation-details)
- [User Interface](#user-interface)

## Technologies Used

### Core Libraries
- **uuid**: Generates unique identifiers for sessions and transactions
- **datetime**: Handles timestamp creation for sessions and transactions
- **enum**: Implements type-safe enumerations for:
  - User Types (Admin/User)
  - Payment Methods
- **typing**: Provides type hints through:
  - Dict: For type-safe collections
  - List: For array-type annotations
  - Optional: For nullable values

### Purpose of Each Library
1. **uuid Library**
   - Session ID generation
   - Transaction tracking
   - Unique identifier creation for cart items

2. **datetime Library**
   - Session timestamp management
   - Transaction logging
   - Order tracking

3. **enum Library**
   - User role definition (UserType.admin, UserType.user)
   - Payment method categorization:
     - UPI
     - Debit Card
     - Net Banking
     - PayPal

4. **typing Library**
   - Type safety for collections
   - Better code documentation
   - Enhanced IDE support
   - Runtime type checking capabilities

## System Architecture

### Core Components
Shopping App
├── Authentication System
│   ├── User Management
│   ├── Session Handling
│   └── Privilege Control
├── Product System
│   ├── Category Management
│   └── Product Management
├── Shopping System
│   ├── Cart Management
│   └── Checkout Process
└── Payment System
    └── Multiple Payment Methods

## Features

### Authentication System
- Secure login mechanism
- Session-based authentication
- Role-based access control
- Automatic privilege verification

### Product Management
- Complete CRUD operations for products
- Category-based organization
- Inventory tracking
- Price management

### Shopping Features
1. Cart Management
   - Add products with quantity
   - Remove products
   - View cart contents
   - Calculate totals

2. Checkout System
   - Multiple payment methods
   - Transaction processing
   - Cart clearing post-purchase

## Data Models

### User Model
class User:
    username: str
    password: str
    type: UserType
    session_id: Optional[str]

### Product Model
class Product:
    id: int
    name: str
    category_id: int
    price: float

### Category Model
class Category:
    id: int
    name: str

### Cart Model
class Cart:
    items: Dict[int, CartItem]
    user_id: str

## Access Control

### User Permissions Matrix

| Feature               | User | Admin |
|----------------------|------|-------|
| View Products        | ✅   | ✅    |
| Add to Cart          | ✅   | ❌    |
| Checkout             | ✅   | ❌    |
| Manage Products      | ❌   | ✅    |
| Manage Categories    | ❌   | ✅    |

## Implementation Details

### Session Management
- Unique session IDs using UUID
- Session validation before operations
- Automatic session clearing on logout

### Cart Implementation
- Per-user cart storage
- Real-time total calculation
- Quantity management
- Product validation

### Payment Processing
1. Payment Method Selection
2. Transaction Initialization
3. Payment Validation
4. Order Completion

## User Interface

### Main Menu
1. Login
2. Exit

### Admin Menu
1. View Products
2. Add Product
3. Update Product
4. Remove Product
5. View Categories
6. Add Category
7. Remove Category
8. Logout

### User Menu
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Checkout
6. Logout

### Input Validation
- Numeric input verification
- Product existence checking
- Category validation
- Quantity validation

### Error Handling
- Invalid input management
- Privilege violation alerts
- Transaction failure handling
- Session expiration management

## Security Features

1. **Access Control**
   - Role-based permissions
   - Session validation
   - Operation authorization

2. **Data Validation**
   - Input sanitization
   - Type checking
   - Boundary validation

3. **Session Security**
   - Unique session IDs
   - Session timeout
   - Secure logout process

## Current Limitations and Future Improvements

### Limitations
- In-memory data storage
- Single session per user
- Basic authentication

### Planned Improvements
- Persistent data storage
- Enhanced security features
- Multiple session support
- Transaction history