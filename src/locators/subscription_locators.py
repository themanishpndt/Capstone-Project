"""
Locators for Subscription Elements (Home and Cart Pages)
"""

from selenium.webdriver.common.by import By


class SubscriptionLocators:
    """Subscription element locators"""
    
    # Home page subscription
    SUBSCRIPTION_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'You have been successfully subscribed')]")
    SUBSCRIPTION_ERROR_MESSAGE = (By.XPATH, "//div[@class='alert alert-danger']")
    
    # Cart page subscription
    CART_SUBSCRIPTION_SECTION = (By.XPATH, "//div[contains(text(), 'Subscription')]")
    CART_SUBSCRIPTION_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Your email address'][@name='email']")
    CART_SUBSCRIPTION_BUTTON = (By.XPATH, "//button[contains(text(), 'Subscribe')][@id='subscribe']")
    
    # Footer subscription (appears on multiple pages)
    FOOTER_SUBSCRIPTION_EMAIL = (By.XPATH, "//footer//input[@placeholder='Your email address']")
    FOOTER_SUBSCRIPTION_BUTTON = (By.XPATH, "//footer//button[contains(text(), 'Subscribe')]")
    FOOTER_SUBSCRIPTION_SUCCESS = (By.XPATH, "//footer//div[contains(text(), 'You have been successfully subscribed')]")
