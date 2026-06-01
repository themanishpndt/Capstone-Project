# E-Commerce Web Automation Using Selenium and Python

## Project Overview
This capstone project is a comprehensive automated testing framework for an e-commerce web application. It demonstrates best practices in test automation using Selenium WebDriver with Python, including UI testing, integration testing, and end-to-end testing.

## Project Scope
This automation testing suite covers all critical functionalities of an e-commerce platform:

### 1. **User Authentication & Account Management**
   - User registration and account creation
   - Login and logout functionality
   - Password reset and recovery
   - Profile management and account settings
   - User session management

### 2. **Product Catalog & Search**
   - Product listing and browsing
   - Advanced product search
   - Product filtering (by price, category, rating)
   - Product sorting (by name, price, popularity)
   - Product detail pages
   - Product reviews and ratings

### 3. **Shopping Cart Management**
   - Add products to cart
   - Remove products from cart
   - Update product quantities
   - Cart persistence
   - Apply discount codes and coupons
   - Calculate totals and taxes

### 4. **Checkout & Payment Processing**
   - Checkout flow
   - Shipping address entry and validation
   - Billing address selection
   - Shipping method selection
   - Payment method selection
   - Order review and confirmation
   - Payment processing simulation

### 5. **Order Management**
   - Order history viewing
   - Order tracking
   - Order cancellation
   - Return and refund processes
   - Order invoice generation

### 6. **Wishlist & Favorites**
   - Add/remove products from wishlist
   - View wishlist
   - Move wishlist items to cart

### 7. **User Notifications & Communication**
   - Email notifications
   - Order status notifications
   - Newsletter subscription

## Technology Stack

### Core Technologies
- **Python 3.8+** - Primary programming language
- **Selenium WebDriver 4.x** - Browser automation tool
- **pytest** - Testing framework
- **pytest-xdist** - Parallel test execution
- **pytest-html** - HTML test reports

### Supporting Libraries
- **WebDriverManager** - Automated driver management
- **python-dotenv** - Environment variable management
- **Requests** - API testing and HTTP requests
- **Faker** - Test data generation
- **openpyxl** - Excel file handling
- **Pillow** - Screenshot and image comparison
- **allure-pytest** - Advanced test reporting

### Browsers Supported
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

### Development Tools
- **Git** - Version control
- **VS Code** - IDE
- **PyCharm** - Alternative IDE
- **Docker** - Containerization (optional)

## Project Structure
```
E-commerce_Web_automation/
│
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── conftest.py                    # Pytest configuration and fixtures
├── pytest.ini                     # Pytest settings
│
├── config/
│   ├── __init__.py
│   ├── config.py                  # Configuration management
│   ├── settings.py                # Environment-specific settings
│   └── urls.py                    # Application URLs
│
├── src/
│   ├── __init__.py
│   ├── pages/                     # Page Object Model classes
│   │   ├── __init__.py
│   │   ├── base_page.py           # Base page class
│   │   ├── login_page.py          # Login page
│   │   ├── registration_page.py   # Registration page
│   │   ├── product_page.py        # Product listing/search
│   │   ├── cart_page.py           # Shopping cart
│   │   ├── checkout_page.py       # Checkout page
│   │   ├── order_page.py          # Order history
│   │   └── wishlist_page.py       # Wishlist page
│   │
│   ├── drivers/                   # Driver management
│   │   ├── __init__.py
│   │   └── driver_factory.py      # WebDriver initialization
│   │
│   ├── utils/                     # Utility functions
│   │   ├── __init__.py
│   │   ├── logger_utils.py        # Logging utilities
│   │   ├── wait_utils.py          # Wait conditions and helpers
│   │   ├── screenshot_utils.py    # Screenshot capture
│   │   ├── excel_utils.py         # Excel operations
│   │   ├── data_generator.py      # Test data generation
│   │   └── assertions_utils.py    # Custom assertions
│   │
│   └── locators/                  # UI Element locators
│       ├── __init__.py
│       ├── login_locators.py
│       ├── product_locators.py
│       ├── cart_locators.py
│       ├── checkout_locators.py
│       └── common_locators.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login_logout.py       # Login/Logout tests
│   ├── test_registration.py       # User registration tests
│   ├── test_product_search.py     # Product search tests
│   ├── test_product_browse.py     # Product browsing tests
│   ├── test_product_filter.py     # Product filtering tests
│   ├── test_shopping_cart.py      # Cart management tests
│   ├── test_checkout.py           # Checkout process tests
│   ├── test_payment.py            # Payment processing tests
│   ├── test_order_management.py   # Order management tests
│   ├── test_wishlist.py           # Wishlist functionality tests
│   ├── test_user_profile.py       # User account tests
│   ├── test_notifications.py      # Notification tests
│   └── test_end_to_end.py         # End-to-end scenarios
│
├── test_data/
│   ├── __init__.py
│   ├── valid_users.csv            # Valid test user data
│   ├── invalid_credentials.csv    # Invalid test data
│   ├── products.json              # Product test data
│   └── orders.json                # Order test data
│
├── reports/                       # Test execution reports
│   ├── screenshots/               # Screenshot storage
│   └── logs/                      # Log files
│
└── .env                           # Environment variables (not in version control)
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

### Steps

1. **Clone the Repository** (or create the project folder)
```bash
cd "C:\Users\MANISH SHARMA\OneDrive\Desktop\Capstone Project"
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# OR
.\venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**
Create a `.env` file in the project root:
```
BASE_URL=https://your-ecommerce-site.com
BROWSER=chrome
HEADLESS=False
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20
```

