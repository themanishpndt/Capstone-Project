"""
Locators for Subscription Elements (Home and Cart Pages)
"""

from selenium.webdriver.common.by import By


class SubscriptionLocators:
    """Subscription element locators"""
    
    # Home page subscription
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MESSAGE = (By.XPATH, "//div[@id='success-subscribe']//*[contains(text(), 'You have been successfully subscribed')]")
    SUBSCRIPTION_ERROR_MESSAGE = (By.XPATH, "//div[@class='alert alert-danger']")
    
    # Cart page subscription
    CART_SUBSCRIPTION_SECTION = (By.XPATH, "//footer//*[contains(normalize-space(), 'Subscription')]")
    CART_SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    CART_SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    
    # Footer subscription (appears on multiple pages)
    FOOTER_SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    FOOTER_SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    FOOTER_SUBSCRIPTION_SUCCESS = (By.XPATH, "//div[@id='success-subscribe']//*[contains(text(), 'You have been successfully subscribed')]")
