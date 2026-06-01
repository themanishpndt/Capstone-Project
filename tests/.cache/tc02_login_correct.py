"""
Test Case 2: Login User with correct email and password
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestLoginCorrectCredentialsTC02:
    """Test suite for login with correct credentials - TC02"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_with_correct_credentials(self, driver, base_url, action_delay, test_data):
        """Test login with valid email and password"""
        
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
        
        logger.info("Entering correct email and password")
        login_page.enter_email(test_data["valid_email"])
        action_delay(0.5)
        login_page.enter_password(test_data["valid_password"])
        action_delay(1)
        
        logger.info("Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        logger.info("Verifying login success")
        is_success = login_page.is_login_success_message_visible()
        assert is_success, "Login was not successful"
        
        logger.info("Login test completed successfully")
