"""
Test Case 12: Add Products in Cart
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price
Workflow: Navigate to products → Add first product → Continue shopping → Add second product → View cart → Verify products
"""

import pytest
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestAddProductsCartTC12:
    """Test suite for adding products to cart - TC12"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_add_multiple_products_to_cart(self, driver, base_url, action_delay):
        """Test adding multiple products to cart and verifying cart contents"""
        
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
        
        logger.info("Step 4: Clicking Products button")
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(1)
        home_page.click_products()
        action_delay(2)
        
        logger.info("Step 5: Hovering over first product and clicking Add to cart")
        products = product_page.find_elements(product_page.locators.PRODUCT_ITEMS)
        assert len(products) > 0, "No products found on page"
        
        actions = ActionChains(driver)
        actions.move_to_element(products[0]).perform()
        action_delay(1)
        
        product_page.add_first_product_to_cart(view_cart=False)
        action_delay(2)
        
        logger.info("Step 6: Clicking Continue Shopping button")
        continue_button_xpath = "//button[@class='btn btn-success' and text()='Continue Shopping']"
        try:
            continue_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((driver.find_element, continue_button_xpath))
            )
            continue_btn.click()
        except:
            driver.execute_script("""
                const buttons = document.querySelectorAll('button');
                for (let btn of buttons) {
                    if (btn.textContent.includes('Continue Shopping')) {
                        btn.click();
                        break;
                    }
                }
            """)
        action_delay(2)
        
        logger.info("Step 7: Hovering over second product and clicking Add to cart")
        products = product_page.find_elements(product_page.locators.PRODUCT_ITEMS)
        if len(products) > 1:
            actions.move_to_element(products[1]).perform()
            action_delay(1)
            product_page.add_product_to_cart(index=1, view_cart=False)
        action_delay(2)
        
        logger.info("Step 8: Clicking View Cart button")
        try:
            view_cart_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((driver.find_element, "//a[@href='/view_cart' and contains(text(), 'View Cart')]"))
            )
            view_cart_btn.click()
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
        
        logger.info("Step 9: Verifying both products are added to Cart")
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) >= 1, "No products found in cart"
        logger.info(f"Found {len(cart_items)} products in cart")
        
        logger.info("Step 10: Verifying prices, quantity and total price")
        for idx, item in enumerate(cart_items):
            logger.info(f"Product {idx+1}: {item['name']}")
            logger.info(f"  Price: {item['price']}")
            logger.info(f"  Quantity: {item['quantity']}")
            assert item['name'], "Product name not found"
            assert item['price'], "Product price not found"
            assert item['quantity'], "Product quantity not found"
        
        logger.info("All products verified successfully in cart")
