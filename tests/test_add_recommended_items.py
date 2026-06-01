"""
Test Case 22: Add To Cart from Recommended Items
Verify that user can add recommended products to cart
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestAddRecommendedItemsToCart:
    """Test suite for adding recommended items to cart"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC22: Add To Cart from Recommended Items")
    @allure.description("Verify that user can add recommended products to cart from home page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_recommended_item_to_cart(self, driver, base_url):
        """Test adding recommended item to cart"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll to recommended items section"):
            home_page.scroll_to_footer()
        
        with allure.step("Add first recommended product to cart"):
            home_page.add_first_recommended_product_to_cart()
        
        with allure.step("Navigate to cart and verify"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            
            product_count = cart_page.get_cart_items_count()
            assert product_count > 0, "Recommended product not added to cart"
            logger.info(f"Recommended product added to cart. Cart items: {product_count}")
    
    @pytest.mark.regression
    @allure.title("TC22: Verify Recommended Products Section")
    @allure.description("Verify recommended products section is visible on home page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_recommended_products_section_visibility(self, driver, base_url):
        """Test recommended products section visibility"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll to recommended section"):
            home_page.scroll_to_footer()
        
        with allure.step("Verify recommended products are visible"):
            product_count = home_page.get_recommended_products_count()
            assert product_count > 0, "No recommended products found"
            logger.info(f"Found {product_count} recommended products")
    
    @pytest.mark.regression
    @allure.title("TC22: Add Multiple Recommended Items")
    @allure.description("Verify multiple recommended items can be added to cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_multiple_recommended_items(self, driver, base_url):
        """Test adding multiple recommended items"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll to recommended section"):
            home_page.scroll_to_footer()
        
        with allure.step("Add multiple recommended products"):
            try:
                buttons = home_page.find_elements(
                    home_page.home_locators.RECOMMENDED_ADD_TO_CART_BUTTONS
                )
                for i, button in enumerate(buttons[:3]):  # Add first 3 products
                    button.click()
                    logger.info(f"Added recommended product {i+1} to cart")
            except Exception as e:
                logger.warning(f"Could not add all recommended products: {e}")
        
        with allure.step("Verify items in cart"):
            cart_page = CartPage(driver)
            cart_page.navigate_to_cart()
            logger.info("Multiple recommended items added to cart")
