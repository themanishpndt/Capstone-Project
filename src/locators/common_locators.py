"""
Common locators used across multiple pages
"""

from selenium.webdriver.common.by import By


class CommonLocators:
    """Common element locators used across all pages"""
    
    # Navigation
    HOME_LINK = (By.XPATH, "//a[contains(text(), 'Home')]")
    PRODUCTS_LINK = (By.XPATH, "//a[contains(text(), 'Products')]")
    CART_LINK = (By.XPATH, "//a[contains(text(), 'Cart')]")
    ACCOUNT_LINK = (By.XPATH, "//a[contains(text(), 'Account')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(), 'Logout')]")
    
    # Header
    LOGO = (By.CLASS_NAME, "logo")
    SEARCH_BAR = (By.CLASS_NAME, "search-bar")
    USER_PROFILE_ICON = (By.CLASS_NAME, "user-profile-icon")
    
    # Messages and alerts
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    WARNING_MESSAGE = (By.CLASS_NAME, "warning-message")
    
    # Buttons
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@type='cancel']")
    OK_BUTTON = (By.XPATH, "//button[contains(text(), 'OK')]")
    
    # Footer
    FOOTER = (By.TAG_NAME, "footer")
    PRIVACY_LINK = (By.XPATH, "//a[contains(text(), 'Privacy Policy')]")
    TERMS_LINK = (By.XPATH, "//a[contains(text(), 'Terms of Service')]")