5. **Verify Installation**
```bash
pytest --version
python -c "import selenium; print(selenium.__version__)"
```

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/test_login_logout.py
```

### Run Specific Test Function
```bash
pytest tests/test_login_logout.py::test_valid_login
```

### Run Tests with Verbose Output
```bash
pytest -v tests/
```

### Run Tests in Parallel
```bash
pytest -n auto tests/
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html tests/
```

### Run Tests with Specific Markers
```bash
pytest -m smoke tests/
pytest -m regression tests/
```

### Run Tests with Screenshots
```bash
pytest --capture=no tests/
```

## Test Categories

### 1. **Unit Tests**
   - Individual component testing
   - Utility function testing
   - Locator validation

### 2. **Integration Tests**
   - Component interaction testing
   - Page-to-page navigation
   - Data flow testing

### 3. **Functional Tests**
   - Feature functionality testing
   - Business logic validation
   - End-user scenarios

### 4. **UI Tests**
   - Element visibility and interactivity
   - Layout validation
   - Visual regression testing

### 5. **API Tests** (if applicable)
   - Backend API endpoint testing
   - Data validation
   - Response verification

### 6. **Regression Tests**
   - Previously fixed bug verification
   - Overall system stability

### 7. **Smoke Tests**
   - Critical path testing
   - Quick sanity checks

### 8. **End-to-End Tests**
   - Complete user journey testing
   - Cross-feature workflows

## Test Naming Convention
All tests follow the pytest naming convention:
```python
def test_<feature>_<scenario>():
    """
    Test description
    """
    # Test implementation
```

Example:
```python
def test_login_with_valid_credentials():
    # Test code
    pass

def test_add_product_to_cart():
    # Test code
    pass
```

## Page Object Model (POM)
This project uses the Page Object Model pattern for maintainability:
- Each page/feature has a corresponding class
- Element locators are centralized
- Reusable methods for common actions
- Reduces code duplication

## Configuration Management
- Environment-specific settings (dev, staging, production)
- Browser configuration
- Wait time configurations
- Logging levels
- Report generation settings

## Reporting & Logging
- Test execution reports in HTML format
- Detailed logs with timestamps
- Screenshot capture on test failures
- Allure reporting for advanced analytics

## Continuous Integration/Continuous Deployment (CI/CD)
This project can be integrated with:
- Jenkins
- GitHub Actions
- GitLab CI
- Azure DevOps

## Best Practices Implemented
1. ✅ Page Object Model Pattern
2. ✅ DRY (Don't Repeat Yourself) Principle
3. ✅ Proper Wait Mechanisms (Explicit Waits)
4. ✅ Comprehensive Logging
5. ✅ Test Data Management
6. ✅ Screenshot Capture on Failures
7. ✅ Proper Exception Handling
8. ✅ Test Organization and Categorization
9. ✅ Reusable Fixtures and Utilities
10. ✅ Clear Test Documentation

## Troubleshooting

### Issue: WebDriver Not Found
**Solution:** Install WebDriverManager
```bash
pip install webdriver-manager
```

### Issue: Tests Not Running
**Solution:** Verify pytest is installed and paths are correct
```bash
pytest --collect-only
```

### Issue: Timeout Errors
**Solution:** Increase wait times in configuration
```python
IMPLICIT_WAIT = 20
EXPLICIT_WAIT = 30
```

## Contributing
1. Create a new branch for each feature
2. Follow PEP 8 style guide
3. Add tests for new features
4. Update documentation
5. Submit pull request

## License
This project is part of the Capstone Project curriculum.

## Author
Created as a Capstone Project for E-Commerce Web Automation Testing

## Contact & Support
For issues or questions, please refer to the project documentation or contact the project maintainer.

---
**Last Updated:** June 1, 2026
**Project Status:** Active Development
