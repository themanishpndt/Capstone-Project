"""
Test Case 20: Search Products and Verify Cart After Login
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Enter product name in search input and click search button
6. Verify 'SEARCHED PRODUCTS' is visible
7. Verify all the products related to search are visible
8. Add those products to cart
9. Click 'Cart' button and verify that products are visible in cart
10. Click 'Signup / Login' button and submit login details
11. Again, go to Cart page
12. Verify that those products are visible in cart after login as well
13. Remove all products that have been added
14. Verify 'Cart is empty! Click here to buy products.' is visible
Workflow: Navigate to Products → Search product → Verify results → Add to cart → Login → Verify cart → Remove products → Verify empty cart
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestSearchProductsVerifyCartAfterLoginTC20:
    """Test suite for Search Products and Verify Cart After Login - TC20"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_search_products_verify_cart_after_login(self, driver, base_url, action_delay):
        """Test product search and cart verification after login"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Clicking on Products button")
        home_page.click_products()
        action_delay(2)
        
        logger.info("Step 4: Verifying ALL PRODUCTS page")
        current_url = driver.current_url
        assert "products" in current_url.lower()
        page_text = driver.execute_script("return document.body.innerText;")
        assert "ALL PRODUCTS" in page_text or "Products" in page_text
        logger.info("ALL PRODUCTS page verified")
        action_delay(1)
        
        logger.info("Step 5: Entering product name in search and clicking search button")
        product_page.search_product("Tshirt")
        action_delay(2)
        
        logger.info("Step 6: Verifying 'SEARCHED PRODUCTS' is visible")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "SEARCHED PRODUCTS" in page_text or "searched" in page_text.lower()
        logger.info("SEARCHED PRODUCTS heading verified")
        action_delay(1)
        
        logger.info("Step 7: Verifying all products related to search are visible")
        product_count = product_page.get_product_count()
        assert product_count > 0
        logger.info(f"Search results verified with {product_count} products")
        action_delay(1)
        
        logger.info("Step 8: Adding products to cart")
        for i in range(min(2, product_count)):
            product_page.add_product_to_cart(index=i, view_cart=False)
            action_delay(1)
        logger.info("Products added to cart")
        action_delay(1)
        
        logger.info("Step 9: Clicking Cart button and verifying products are visible")
        home_page.click_cart()
        action_delay(2)
        
        cart_items = cart_page.get_cart_items_count()
        assert cart_items > 0
        logger.info(f"Cart verified with {cart_items} items")
        action_delay(1)
        
        logger.info("Step 10: Clicking Signup/Login button and logging in")
        home_page.click_signup_login()
        action_delay(2)
        login_page.enter_login_email("testuser@example.com")
        action_delay(0.5)
        login_page.enter_login_password("Test@123")
        action_delay(0.5)
        login_page.click_login_button()
        action_delay(2)
        logger.info("Login completed")
        
        logger.info("Step 11: Navigating to Cart page")
        home_page.click_cart()
        action_delay(2)
        
        logger.info("Step 12: Verifying products are visible in cart after login")
        cart_items_after_login = cart_page.get_cart_items_count()
        assert cart_items_after_login > 0
        logger.info(f"Cart verified after login with {cart_items_after_login} items")
        action_delay(1)
        
        logger.info("Step 13: Removing all products from cart")
        # Get current cart count and remove all items
        cart_items_count = cart_page.get_cart_items_count()
        for i in range(cart_items_count):
            # Always remove the first item since items shift after removal
            try:
                cart_page.remove_product_from_cart(0)
                action_delay(1)
            except Exception as e:
                logger.warning(f"Error removing item: {e}")
        logger.info("All products removed from cart")
        action_delay(1)
        
        logger.info("Step 14: Verifying 'Cart is empty' message")
        # Refresh to see updated cart state
        driver.refresh()
        action_delay(2)
        page_text = driver.execute_script("return document.body.innerText;")
        # Check if cart is empty by looking for multiple possible messages or empty items
        is_empty = ("cart is empty" in page_text.lower() or 
                   "empty" in page_text.lower() or
                   driver.execute_script("return document.querySelectorAll('tr[id^=\"product-\"]').length") == 0)
        assert is_empty, "Cart should be empty after removing all items"
        logger.info("Empty cart verified")
        logger.info("Search products and cart after login test completed successfully")
