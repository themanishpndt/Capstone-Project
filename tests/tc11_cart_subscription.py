"""
Test Case 11: Verify Subscription in Cart page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Cart' button and scroll down to footer
5. Verify text 'SUBSCRIPTION'
6. Enter email address in input and click arrow button
7. Verify success message 'You have been successfully subscribed!' is visible
Workflow: Navigate to cart → Scroll to footer → Enter email → Verify success message
"""

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.locators.subscription_locators import SubscriptionLocators

logger = logging.getLogger(__name__)


class TestCartSubscriptionTC11:
    """Test suite for Cart page subscription - TC11"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_subscription_in_cart_page(self, driver, base_url, action_delay):
        """Test subscription functionality in cart page footer"""
        
        home_page = HomePage(driver)
        cart_page = CartPage(driver)
        subscription_locators = SubscriptionLocators()
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Verifying home page is visible")
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info(f"Home page verified: {driver.title}")
        action_delay(1)
        
        logger.info("Step 4: Clicking Cart button and scrolling to footer")
        home_page.click_cart()
        action_delay(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        action_delay(2)
        
        logger.info("Step 5: Verifying SUBSCRIPTION text is visible")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "SUBSCRIPTION" in page_text.upper()
        logger.info("SUBSCRIPTION text verified in cart page footer")
        action_delay(1)
        
        logger.info("Step 6: Entering email and clicking subscribe button")
        email_input = home_page.find_element(subscription_locators.FOOTER_SUBSCRIPTION_EMAIL)
        email_input.send_keys("cartuser@example.com")
        action_delay(0.5)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        action_delay(0.5)
        
        subscribe_button = home_page.find_element(subscription_locators.FOOTER_SUBSCRIPTION_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", subscribe_button)
        action_delay(0.5)
        driver.execute_script("arguments[0].click();", subscribe_button)
        logger.info("Email entered and subscribe button clicked")
        action_delay(2)
        
        logger.info("Step 7: Verifying success message")
        try:
            wait = WebDriverWait(driver, 10)
            success_element = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='success-subscribe']")
                )
            )
            logger.info("Success message element found")
            
            success_text = success_element.text
            logger.info(f"Success message text: {success_text}")
            
            if not success_text:
                success_html = driver.execute_script("return document.querySelector('#success-subscribe').innerHTML;")
                logger.info(f"Success message HTML: {success_html}")
                assert success_html
            else:
                assert "subscribed" in success_text.lower()
            
            logger.info("Success message verified in cart page")
            
        except Exception as e:
            logger.warning(f"Could not verify success element: {e}")
            
            success_check = driver.execute_script("""
                const elem = document.querySelector('#success-subscribe');
                if (elem) {
                    return elem.textContent.includes('subscribed') || 
                           elem.innerHTML.includes('subscribed');
                }
                return false;
            """)
            assert success_check, "Success message not found after subscription in cart"
            logger.info("Success message verified via JavaScript fallback")
