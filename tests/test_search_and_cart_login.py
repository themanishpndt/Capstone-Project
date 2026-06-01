"""
Test Case 20: Search Products and Verify Cart After Login
Verify search functionality and cart persistence after login
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestSearchProductsAndCartAfterLogin:
    """Test suite for search and cart after login"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC20: Search Products and Verify Cart After Login")
    @allure.description("Verify that products can be searched and cart is preserved after login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_product_and_cart_after_login(self, driver, base_url):
        """Test search and cart verification after login"""
        with allure.step("Navigate to products and search"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            product_page.search_product("Blue Top")
        
        with allure.step("Add searched product to cart"):
            add_to_cart_buttons = product_page.find_elements(
                product_page.locators.ADD_TO_CART_BUTTON
            )
            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
        
        with allure.step("Login to account"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
            
            login_page = LoginPage(driver)
            login_page.login("test@example.com", "Password123!")
        
        with allure.step("Navigate to cart and verify product"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            
            product_count = cart_page.get_cart_items_count()
            assert product_count > 0, "Cart should contain searched product after login"
            logger.info(f"Cart contains {product_count} items after login")
    
    @pytest.mark.regression
    @allure.title("TC20: Multiple Product Search")
    @allure.description("Verify search works for multiple different products")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("search_term", [
        "Top",
        "Saree",
        "Dress"
    ])
    def test_multiple_product_searches(self, driver, base_url, search_term):
        """Test searching for multiple products"""
        with allure.step(f"Search for '{search_term}'"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            
            product_page.search_product(search_term)
        
        with allure.step("Verify search results"):
            product_count = product_page.get_product_count()
            assert product_count > 0, f"No products found for '{search_term}'"
            logger.info(f"Found {product_count} products for '{search_term}'")
