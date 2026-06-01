"""
Test Case 5: Register User with existing email
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestRegisterExistingEmailTC05:
    """Test suite for register with existing email - TC05"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_register_with_existing_email(self, driver, base_url, action_delay):
        """Test registration with already registered email"""
        
        logger.info("Navigating to home page")
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        action_delay(1)
        
        logger.info("Clicking on Signup/Login link")
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Entering name and already registered email")
        login_page = LoginPage(driver)
        login_page.enter_signup_name("Test User")
        action_delay(0.5)
        # Using an email that should already exist in the system
        login_page.enter_signup_email("test@example.com")
        action_delay(1)
        
        logger.info("Clicking Signup button")
        login_page.click_signup_button()
        action_delay(2)
        
        logger.info("Verifying error message for existing email")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0, \
            "Expected error message for existing email not found"
        
        logger.info(f"Error message displayed: {error_message}")
        logger.info("Register with existing email test completed successfully")
