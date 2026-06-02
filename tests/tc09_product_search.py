"""
Test Case 9: Search Product
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible
Workflow: Navigate to home → Click Products → Search product → Verify SEARCHED PRODUCTS
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage

logger = logging.getLogger(__name__)


class TestProductSearchTC09:
    """Test suite for Product Search - TC09"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_search_product(self, driver, base_url, action_delay):
        """Test product search functionality"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Verifying home page is visible")
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info(f"Home page verified: {driver.title}")
        action_delay(1)
        
        logger.info("Step 4: Clicking on Products button")
        home_page.click_products()
        action_delay(2)
        
        logger.info("Step 5: Verifying ALL PRODUCTS page")
        current_url = driver.current_url
        assert "products" in current_url.lower()
        logger.info("ALL PRODUCTS page verified")
        action_delay(1)
        
        logger.info("Step 6: Searching for product")
        search_term = "Tshirts"
        product_page.search_product(search_term)
        action_delay(2)
        
        logger.info("Step 7: Verifying SEARCHED PRODUCTS heading")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "SEARCHED PRODUCTS" in page_text.upper()
        logger.info("SEARCHED PRODUCTS heading verified")
        action_delay(1)
        
        logger.info("Step 8: Verifying search results")
        products_count = product_page.get_product_count()
        assert products_count > 0
        logger.info(f"Search results verified: {products_count} products found for '{search_term}'")
        logger.info("Product search test completed successfully")
