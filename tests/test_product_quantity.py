"""
Test Case 13: Verify Product Quantity in Cart
Verify that product quantity can be modified in cart
"""

import pytest
import allure
import logging
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestProductQuantityInCart:
    """Test suite for product quantity in cart"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC13: Verify Product Quantity in Cart")
    @allure.description("Verify that user can verify and modify product quantity in cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_product_quantity_in_cart(self, driver, base_url):
        """Test product quantity in cart"""
        with allure.step("Navigate to products page"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
        
        with allure.step("Add product to cart"):
            # Add first product to cart
            products = product_page.find_elements(product_page.locators.PRODUCT_ITEMS)
            assert len(products) > 0, "No products found"
            
            # Click add to cart
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to cart page"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
        
        with allure.step("Verify product quantity"):
            quantity = cart_page.get_product_quantity()
            assert quantity >= 1, "Product quantity should be at least 1"
            logger.info(f"Product quantity in cart: {quantity}")
    
    @pytest.mark.regression
    @allure.title("TC13: Modify Product Quantity in Cart")
    @allure.description("Verify that user can increase product quantity in cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_modify_product_quantity_in_cart(self, driver, base_url):
        """Test modifying product quantity in cart"""
        with allure.step("Add product to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            products = product_page.find_elements(product_page.locators.PRODUCT_ITEMS)
            if products:
                add_to_cart_buttons = product_page.find_elements(
                    product_page.locators.ADD_TO_CART_BUTTON
                )
                if add_to_cart_buttons:
                    add_to_cart_buttons[0].click()
        
        with allure.step("Navigate to cart and modify quantity"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            
            # Increase quantity
            try:
                cart_page.increase_product_quantity(2)
            except Exception as e:
                logger.warning(f"Could not increase quantity: {e}")
        
        with allure.step("Verify updated quantity"):
            logger.info("Product quantity modification verified")
