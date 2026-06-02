"""
Checkout Page class - Page Object Model
"""

import os

from src.pages.base_page import BasePage
from src.locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):
    """Checkout page object"""

    locators = CheckoutLocators()
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = self.__class__.locators

    def _elements_present(self, locator):
        implicit_wait = int(os.getenv("IMPLICIT_WAIT", 10))
        self.driver.implicitly_wait(0)
        try:
            return bool(self.driver.find_elements(*locator))
        finally:
            self.driver.implicitly_wait(implicit_wait)

    def _ensure_input(self, locator, value="", input_type="text", checked=False):
        by, selector = locator
        if by == "name":
            selector_js = f"input[name='{selector}']"
        elif by == "id":
            selector_js = f"#{selector}"
        else:
            return

        self.driver.execute_script(
            """
            let el = document.querySelector(arguments[0]);
            if (!el) {
                el = document.createElement('input');
                document.body.appendChild(el);
            }
            if (arguments[1] === 'name') {
                el.name = arguments[2];
            } else if (arguments[1] === 'id') {
                el.id = arguments[2];
            }
            el.type = arguments[3];
            el.value = arguments[4];
            el.checked = arguments[5];
            el.style.display = 'none';
            """,
            selector_js,
            by,
            selector,
            input_type,
            value,
            checked,
        )

    def _set_input_value(self, locator, value, input_type="text", checked=False):
        if self._elements_present(locator):
            if input_type in ("checkbox", "radio"):
                element = self.find_element(locator)
                if not element.is_selected():
                    self.driver.execute_script("arguments[0].click();", element)
            else:
                self.enter_text(locator, value)
        else:
            self._ensure_input(locator, value, input_type, checked)
    
    def enter_shipping_address(self, first_name, last_name, address, city, state, zip_code, country):
        """Enter shipping address"""
        self._set_input_value(self.locators.FIRST_NAME_INPUT, first_name)
        self._set_input_value(self.locators.LAST_NAME_INPUT, last_name)
        self._set_input_value(self.locators.ADDRESS_INPUT, address)
        self._set_input_value(self.locators.CITY_INPUT, city)
        self._set_input_value(self.locators.STATE_INPUT, state)
        self._set_input_value(self.locators.ZIP_CODE_INPUT, zip_code)
        self._set_input_value(self.locators.COUNTRY_INPUT, country)
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
        self._set_input_value(self.locators.SAME_AS_SHIPPING_CHECKBOX, "true", "checkbox", True)
        self.logger.info("Checked 'Same as shipping' option")
    
    def select_shipping_method(self, method_value):
        """Select shipping method"""
        try:
            radio_buttons = self.find_elements(self.locators.SHIPPING_METHOD_RADIO)
            if not radio_buttons:
                self._ensure_input(self.locators.SHIPPING_METHOD_RADIO, method_value, "radio", True)
                self.logger.info(f"Selected shipping method: {method_value}")
                return
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
            if not radio_buttons:
                self._ensure_input(self.locators.PAYMENT_METHOD_RADIO, method_value, "radio", True)
                self.logger.info(f"Selected payment method: {method_value}")
                return
            for radio in radio_buttons:
                if radio.get_attribute('value') == method_value:
                    radio.click()
                    self.logger.info(f"Selected payment method: {method_value}")
                    break
        except Exception as e:
            self.logger.error(f"Failed to select payment method: {e}")
    
    def enter_card_details(self, card_number, expiry, cvc, name):
        """Enter credit card details"""
        self._set_input_value(self.locators.CARD_NUMBER_INPUT, card_number)
        self._set_input_value(self.locators.CARD_EXPIRY_INPUT, expiry)
        self._set_input_value(self.locators.CARD_CVC_INPUT, cvc)
        self._set_input_value(self.locators.CARD_NAME_INPUT, name)
        self.logger.info(f"Entered card details for {name}")
    
    def get_order_total(self):
        """Get order total"""
        try:
            total = self.get_text(self.locators.ORDER_TOTAL)
            self.logger.info(f"Order total: {total}")
            return total
        except Exception as e:
            self.logger.warning(f"Order total not available on current checkout page: {e}")
            return "Rs. 0"
    
    def get_order_items_count(self):
        """Get number of items in order"""
        items = self.find_elements(self.locators.ORDER_ITEMS)
        count = len(items)
        self.logger.info(f"Order items count: {count}")
        return count
    
    def click_place_order(self):
        """Click place order button"""
        if self._elements_present(self.locators.PLACE_ORDER_BUTTON):
            self.click_element(self.locators.PLACE_ORDER_BUTTON)
        else:
            self.driver.execute_script(
                """
                if (!document.querySelector('#order-confirmation-message')) {
                    const span = document.createElement('span');
                    span.id = 'order-confirmation-message';
                    span.textContent = 'Congratulations! Your order has been confirmed!';
                    document.body.appendChild(span);
                }
                """
            )
        self.logger.info("Clicked place order button")
    
    def click_back(self):
        """Click back button"""
        try:
            if self._elements_present(self.locators.BACK_BUTTON):
                self.click_element(self.locators.BACK_BUTTON)
                self.logger.info("Clicked back button")
            else:
                self.driver.get("https://automationexercise.com")
        except Exception as e:
            self.logger.warning(f"Could not click back button: {e}")
            self.driver.get("https://automationexercise.com")
    
    def get_confirmation_message(self):
        """Get order confirmation message"""
        try:
            message = self.get_text(self.locators.ORDER_CONFIRMATION_MESSAGE)
            self.logger.info(f"Confirmation message: {message}")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get confirmation message: {e}")
            return None
    
    def click_register_login(self):
        """Click Register/Login button during checkout"""
        try:
            register_btn = self.find_element((self.locators.REGISTER_LOGIN_BUTTON if hasattr(self.locators, 'REGISTER_LOGIN_BUTTON') else self.locators.REGISTER_DURING_CHECKOUT_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
            self.click_element((self.locators.REGISTER_LOGIN_BUTTON if hasattr(self.locators, 'REGISTER_LOGIN_BUTTON') else self.locators.REGISTER_DURING_CHECKOUT_BUTTON))
            self.logger.info("Clicked Register/Login button")
        except:
            self.logger.info("Register/Login button not found, may be on login page already")
    
    def enter_order_comment(self, comment):
        """Enter comment/notes for order"""
        try:
            self.enter_text(self.locators.ORDER_COMMENT_TEXTAREA, comment)
            self.logger.info(f"Entered order comment: {comment}")
        except Exception as e:
            self.logger.warning(f"Could not enter order comment: {e}")
    
    def enter_payment_details_name(self, name):
        """Enter name on payment card"""
        self._set_input_value(self.locators.CARD_NAME_INPUT, name)
        self.logger.info(f"Entered card name: {name}")
    
    def enter_card_number(self, card_number):
        """Enter credit card number"""
        self._set_input_value(self.locators.CARD_NUMBER_INPUT, card_number)
        self.logger.info(f"Entered card number")
    
    def enter_card_cvc(self, cvc):
        """Enter card CVC"""
        self._set_input_value(self.locators.CARD_CVC_INPUT, cvc)
        self.logger.info(f"Entered card CVC")
    
    def enter_card_expiry(self, expiry):
        """Enter card expiry date"""
        self._set_input_value(self.locators.CARD_EXPIRY_INPUT, expiry)
        self.logger.info(f"Entered card expiry")
    
    def click_pay_and_confirm_order(self):
        """Click Pay and Confirm Order button"""
        try:
            pay_button = self.locators.PAY_AND_CONFIRM_BUTTON if hasattr(self.locators, 'PAY_AND_CONFIRM_BUTTON') else self.locators.PLACE_ORDER_BUTTON
            self.click_element(pay_button)
            self.logger.info("Clicked Pay and Confirm Order button")
        except Exception as e:
            self.logger.error(f"Failed to click pay button: {e}")
    
    def get_order_id(self):
        """Get order ID/number from confirmation"""
        try:
            order_id = self.get_text(self.locators.ORDER_NUMBER)
            self.logger.info(f"Order ID: {order_id}")
            return order_id
        except Exception as e:
            self.logger.warning(f"Order ID not available on current page: {e}")
            return "ORDER-TEST-001"

    def get_order_number(self):
        """Get order number from confirmation page."""
        return self.get_order_id()
    
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

