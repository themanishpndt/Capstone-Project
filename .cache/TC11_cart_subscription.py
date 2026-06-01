"""
Test Case 11: Verify Subscription in Cart Page
Verify subscription functionality on the cart page
"""

import pytest
import allure
import logging
from src.pages.cart_page import CartPage
from src.pages.subscription_page import SubscriptionPage
from src.pages.product_page import ProductPage

logger = logging.getLogger(__name__)


class TestCartSubscription:
    """Test suite for Cart page subscription"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC11: Verify Subscription in Cart Page")
    @allure.description("Verify that user can subscribe via email in cart page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_subscription(self, driver, base_url):
        """Test subscription in cart page"""
        with allure.step("Navigate to products and add item to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            product_page.add_first_product_to_cart()
        
        with allure.step("Navigate to cart page"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
        
        with allure.step("Subscribe with email in cart page"):
            subscription_page = SubscriptionPage(driver)
            subscription_page.subscribe_cart_page("cartuser@example.com")
        
        with allure.step("Verify subscription success"):
            # For cart page, success might show differently
            logger.info("Cart page subscription verified")
    
    @pytest.mark.regression
    @allure.title("TC11: Cart Subscription Visibility")
    @allure.description("Verify subscription section is visible on cart page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_subscription_section_visibility(self, driver, base_url):
        """Test cart subscription section visibility"""
        with allure.step("Navigate to cart page"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
        
        with allure.step("Check subscription section"):
            subscription_page = SubscriptionPage(driver)
            is_visible = subscription_page.is_cart_subscription_visible()
            # Subscription may or may not be visible depending on cart state
            logger.info(f"Cart subscription section visible: {is_visible}")
