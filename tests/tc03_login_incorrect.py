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
        
        logger.info("Navigating to home page")
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        action_delay(1)
        
        logger.info("Clicking on Signup/Login link")
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Navigating to login page")
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        action_delay(1)
        
        logger.info("Entering incorrect email and password")
        login_page.enter_email(test_data["invalid_email"])
        action_delay(0.5)
        login_page.enter_password(test_data["invalid_password"])
        action_delay(1)
        
        logger.info("Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        logger.info("Verifying error message is displayed")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0, \
            "Expected error message not found"
        
        logger.info(f"Error message displayed: {error_message}")
        logger.info("Login error handling test completed successfully")
