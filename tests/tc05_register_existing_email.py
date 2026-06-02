"""
Test Case 5: Register User with existing email
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible
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
        
        logger.info("Step 1: Navigating to home")
        home_page.navigate_to_home()
        action_delay(1)
        
        logger.info("Step 2: Clicking Signup/Login")
        home_page.click_signup_login()
        action_delay(2)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(0.5)
        
        logger.info("Step 3: Creating first account")
        unique_email = f"testuser_{int(__import__('time').time())}@example.com"
        
        login_page.enter_signup_name("Test User")
        action_delay(0.5)
        login_page.enter_signup_email(unique_email)
        action_delay(1)
        login_page.click_signup_button()
        action_delay(2)
        
        logger.info("Step 4: Filling account information")
        assert login_page.is_account_info_visible()
        action_delay(1)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(0.5)
        
        login_page.select_title_mr()
        action_delay(0.5)
        login_page.enter_reg_name("Test User")
        action_delay(0.5)
        login_page.enter_reg_password("TestPass123!")
        action_delay(1)
        login_page.select_date_of_birth("15", "5", "1990")
        action_delay(1)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
        action_delay(0.5)
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
        
        logger.info("Step 5: Creating account")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        action_delay(0.5)
        login_page.click_create_account()
        action_delay(2)
        assert login_page.is_account_created_visible()
        action_delay(1)
        
        logger.info("Step 6: Logging out")
        login_page.click_continue()
        action_delay(3)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(1)
        home_page.click_logout()
        action_delay(2)
        
        logger.info("Step 7: Attempting to register with same email")
        home_page.click_signup_login()
        action_delay(2)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(0.5)
        
        login_page.enter_signup_name("Test User 2")
        action_delay(0.5)
        login_page.enter_signup_email(unique_email)
        action_delay(1)
        login_page.click_signup_button()
        action_delay(2)
        
        logger.info("Step 8: Verifying error message")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0
        logger.info(f"Error message: {error_message}")
        logger.info("Existing email test completed successfully")
