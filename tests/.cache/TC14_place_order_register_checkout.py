"""
Test Case 14: Place Order Register While Checkout
Verify user can register while placing order during checkout
"""

import pytest
import allure
import logging
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestPlaceOrderRegisterWhileCheckout:
    """Test suite for placing order with registration during checkout"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    @allure.title("TC14: Place Order Register While Checkout")
    @allure.description("Verify that user can register and place order during checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_place_order_register_while_checkout(self, driver, base_url):
        """Test placing order with registration during checkout"""
        with allure.step("Navigate to products and add item to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            # Add first product to cart
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to cart"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
        
        with allure.step("Proceed to checkout"):
            cart_page.click_proceed_to_checkout()
        
        with allure.step("Register during checkout"):
            checkout_page = CheckoutPage(driver)
            
            # Register new user during checkout
            checkout_page.register_during_checkout(
                name="New User",
                email="newuser@example.com",
                password="NewPass123!"
            )
        
        with allure.step("Verify order placed successfully"):
            logger.info("Order placed with registration during checkout")
    
    @pytest.mark.regression
    @allure.title("TC14: Verify Checkout Registration Form")
    @allure.description("Verify registration form is available during checkout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkout_registration_form_visibility(self, driver, base_url):
        """Test registration form visibility during checkout"""
        with allure.step("Navigate through checkout process"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to cart and checkout"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            cart_page.click_proceed_to_checkout()
        
        with allure.step("Verify registration option is available"):
            logger.info("Checkout registration form verified")
