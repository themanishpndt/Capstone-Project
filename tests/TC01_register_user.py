"""
Test Case 1: Register User
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
Complete registration flow with account creation and deletion
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestRegisterUserTC01:
    """Test suite for user registration - TC01"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_register_user(self, driver, base_url, action_delay):
        """Test complete user registration workflow"""
        
        # Steps 1-7: Navigate and enter signup details
        logger.info("Step 1-2: Navigating to home page")
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        action_delay(1)
        
        logger.info("Step 4: Clicking on Signup/Login link")
        home_page.click_signup_login()
        action_delay(2)
        
        logger.info("Step 6: Entering signup information")
        login_page = LoginPage(driver)
        signup_email = f"testuser_{int(__import__('time').time())}@example.com"
        login_page.enter_signup_name("Test User")
        action_delay(0.5)
        login_page.enter_signup_email(signup_email)
        action_delay(1)
        
        logger.info("Step 7: Clicking Signup button")
        login_page.click_signup_button()
        action_delay(2)
        
        # Step 8: Verify ENTER ACCOUNT INFORMATION is visible
        logger.info("Step 8: Verifying ENTER ACCOUNT INFORMATION section")
        assert login_page.is_account_info_visible(), \
            "ENTER ACCOUNT INFORMATION section not visible"
        action_delay(1)
        
        # Steps 9-11: Fill account information
        logger.info("Step 9: Filling account information")
        login_page.select_title_mr()
        action_delay(0.5)
        login_page.enter_reg_name("Test User")
        action_delay(0.5)
        login_page.enter_reg_password("TestPass123!")
        action_delay(0.5)
        login_page.select_date_of_birth("15", "05", "1990")
        action_delay(1)
        
        logger.info("Step 10: Checking newsletter checkbox")
        login_page.check_newsletter()
        action_delay(0.5)
        
        logger.info("Step 11: Checking special offers checkbox")
        login_page.check_special_offers()
        action_delay(1)
        
        # Step 12: Fill address information
        logger.info("Step 12: Filling address information")
        login_page.enter_first_name("Test")
        action_delay(0.3)
        login_page.enter_last_name("User")
        action_delay(0.3)
        login_page.enter_company("Test Company")
        action_delay(0.3)
        login_page.enter_address("123 Test Street")
        action_delay(0.3)
        login_page.enter_address2("Apt 456")
        action_delay(0.3)
        login_page.select_country("United States")
        action_delay(0.3)
        login_page.enter_state("Texas")
        action_delay(0.3)
        login_page.enter_city("Houston")
        action_delay(0.3)
        login_page.enter_zipcode("77001")
        action_delay(0.3)
        login_page.enter_mobile_number("1234567890")
        action_delay(1)
        
        # Step 13: Click Create Account button
        logger.info("Step 13: Clicking Create Account button")
        login_page.click_create_account()
        action_delay(2)
        
        # Step 14: Verify ACCOUNT CREATED message
        logger.info("Step 14: Verifying ACCOUNT CREATED message")
        assert login_page.is_account_created_visible(), \
            "ACCOUNT CREATED message not visible"
        action_delay(1)
        
        # Step 15: Click Continue button
        logger.info("Step 15: Clicking Continue button")
        login_page.click_continue()
        action_delay(2)
        
        # Step 16: Verify Logged in as message
        logger.info("Step 16: Verifying 'Logged in as' message")
        assert login_page.is_logged_in_visible(), \
            "'Logged in as' message not visible"
        action_delay(1)
        
        # Step 17: Click Delete Account button
        logger.info("Step 17: Clicking Delete Account button")
        login_page.click_delete_account()
        action_delay(2)
        
        # Step 18: Verify ACCOUNT DELETED message
        logger.info("Step 18: Verifying ACCOUNT DELETED message")
        assert login_page.is_account_deleted_visible(), \
            "ACCOUNT DELETED message not visible"
        action_delay(1)
        
        logger.info("Complete registration and deletion test passed")
