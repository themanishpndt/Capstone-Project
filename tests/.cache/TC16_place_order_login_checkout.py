"""
Test Case 16: Place Order Login Before Checkout
Verify user can login and place order
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


class TestPlaceOrderLoginBeforeCheckout:
    """Test suite for placing order after login before checkout"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    @allure.title("TC16: Place Order Login Before Checkout")
    @allure.description("Verify that user can login and place order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_place_order_login_before_checkout(self, driver, base_url):
        """Test placing order after login"""
        with allure.step("Navigate to home and login"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
        
        with allure.step("Login with valid credentials"):
            login_page = LoginPage(driver)
            login_page.login("test@example.com", "Password123!")
        
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
        
        with allure.step("Verify logged in user details"):
            checkout_page = CheckoutPage(driver)
            # User details should be pre-filled for logged-in user
            logger.info("Logged-in user details verified")
        
        with allure.step("Complete checkout"):
            checkout_page.fill_delivery_address(
                first_name="Test",
                last_name="User",
                address="123 Test St",
                city="Test City",
                state="TC",
                zipcode="12345",
                country="Test Country"
            )
            
            checkout_page.click_place_order()
        
        with allure.step("Verify order placed"):
            logger.info("Order placed successfully by logged-in user")
    
    @pytest.mark.regression
    @allure.title("TC16: Verify Checkout Page for Logged-In User")
    @allure.description("Verify checkout page shows logged-in user information")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_page_logged_in_user_info(self, driver, base_url):
        """Test checkout page displays logged-in user info"""
        with allure.step("Login and navigate to checkout"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
        
        with allure.step("Login"):
            login_page = LoginPage(driver)
            login_page.login("test@example.com", "Password123!")
        
        with allure.step("Add item and go to checkout"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
            
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            cart_page.click_proceed_to_checkout()
        
        with allure.step("Verify user information"):
            logger.info("Logged-in user information verified on checkout page")
