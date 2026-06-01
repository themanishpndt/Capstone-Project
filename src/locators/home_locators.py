"""
Locators for Home Page
"""

from selenium.webdriver.common.by import By


class HomeLocators:
    """Home page element locators"""
    
    # URL
    HOME_URL = "https://automationexercise.com"
    
    # Header navigation
    HOME_LINK = (By.XPATH, "//a[contains(text(), ' Home')]")
    PRODUCTS_LINK = (By.XPATH, "//a[contains(text(), 'Products')]")
    CART_LINK = (By.XPATH, "//a[contains(text(), ' Cart')]")
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    TEST_CASES_LINK = (By.XPATH, "//a[contains(text(), 'Test Cases')]")
    CONTACT_US_LINK = (By.XPATH, "//a[contains(text(), 'Contact us')]")
    
    # Logged in user message
    LOGGED_IN_USER_TEXT = (By.XPATH, "//li//a[contains(text(), 'Logged in as')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(), 'Logout')]")
    
    # Banner
    SLIDER_CONTAINER = (By.ID, "slider")
    FEATURED_ITEMS_SECTION = (By.CLASS_NAME, "features")
    
    # Subscription
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'You have been successfully')]")
    
    # Footer
    FOOTER_SECTION = (By.TAG_NAME, "footer")
    FOOTER_SUBSCRIPTION_EMAIL = (By.XPATH, "//footer//input[@placeholder='Your email address']")
    FOOTER_SUBSCRIPTION_BUTTON = (By.XPATH, "//footer//button[contains(text(), 'Subscribe')]")
    FOOTER_SUBSCRIPTION_SUCCESS = (By.XPATH, "//footer//div[contains(text(), 'You have been successfully')]")
    
    # Recommended items
    RECOMMENDED_SECTION = (By.CLASS_NAME, "recommended_items")
    RECOMMENDED_PRODUCTS = (By.XPATH, "//div[contains(@class, 'recommended_items')]//div[contains(@class, 'product-image-wrapper')]")
    RECOMMENDED_ADD_TO_CART_BUTTONS = (By.XPATH, "//div[contains(@class, 'recommended_items')]//a[contains(@class, 'add-to-cart')]")
    CART_MODAL = (By.ID, "cartModal")
    CART_MODAL_VIEW_CART_LINK = (By.XPATH, "//div[@id='cartModal']//u[contains(text(), 'View Cart')]/ancestor::a")
    
    # Scroll elements
    SCROLL_TOP_ARROW = (By.ID, "scrollUp")
