"""
Test Case 5: Register User with existing email
Workflow: Create account with email → Try to register with same email → Verify error
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
        
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Step 1: Create an account first
        logger.info("Step 1-2: Navigating to home and clicking Signup/Login")
        home_page.navigate_to_home()
        action_delay(1)
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Step 3: Creating a new account with unique email")
        # Generate unique email for this test
        unique_email = f"testuser_{int(__import__('time').time())}@example.com"
        
        login_page.enter_signup_name("Test User")
        action_delay(0.5)
        login_page.enter_signup_email(unique_email)
        action_delay(1)
        login_page.click_signup_button()
        action_delay(2)
        
        # Step 2: Complete account creation
        logger.info("Step 4: Completing account creation")
        assert login_page.is_account_info_visible(), "Account info section not visible"
        action_delay(1)
        
        login_page.select_title_mr()
        action_delay(0.5)
        login_page.enter_reg_name("Test User")
        action_delay(0.5)
        login_page.enter_reg_password("TestPass123!")
        action_delay(1)
        login_page.select_date_of_birth("15", "5", "1990")
        action_delay(1)
        
        # Fill minimal address info
        login_page.enter_first_name("Test")
        action_delay(0.5)
        login_page.enter_last_name("User")
        action_delay(0.5)
        login_page.enter_address("123 Test Street")
        action_delay(0.5)
        login_page.select_country("United States")
        action_delay(0.5)
        login_page.enter_state("Texas")
        action_delay(0.5)
        login_page.enter_city("Houston")
        action_delay(0.5)
        login_page.enter_zipcode("77001")
        action_delay(0.5)
        login_page.enter_mobile_number("1234567890")
        action_delay(1)
        
        logger.info("Creating account")
        login_page.click_create_account()
        action_delay(2)
        
        assert login_page.is_account_created_visible(), "Account not created"
        action_delay(1)
        
        # Step 3: Logout and logout to clear session
        logger.info("Step 5: Logging out")
        login_page.click_continue()
        action_delay(2)
        home_page.click_logout()
        action_delay(2)
        
        # Step 4: Try to register with the same email
        logger.info("Step 6: Attempting to register with the same email")
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Entering name and already registered email")
        login_page.enter_signup_name("Test User 2")
        action_delay(0.5)
        login_page.enter_signup_email(unique_email)  # Using the email we just created
        action_delay(1)
        
        logger.info("Clicking Signup button")
        login_page.click_signup_button()
        action_delay(2)
        
        # Step 5: Verify error message
        logger.info("Step 7: Verifying error message for existing email")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0, \
            "Expected error message for existing email not found"
        
        logger.info(f"Error message displayed: {error_message}")
        logger.info("Register with existing email test completed successfully")
