"""
Locators for Scroll Functionality Elements
"""

from selenium.webdriver.common.by import By


class ScrollLocators:
    """Scroll functionality element locators"""
    
    # Scroll to top button
    SCROLL_UP_BUTTON = (By.ID, "scrollUp")
    
    # Footer element to scroll to
    FOOTER = (By.TAG_NAME, "footer")
    
    # Body element for scroll position
    BODY = (By.TAG_NAME, "body")
    
    # Page content sections
    HEADER = (By.TAG_NAME, "header")
    FEATURED_SECTION = (By.CLASS_NAME, "features")
    PRODUCTS_SECTION = (By.ID, "Women")
