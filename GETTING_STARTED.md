# Getting Started with E-Commerce Web Automation Project

## Quick Start Guide

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Environment File

Copy the `.env.example` to `.env` and update with your configuration:

```bash
cp .env.example .env
```

Edit `.env` with your settings:
```
BASE_URL=https://your-ecommerce-site.com
BROWSER=chrome
HEADLESS=False
```

### 3. Run Tests

#### Run all tests:
```bash
pytest tests/ -v
```

#### Run specific test file:
```bash
pytest tests/test_login_logout.py -v
```

#### Run specific test function:
```bash
pytest tests/test_login_logout.py::TestLoginLogout::test_valid_login -v
```

#### Run with HTML report:
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

#### Run tests in parallel:
```bash
pytest tests/ -v -n auto
```

#### Run smoke tests only:
```bash
pytest tests/ -v -m smoke
```

#### Run with screenshots:
```bash
pytest tests/ -v --capture=no
```

## Test Files Overview

| Test File | Purpose | Test Count |
|-----------|---------|-----------|
| `test_login_logout.py` | Login/Logout functionality | 12 |
| `test_registration.py` | User registration | 8 |
| `test_product_search.py` | Product search | 8 |
| `test_product_browse.py` | Product browsing | 8 |
| `test_product_filter.py` | Product filtering | 9 |
| `test_shopping_cart.py` | Shopping cart | 12 |
| `test_checkout.py` | Checkout process | 13 |
| `test_wishlist.py` | Wishlist functionality | 7 |
| `test_order_management.py` | Order management | 10 |
| `test_payment.py` | Payment processing | 10 |
| `test_user_profile.py` | User profile management | 11 |
| `test_end_to_end.py` | End-to-end scenarios | 5 |

**Total Test Count: 113 tests**

## Test Naming Convention

All tests follow the pytest naming convention:

```python
def test_<feature>_<scenario>():
    """Test description"""
    # Test implementation
```

Examples:
- `test_valid_login()` - Tests login with valid credentials
- `test_add_product_to_cart()` - Tests adding product to cart
- `test_filter_products_by_price_range()` - Tests price filtering

## Project Structure

```
tests/                          # All test files
├── test_login_logout.py        # 12 login tests
├── test_registration.py        # 8 registration tests
├── test_product_search.py      # 8 search tests
├── test_product_browse.py      # 8 browsing tests
├── test_product_filter.py      # 9 filter tests
├── test_shopping_cart.py       # 12 cart tests
├── test_checkout.py            # 13 checkout tests
├── test_wishlist.py            # 7 wishlist tests
├── test_order_management.py    # 10 order tests
├── test_payment.py             # 10 payment tests
├── test_user_profile.py        # 11 profile tests
└── test_end_to_end.py          # 5 E2E tests

src/                            # Source code
├── pages/                      # Page Object Model classes
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Login page object
│   ├── product_page.py        # Product page object
│   ├── cart_page.py           # Cart page object
│   └── checkout_page.py       # Checkout page object
├── locators/                   # Element locators
│   ├── login_locators.py
│   ├── product_locators.py
│   ├── cart_locators.py
│   ├── checkout_locators.py
│   └── common_locators.py
└── utils/                      # Utility functions
    ├── logger_utils.py        # Logging utilities
    ├── wait_utils.py          # Wait condition helpers
    └── screenshot_utils.py    # Screenshot capture

config/                         # Configuration files
├── config.py                  # Application configuration

test_data/                      # Test data files
├── valid_users.csv            # Valid user test data
├── invalid_credentials.csv    # Invalid credentials
└── products.json              # Product test data

reports/                        # Test reports and logs
├── screenshots/               # Failure screenshots
└── logs/                       # Test execution logs
```

## Test Markers

Tests are marked with categories for selective execution:

- `@pytest.mark.smoke` - Critical smoke tests
- `@pytest.mark.regression` - Regression test cases
- `@pytest.mark.functional` - Functional test cases
- `@pytest.mark.end_to_end` - End-to-end scenarios
- `@pytest.mark.critical` - Critical tests

### Run tests by marker:

```bash
# Smoke tests only
pytest -m smoke tests/

# Regression tests only
pytest -m regression tests/

# Skip slow tests
pytest -m "not slow" tests/

# Multiple markers
pytest -m "smoke and critical" tests/
```

## Configuration

### Environment Variables (.env file)

```
BASE_URL=https://example.com
BROWSER=chrome                  # chrome, firefox, edge
HEADLESS=False                  # True for headless mode
WINDOW_SIZE=1920,1080
IMPLICIT_WAIT=10               # Implicit wait in seconds
EXPLICIT_WAIT=20               # Explicit wait in seconds
PAGE_LOAD_TIMEOUT=30           # Page load timeout
LOG_LEVEL=INFO                 # INFO, DEBUG, WARNING, ERROR
TAKE_SCREENSHOT_ON_FAILURE=True
```

## Common Test Scenarios

### Running Login Tests Only
```bash
pytest tests/test_login_logout.py -v
```

### Running Shopping Cart Tests
```bash
pytest tests/test_shopping_cart.py -v
```

### Running Complete Purchase Journey
```bash
pytest tests/test_end_to_end.py::TestEndToEnd::test_complete_purchase_journey -v
```

### Running Tests on Different Browser
```bash
pytest tests/ --browser firefox -v
```

### Running Headless
```bash
pytest tests/ --headless -v
```

## Test Reports

### HTML Report
```bash
pytest tests/ --html=reports/report.html --self-contained-html
# Report will be generated at: reports/report.html
```

### Allure Report
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### JUnit XML Report
```bash
pytest tests/ --junit-xml=reports/junit.xml
```

## Troubleshooting

### Issue: WebDriver Not Found
```bash
pip install webdriver-manager
```

### Issue: Tests Timeout
Increase wait times in `.env`:
```
EXPLICIT_WAIT=30
PAGE_LOAD_TIMEOUT=60
```

### Issue: Unable to Find Elements
- Check element locators in `src/locators/`
- Verify application URL in `.env`
- Check browser compatibility

## Page Object Model (POM)

The project uses POM for maintainability:

```python
from src.pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("email@test.com", "password")
```

## Best Practices

✅ **Do:**
- Use page objects for UI interactions
- Centralize element locators
- Write descriptive test names
- Use explicit waits
- Take screenshots on failures
- Organize tests by feature

❌ **Don't:**
- Use implicit waits alone
- Hardcode locators in test methods
- Mix business logic with test code
- Ignore wait conditions
- Use sleep() for waits

## Running Tests in CI/CD

### GitHub Actions Example
```yaml
- name: Run Tests
  run: pytest tests/ -v --html=report.html
```

### Jenkins Example
```groovy
stage('Test') {
    steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest tests/ -v'
    }
}
```

## Support & Documentation

- See [README.md](README.md) for detailed project documentation
- Check individual test files for specific test scenarios
- Review [pytest.ini](pytest.ini) for pytest configuration
- See [conftest.py](conftest.py) for fixture definitions

## Next Steps

1. ✅ Install dependencies: `pip install -r requirements.txt`
2. ✅ Configure `.env` file with your application URL
3. ✅ Run first test: `pytest tests/test_login_logout.py::TestLoginLogout::test_valid_login -v`
4. ✅ Generate report: `pytest tests/ --html=reports/report.html --self-contained-html`
5. ✅ Review results in reports/report.html

Happy Testing! 🚀
