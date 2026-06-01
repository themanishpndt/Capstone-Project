"""
Configuration Management
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for the test suite"""
    
    # Base URL
    BASE_URL = os.getenv('BASE_URL', 'https://automationexercise.com')
    
    # Browser Configuration
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
    WINDOW_SIZE = os.getenv('WINDOW_SIZE', '1920,1080')
    
    # Wait Times (in seconds)
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))
    PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', 30))
    
    # Test Data
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'test@example.com')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'Password123!')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'reports/logs/test.log')
    
    # Screenshot Configuration
    TAKE_SCREENSHOT_ON_FAILURE = os.getenv('TAKE_SCREENSHOT_ON_FAILURE', 'True').lower() == 'true'
    SCREENSHOT_PATH = os.getenv('SCREENSHOT_PATH', 'reports/screenshots/')
    
    # Report Configuration
    GENERATE_HTML_REPORT = os.getenv('GENERATE_HTML_REPORT', 'True').lower() == 'true'
    GENERATE_ALLURE_REPORT = os.getenv('GENERATE_ALLURE_REPORT', 'True').lower() == 'true'
    
    # Proxy Configuration
    USE_PROXY = os.getenv('USE_PROXY', 'False').lower() == 'true'
    PROXY_URL = os.getenv('PROXY_URL', '')


# Application URLs
class URLs:
    """Application URLs"""
    
    BASE_URL = Config.BASE_URL
    LOGIN_URL = f"{BASE_URL}/login"
    REGISTER_URL = f"{BASE_URL}/register"
    PRODUCTS_URL = f"{BASE_URL}/products"
    CART_URL = f"{BASE_URL}/cart"
    CHECKOUT_URL = f"{BASE_URL}/checkout"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    ORDERS_URL = f"{BASE_URL}/account/orders"
    WISHLIST_URL = f"{BASE_URL}/wishlist"
