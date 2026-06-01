"""
Test Case 2: Login User with correct email and password
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
Workflow: Create account → Logout → Login → Verify logged in
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
        """Test login with valid email and password
        
        Steps:
        1. Navigate to home page
        2. Click Signup/Login
        3. Register new account with test credentials
        4. Verify account created
        5. Logout
        6. Login with same credentials
        7. Verify logged in message
        """
        
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Step 1-3: Navigate and sign up with test credentials (use unique email)
        logger.info("Step 1-2: Navigating to home and clicking Signup/Login")
        home_page.navigate_to_home()
        action_delay(1)
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Step 3: Registering new account")
        test_email = f"testuser_{int(__import__('time').time())}@example.com"
        test_password = "TestPass123!"
        
        login_page.enter_signup_name("Test User")
        action_delay(0.5)
        login_page.enter_signup_email(test_email)
        action_delay(1)
        login_page.click_signup_button()
        action_delay(2)
        
        # Step 4: Fill account info and create account
        logger.info("Step 4: Filling account information and creating account")
        assert login_page.is_account_info_visible(), "Account info section not visible"
        action_delay(1)
        
        login_page.select_title_mr()
        action_delay(0.5)
        login_page.enter_reg_name("Test User")
        action_delay(0.5)
        login_page.enter_reg_password(test_password)
        action_delay(1)
        login_page.select_date_of_birth("15", "5", "1990")
        action_delay(1)
        login_page.check_newsletter()
        action_delay(0.5)
        login_page.check_special_offers()
        action_delay(1)
        
        # Fill address info
        login_page.enter_first_name("Test")
        action_delay(0.5)
        login_page.enter_last_name("User")
        action_delay(0.5)
        login_page.enter_company("Test Company")
        action_delay(0.5)
        login_page.enter_address("123 Test Street")
        action_delay(0.5)
        login_page.enter_address2("Apt 456")
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
        
        # Step 5: Logout
        logger.info("Step 5: Clicking Continue and then Logout")
        login_page.click_continue()
        action_delay(2)
        
        logger.info("Logging out")
        home_page.click_logout()
        action_delay(2)
        
        # Step 6-8: Login again with same credentials
        logger.info("Step 6: Logging in with same credentials")
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Entering email and password")
        login_page.navigate_to_login()
        action_delay(1)
        login_page.enter_email(test_email)
        action_delay(0.5)
        login_page.enter_password(test_password)
        action_delay(1)
        
        logger.info("Step 7: Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        logger.info("Step 8: Verifying login success")
        is_success = login_page.is_logged_in_visible()
        assert is_success, "Login was not successful - 'Logged in as' message not visible"
        
        logger.info("Login test completed successfully")
