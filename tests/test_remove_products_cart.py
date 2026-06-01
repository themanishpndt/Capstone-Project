"""
Test Case 17: Remove Products From Cart
Verify that user can remove products from cart
"""

import pytest
import allure
import logging
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestRemoveProductsFromCart:
    """Test suite for removing products from cart"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC17: Remove Products From Cart")
    @allure.description("Verify that user can remove products from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_from_cart(self, driver, base_url):
        """Test removing product from cart"""
        with allure.step("Add products to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            # Add 2 products to cart
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if len(add_to_cart_buttons) >= 2:
                add_to_cart_buttons[0].click()
                add_to_cart_buttons[1].click()
        
        with allure.step("Go to cart"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            
            initial_count = cart_page.get_cart_items_count()
            logger.info(f"Initial cart items: {initial_count}")
        
        with allure.step("Remove first product"):
            cart_page.remove_product(0)
        
        with allure.step("Verify product removed"):
            final_count = cart_page.get_cart_items_count()
            assert final_count < initial_count, "Product was not removed from cart"
            logger.info(f"Product removed. New cart count: {final_count}")
    
    @pytest.mark.regression
    @allure.title("TC17: Remove All Products From Cart")
    @allure.description("Verify cart becomes empty when all products are removed")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_all_products_from_cart(self, driver, base_url):
        """Test removing all products from cart"""
        with allure.step("Add product to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to cart and remove product"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            
            cart_page.remove_product(0)
        
        with allure.step("Verify cart is empty"):
            cart_items = cart_page.get_cart_items_count()
            assert cart_items == 0, "Cart should be empty after removing all products"
            logger.info("Cart is empty after removing all products")
    
    @pytest.mark.regression
    @allure.title("TC17: Remove Product Using Delete Button")
    @allure.description("Verify product can be removed using delete/remove button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_product_using_delete_button(self, driver, base_url):
        """Test removing product using delete button"""
        with allure.step("Add product and navigate to cart"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Go to cart"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
        
        with allure.step("Remove using delete button"):
            cart_page.click_remove_product_button(0)
        
        with allure.step("Verify removal"):
            logger.info("Product removed using delete button")
