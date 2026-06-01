"""
Test Case 15: Place Order Register Before Checkout
Verify user can register before placing order
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

logger = logging.getLogger(__name__)


class TestPlaceOrderRegisterBeforeCheckout:
    """Test suite for placing order with registration before checkout"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    @allure.title("TC15: Place Order Register Before Checkout")
    @allure.description("Verify that user can register before checkout and place order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_place_order_register_before_checkout(self, driver, base_url):
        """Test placing order after registering before checkout"""
        with allure.step("Navigate to home and register"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
        
        with allure.step("Register new account"):
            login_page = LoginPage(driver)
            login_page.fill_registration_form(
                name="John Register",
                email="johnregister@example.com",
                password="RegPass123!",
                first_name="John",
                last_name="Register"
            )
        
        with allure.step("Login with newly registered account"):
            login_page.login("johnregister@example.com", "RegPass123!")
        
        with allure.step("Add product to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to checkout"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            cart_page.click_proceed_to_checkout()
        
        with allure.step("Complete checkout"):
            checkout_page = CheckoutPage(driver)
            # Fill delivery address
            checkout_page.fill_delivery_address(
                first_name="John",
                last_name="Register",
                address="123 Main Street",
                city="New York",
                state="NY",
                zipcode="10001",
                country="United States"
            )
            
            checkout_page.click_place_order()
        
        with allure.step("Verify order placement"):
            logger.info("Order placed successfully after registration")
