"""
Test Case 19: View & Cart Brand Products
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify that Brands are visible on left side bar
5. Click on any brand name
6. Verify that user is navigated to brand page and brand products are displayed
7. On left side bar, click on any other brand link
8. Verify that user is navigated to that brand page and can see products
Workflow: Navigate to Products → Verify brands sidebar → Click first brand → Verify brand page → Click second brand → Verify brand page
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.brand_page import BrandPage

logger = logging.getLogger(__name__)


class TestViewCartBrandProductsTC19:
    """Test suite for View & Cart Brand Products - TC19"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_view_cart_brand_products(self, driver, base_url, action_delay):
        """Test brand filtering and product display"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        brand_page = BrandPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Clicking on Products button")
        home_page.click_products()
        action_delay(2)
        
        logger.info("Step 4: Verifying Brands are visible on left sidebar")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "BRANDS" in page_text or "brand" in page_text.lower()
        logger.info("Brands verified on left sidebar")
        action_delay(1)
        
        logger.info("Step 5: Clicking on first brand (Polo)")
        # Use JavaScript to find and click brand
        driver.execute_script("""
            let brands = document.querySelectorAll('.left-sidebar a');
            for(let brand of brands) {
                if(brand.textContent.includes('Polo')) {
                    brand.click();
                    break;
                }
            }
        """)
        action_delay(2)
        
        logger.info("Step 6: Verifying user is navigated to brand page and products are displayed")
        current_url = driver.current_url
        page_text = driver.execute_script("return document.body.innerText;")
        assert "polo" in current_url.lower() or "brand" in current_url.lower()
        product_count = product_page.get_product_count()
        assert product_count > 0
        logger.info(f"Brand page verified with {product_count} products")
        action_delay(1)
        
        logger.info("Step 7: Clicking on another brand (H&M)")
        # Use JavaScript to find and click brand
        driver.execute_script("""
            let brands = document.querySelectorAll('.left-sidebar a');
            for(let brand of brands) {
                if(brand.textContent.includes('H&M') || brand.textContent.includes('H & M')) {
                    brand.click();
                    break;
                }
            }
        """)
        action_delay(2)
        
        logger.info("Step 8: Verifying user is navigated to that brand page and products are displayed")
        current_url = driver.current_url
        assert "h&m" in current_url.lower() or "brand" in current_url.lower() or "hm" in current_url.lower()
        product_count = product_page.get_product_count()
        assert product_count > 0
        logger.info(f"Second brand page verified with {product_count} products")
        logger.info("View and cart brand products test completed successfully")
