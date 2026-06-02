"""
Test Case 13: Verify Product quantity in Cart
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'View Product' for any product on home page
5. Verify product detail is opened
6. Increase quantity to 4
7. Click 'Add to cart' button
8. Click 'View Cart' button
9. Verify that product is displayed in cart page with exact quantity
Workflow: Navigate to product details → Increase quantity → Add to cart → Verify quantity in cart
"""

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestProductQuantityTC13:
    """Test suite for product quantity in cart - TC13"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_product_quantity_in_cart(self, driver, base_url, action_delay):
        """Test product quantity adjustment and verification in cart"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Verifying home page is visible")
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info(f"Home page verified: {driver.title}")
        action_delay(1)
        
        logger.info("Step 4: Clicking View Product for first product on home page")
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(1)
        
        view_product_links = product_page.find_elements(product_page.locators.VIEW_PRODUCT_LINKS)
        assert len(view_product_links) > 0, "No product links found on home page"
        
        product_page.open_first_product_details()
        action_delay(2)
        
        logger.info("Step 5: Verifying product detail page is opened")
        assert "/product_details/" in driver.current_url, "Product detail page not opened"
        logger.info(f"Product detail page opened: {driver.current_url}")
        action_delay(1)
        
        logger.info("Step 6: Increasing quantity to 4")
        
        quantity_input_locator = (By.NAME, "quantity")
        try:
            quantity_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(quantity_input_locator)
            )
            
            quantity_input.clear()
            action_delay(0.3)
            quantity_input.send_keys("4")
            logger.info("Quantity set to 4")
            action_delay(1)
        except Exception as e:
            logger.warning(f"Could not find quantity input, attempting JavaScript: {e}")
            driver.execute_script("""
                const qty_input = document.querySelector('input[name="quantity"]');
                if (qty_input) {
                    qty_input.value = '4';
                    qty_input.dispatchEvent(new Event('change', { bubbles: true }));
                }
            """)
            action_delay(1)
        
        logger.info("Step 7: Clicking Add to cart button")
        try:
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'Add to cart')]")
                )
            )
            add_to_cart_button.click()
            logger.info("Add to cart button clicked")
        except:
            driver.execute_script("""
                const buttons = document.querySelectorAll('button, a.btn');
                for (let btn of buttons) {
                    if (btn.textContent.includes('Add to cart')) {
                        btn.click();
                        break;
                    }
                }
            """)
        action_delay(2)
        
        logger.info("Step 8: Clicking View Cart button")
        try:
            view_cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(), 'View Cart')]")
                )
            )
            view_cart_link.click()
            logger.info("View Cart button clicked")
        except:
            driver.execute_script("""
                const links = document.querySelectorAll('a');
                for (let link of links) {
                    if (link.textContent.includes('View Cart')) {
                        link.click();
                        break;
                    }
                }
            """)
        action_delay(2)
        
        logger.info("Step 9: Verifying product is displayed in cart with exact quantity")
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) > 0, "No products found in cart"
        
        first_item = cart_items[0]
        logger.info(f"Product in cart: {first_item['name']}")
        logger.info(f"Quantity: {first_item['quantity']}")
        
        quantity_text = first_item['quantity'].strip()
        assert "4" in quantity_text, f"Expected quantity 4, but got {quantity_text}"
        
        logger.info("Product quantity verified successfully in cart with exact quantity 4")
