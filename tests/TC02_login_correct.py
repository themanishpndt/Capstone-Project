"""
Test Case 2: Login User with correct email and password
Test Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Navigate to login page
6. Enter correct email address and password
7. Click 'login' button
8. Verify login was successful
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestLoginUserCorrectCredentials:
    """Test suite for user login with correct credentials"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_with_correct_email_and_password(self, driver, base_url, action_delay, test_data):
        """Test login functionality with valid email and password"""
        
        # Step 1-2: Launch browser and navigate to URL
        logger.info("Step 1-2: Launching browser and navigating to home page")
        home_page = HomePage(driver)
        home_page.navigate_to_home()
        action_delay(1)
        
        # Step 3: Verify that home page is visible successfully
        logger.info("Step 3: Verifying home page is loaded")
        assert home_page.verify_home_page_loaded(), \
            "Home page not loaded properly"
        action_delay(1)
        
        # Step 4: Click on 'Signup / Login' button
        logger.info("Step 4: Clicking on Signup/Login button")
        home_page.click_signup_login()
        action_delay(2)
        
        # Step 5: Navigate to login page
        logger.info("Step 5: Navigating to login page")
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        action_delay(1)
        
        # Step 6: Enter correct email address and password
        logger.info("Step 6: Entering correct email and password")
        correct_email = test_data["valid_email"]
        correct_password = test_data["valid_password"]
        
        login_page.enter_email(correct_email)
        action_delay(0.5)
        login_page.enter_password(correct_password)
        action_delay(1)
        
        # Step 7: Click 'login' button
        logger.info("Step 7: Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        # Step 8: Verify login was successful
        logger.info("Step 8: Verifying login was successful")
        is_login_success = login_page.is_login_success_message_visible()
        assert is_login_success, \
            "User login not successful or success message not visible"
        action_delay(1)
        
        logger.info("Test completed successfully - User login with correct credentials validated")
