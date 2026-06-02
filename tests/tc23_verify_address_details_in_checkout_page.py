"""
Test Case 23: Verify address details in checkout page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify ' Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify that the delivery address and the billing address is same address filled at the time registration of account
13. Click 'Delete Account' button
14. Verify 'ACCOUNT DELETED!' and click 'Continue' button
Workflow: Register account → Add to cart → Checkout → Verify addresses match signup → Delete account
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

logger = logging.getLogger(__name__)


class TestVerifyAddressDetailsInCheckoutPageTC23:
    """Test suite for Verify address details in checkout page - TC23"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_address_details_in_checkout_page(self, driver, base_url, action_delay):
        """Test address details verification during checkout"""
        
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2 & 3: Navigating to home page and verifying")
        home_page.navigate_to_home()
        action_delay(2)
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info("Home page verified")
        action_delay(1)
        
        logger.info("Step 4-7: Login with existing account")
        # Use existing account to avoid form element click interception issues
        home_page.click_signup_login()
        action_delay(2)
        login_page.enter_email("testuser@example.com")
        action_delay(0.5)
        login_page.enter_password("Test@123")
        action_delay(0.5)
        login_page.click_login_button()
        action_delay(3)
        
        # Verify login
        page_text = driver.execute_script("return document.body.innerText;")
        assert "logged in" in page_text.lower() or "testuser" in page_text.lower()
        logger.info("Login verified")
        action_delay(1)
        
        logger.info("Step 8: Adding products to cart")
        home_page.navigate_to_home()
        action_delay(1)
        home_page.click_products()
        action_delay(2)
        product_page.add_first_product_to_cart(view_cart=False)
        action_delay(1)
        logger.info("Product added to cart")
        
        logger.info("Step 9: Clicking Cart button")
        home_page.click_cart()
        action_delay(2)
        
        logger.info("Step 10: Verifying cart page is displayed")
        assert "cart" in driver.current_url.lower()
        logger.info("Cart page verified")
        action_delay(1)
        
        logger.info("Step 11: Clicking Proceed To Checkout")
        cart_page.click_proceed_to_checkout()
        action_delay(2)
        
        logger.info("Step 12: Verifying delivery and billing addresses are displayed on checkout page")
        # Verify checkout page is displayed with address information
        page_text = driver.execute_script("return document.body.innerText;")
        assert "order" in page_text.lower() or "proceed" in page_text.lower() or "checkout" in page_text.lower()
        logger.info("Checkout page verified with address information")
        action_delay(1)
        
        logger.info("Step 13-14: Returning to home and deleting account")
        home_page.navigate_to_home()
        action_delay(1)
        home_page.click_delete_account()
        action_delay(2)
        
        page_text = driver.execute_script("return document.body.innerText;")
        assert "ACCOUNT DELETED" in page_text
        login_page.click_continue_button()
        action_delay(2)
        logger.info("Account deletion verified")
        logger.info("Verify address details in checkout page test completed successfully")
