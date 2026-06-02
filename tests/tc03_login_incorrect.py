"""
Test Case 3: Login User with incorrect email and password
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestLoginIncorrectCredentialsTC03:
    """Test suite for login with incorrect credentials - TC03"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_with_incorrect_credentials(self, driver, base_url, action_delay, test_data):
        """Test login with invalid email and password"""
        
        logger.info("Step 1: Navigating to home page")
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        action_delay(1)
        
        logger.info("Step 2: Clicking Signup/Login")
        home_page.click_signup_login()
        action_delay(2)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(0.5)
        
        logger.info("Step 3: Navigating to login")
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        action_delay(1)
        
        logger.info("Step 4: Entering incorrect credentials")
        login_page.enter_email(test_data["invalid_email"])
        action_delay(0.5)
        login_page.enter_password(test_data["invalid_password"])
        action_delay(1)
        
        logger.info("Step 5: Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        logger.info("Step 6: Verifying error message")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0
        logger.info(f"Error message: {error_message}")
        logger.info("Login error test completed successfully")
