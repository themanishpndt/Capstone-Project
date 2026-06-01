"""
Subscription Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.subscription_locators import SubscriptionLocators


class SubscriptionPage(BasePage):
    """Subscription page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SubscriptionLocators()
    
    def subscribe_home_page(self, email):
        """Subscribe using email in home page section"""
        self.enter_text(self.locators.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click_element(self.locators.SUBSCRIPTION_BUTTON)
        self.logger.info(f"Subscribed with email: {email} in home page section")
    
    def subscribe_cart_page(self, email):
        """Subscribe using email in cart page"""
        self.enter_text(self.locators.CART_SUBSCRIPTION_EMAIL_INPUT, email)
        self.click_element(self.locators.CART_SUBSCRIPTION_BUTTON)
        self.logger.info(f"Subscribed with email: {email} in cart page")
    
    def subscribe_footer(self, email):
        """Subscribe using email in footer"""
        self.enter_text(self.locators.FOOTER_SUBSCRIPTION_EMAIL, email)
        self.click_element(self.locators.FOOTER_SUBSCRIPTION_BUTTON)
        self.logger.info(f"Subscribed with email: {email} in footer")
    
    def is_home_subscription_success_visible(self):
        """Check if home subscription success message is visible"""
        is_visible = self.is_element_visible(self.locators.SUBSCRIPTION_SUCCESS_MESSAGE)
        self.logger.info(f"Home subscription success message visible: {is_visible}")
        return is_visible
    
    def is_cart_subscription_visible(self):
        """Check if cart subscription section is visible"""
        is_visible = self.is_element_visible(self.locators.CART_SUBSCRIPTION_SECTION)
        self.logger.info(f"Cart subscription section visible: {is_visible}")
        return is_visible
    
    def is_footer_subscription_success_visible(self):
        """Check if footer subscription success message is visible"""
        is_visible = self.is_element_visible(self.locators.FOOTER_SUBSCRIPTION_SUCCESS)
        self.logger.info(f"Footer subscription success message visible: {is_visible}")
        return is_visible
    
    def subscribe_with_invalid_email(self, email):
        """Attempt subscription with invalid email"""
        self.enter_text(self.locators.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click_element(self.locators.SUBSCRIPTION_BUTTON)
        self.logger.info(f"Attempted subscription with invalid email: {email}")
    
    def is_subscription_error_visible(self):
        """Check if subscription error message is visible"""
        is_visible = self.is_element_visible(self.locators.SUBSCRIPTION_ERROR_MESSAGE)
        self.logger.info(f"Subscription error message visible: {is_visible}")
        return is_visible
