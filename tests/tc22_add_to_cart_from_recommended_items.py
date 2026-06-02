"""
Test Case 22: Add to cart from Recommended items
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Scroll to bottom of page
4. Verify 'RECOMMENDED ITEMS' are visible
5. Click on 'Add To Cart' on Recommended product
6. Click on 'View Cart' button
7. Verify that product is displayed in cart page
Workflow: Navigate home → Scroll to bottom → Verify recommended items → Add to cart → View cart → Verify product in cart
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.scroll_page import ScrollPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestAddToCartFromRecommendedItemsTC22:
    """Test suite for Add to cart from Recommended items - TC22"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_add_to_cart_from_recommended_items(self, driver, base_url, action_delay):
        """Test adding recommended items to cart"""
        
        home_page = HomePage(driver)
        scroll_page = ScrollPage(driver)
        cart_page = CartPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Scrolling to bottom of page")
        scroll_page.scroll_down_to_bottom()
        action_delay(2)
        
        logger.info("Step 4: Verifying 'RECOMMENDED ITEMS' are visible")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "RECOMMENDED" in page_text or "recommended" in page_text.lower()
        logger.info("RECOMMENDED ITEMS section verified")
        action_delay(1)
        
        logger.info("Step 5: Clicking on 'Add To Cart' on Recommended product")
        # Find and click the first recommended item's add to cart button
        recommended_add_buttons = driver.execute_script(
            """
            let buttons = [];
            let elements = document.querySelectorAll('[class*="recommended"], [id*="recommended"]');
            elements.forEach(el => {
                let addBtn = el.querySelector('a[data-product-id], button[class*="cart"], a[class*="cart"]');
                if(addBtn) buttons.push(addBtn);
            });
            return buttons.length;
            """
        )
        
        if recommended_add_buttons > 0:
            driver.execute_script(
                """
                let elements = document.querySelectorAll('[class*="recommended"], [id*="recommended"]');
                elements.forEach(el => {
                    let addBtn = el.querySelector('a[data-product-id], button[class*="cart"], a[class*="cart"]');
                    if(addBtn) addBtn.click();
                });
                """
            )
            logger.info("Clicked Add To Cart on recommended product")
        action_delay(2)
        
        # Handle modal if it appears
        try:
            modal_button = driver.find_element(*cart_page.locators.CART_MODAL_VIEW_CART_LINK) if hasattr(cart_page, 'locators') else None
            if modal_button:
                modal_button.click()
                action_delay(1)
        except:
            pass
        
        logger.info("Step 6: Clicking on 'View Cart' button")
        home_page.click_cart()
        action_delay(2)
        
        logger.info("Step 7: Verifying that product is displayed in cart page")
        cart_items = cart_page.get_cart_items_count()
        assert cart_items > 0
        logger.info(f"Product verified in cart with {cart_items} items")
        logger.info("Add to cart from recommended items test completed successfully")
