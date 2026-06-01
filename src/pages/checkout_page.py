"""
Checkout Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    """Checkout page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutLocators()
    
    def enter_shipping_address(self, first_name, last_name, address, city, state, zip_code, country):
        """Enter shipping address"""
        self.enter_text(self.locators.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.locators.LAST_NAME_INPUT, last_name)
        self.enter_text(self.locators.ADDRESS_INPUT, address)
        self.enter_text(self.locators.CITY_INPUT, city)
        self.enter_text(self.locators.STATE_INPUT, state)
        self.enter_text(self.locators.ZIP_CODE_INPUT, zip_code)
        self.enter_text(self.locators.COUNTRY_INPUT, country)
        self.logger.info(f"Entered shipping address for {first_name} {last_name}")
    
    def fill_delivery_address(self, first_name, last_name, address, city, state, zipcode, country):
        """Fill delivery address (alias for enter_shipping_address)"""
        self.enter_shipping_address(first_name, last_name, address, city, state, zipcode, country)
    
    def get_billing_address(self):
        """Get billing address information"""
        try:
            billing_address = self.get_text(self.locators.BILLING_ADDRESS_SECTION)
            self.logger.info(f"Billing address: {billing_address}")
            return billing_address
        except Exception as e:
            self.logger.error(f"Failed to get billing address: {e}")
            return None
    
    def get_delivery_address(self):
        """Get delivery address information"""
        try:
            delivery_address = self.get_text(self.locators.DELIVERY_ADDRESS_SECTION)
            self.logger.info(f"Delivery address: {delivery_address}")
            return delivery_address
        except Exception as e:
            self.logger.error(f"Failed to get delivery address: {e}")
            return None
    
    def use_same_as_shipping(self):
        """Check 'Same as shipping' checkbox"""
        self.click_element(self.locators.SAME_AS_SHIPPING_CHECKBOX)
        self.logger.info("Checked 'Same as shipping' option")
    
    def select_shipping_method(self, method_value):
        """Select shipping method"""
        try:
            radio_buttons = self.find_elements(self.locators.SHIPPING_METHOD_RADIO)
            for radio in radio_buttons:
                if radio.get_attribute('value') == method_value:
                    radio.click()
                    self.logger.info(f"Selected shipping method: {method_value}")
                    break
        except Exception as e:
            self.logger.error(f"Failed to select shipping method: {e}")
    
    def select_payment_method(self, method_value):
        """Select payment method"""
        try:
            radio_buttons = self.find_elements(self.locators.PAYMENT_METHOD_RADIO)
            for radio in radio_buttons:
                if radio.get_attribute('value') == method_value:
                    radio.click()
                    self.logger.info(f"Selected payment method: {method_value}")
                    break
        except Exception as e:
            self.logger.error(f"Failed to select payment method: {e}")
    
    def enter_card_details(self, card_number, expiry, cvc, name):
        """Enter credit card details"""
        self.enter_text(self.locators.CARD_NUMBER_INPUT, card_number)
        self.enter_text(self.locators.CARD_EXPIRY_INPUT, expiry)
        self.enter_text(self.locators.CARD_CVC_INPUT, cvc)
        self.enter_text(self.locators.CARD_NAME_INPUT, name)
        self.logger.info(f"Entered card details for {name}")
    
    def get_order_total(self):
        """Get order total"""
        try:
            total = self.get_text(self.locators.ORDER_TOTAL)
            self.logger.info(f"Order total: {total}")
            return total
        except Exception as e:
            self.logger.error(f"Failed to get order total: {e}")
            return None
    
    def get_order_items_count(self):
        """Get number of items in order"""
        items = self.find_elements(self.locators.ORDER_ITEMS)
        count = len(items)
        self.logger.info(f"Order items count: {count}")
        return count
    
    def click_place_order(self):
        """Click place order button"""
        self.click_element(self.locators.PLACE_ORDER_BUTTON)
        self.logger.info("Clicked place order button")
    
    def click_back(self):
        """Click back button"""
        try:
            self.click_element(self.locators.BACK_BUTTON)
            self.logger.info("Clicked back button")
        except Exception as e:
            self.logger.warning(f"Could not click back button: {e}")
    
    def get_confirmation_message(self):
        """Get order confirmation message"""
        try:
            message = self.get_text(self.locators.ORDER_CONFIRMATION_MESSAGE)
            self.logger.info(f"Confirmation message: {message}")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get confirmation message: {e}")
            return None
    
    def get_order_id(self):
        """Get order ID/number from confirmation"""
        try:
            order_id = self.get_text(self.locators.ORDER_NUMBER)
            self.logger.info(f"Order ID: {order_id}")
            return order_id
        except Exception as e:
            self.logger.error(f"Failed to get order ID: {e}")
            return None
    
    def register_during_checkout(self, name, email, password):
        """Register new user during checkout"""
        try:
            self.enter_text(self.locators.REGISTER_NAME_INPUT, name)
            self.enter_text(self.locators.REGISTER_EMAIL_INPUT, email)
            self.enter_text(self.locators.REGISTER_PASSWORD_INPUT, password)
            self.click_element(self.locators.REGISTER_DURING_CHECKOUT_BUTTON)
            self.logger.info(f"Registered during checkout for: {email}")
        except Exception as e:
            self.logger.error(f"Failed to register during checkout: {e}")

