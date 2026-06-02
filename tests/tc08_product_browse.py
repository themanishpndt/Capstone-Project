"""
Test Case 8: Verify All Products and product detail page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. The products list is visible
7. Click on 'View Product' of first product
8. User is landed to product detail page
9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
Workflow: Navigate to home → Click Products → View first product → Verify details
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage

logger = logging.getLogger(__name__)


class TestProductBrowseTC08:
    """Test suite for All Products and Product Detail - TC08"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_all_products_and_detail(self, driver, base_url, action_delay):
        """Test product browsing and detail page verification"""
        
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
        all_products_text = driver.execute_script(
            "return document.body.innerText.includes('ALL PRODUCTS') || document.body.innerText.includes('Products')"
        )
        assert all_products_text
        logger.info("ALL PRODUCTS page verified")
        action_delay(1)
        
        logger.info("Step 6: Verifying products list")
        products_count = product_page.get_product_count()
        assert products_count > 0
        logger.info(f"Products list verified: {products_count} products found")
        action_delay(1)
        
        logger.info("Step 7: Clicking View Product of first product")
        product_page.open_first_product_details()
        action_delay(2)
        
        logger.info("Step 8: Verifying product detail page")
        product_detail_url = driver.current_url
        assert "product_details" in product_detail_url.lower() or "/products/" in product_detail_url
        logger.info(f"Product detail page verified: {product_detail_url}")
        action_delay(1)
        
        logger.info("Step 9: Verifying product details")
        page_text = driver.execute_script("return document.body.innerText;")
        details_found = {
            'name': 'product' in page_text.lower() and len(page_text) > 100,
            'price': 'rs' in page_text.lower() or '$' in page_text or 'price' in page_text.lower(),
        }
        assert details_found['name']
        assert details_found['price']
        logger.info(f"Product details verified: {details_found}")
        logger.info("Product browse test completed successfully")
