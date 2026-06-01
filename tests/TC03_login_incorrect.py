"""
Test Case 3: Login User with incorrect email and password
Test Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Navigate to login page
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error message is visible
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestLoginUserIncorrectCredentials:
    """Test suite for user login with incorrect credentials"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_with_incorrect_email_and_password(self, driver, base_url, action_delay, test_data):
        """Test login functionality with invalid email and password"""
        
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
        
        # Step 6: Enter incorrect email address and password
        logger.info("Step 6: Entering incorrect email and password")
        incorrect_email = test_data["invalid_email"]
        incorrect_password = test_data["invalid_password"]
        
        login_page.enter_email(incorrect_email)
        action_delay(0.5)
        login_page.enter_password(incorrect_password)
        action_delay(1)
        
        # Step 7: Click 'login' button
        logger.info("Step 7: Clicking login button")
        login_page.click_login_button()
        action_delay(2)
        
        # Step 8: Verify error message is visible
        logger.info("Step 8: Verifying error message for incorrect credentials")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0, \
            "Expected error message not found"
        action_delay(1)
        
        logger.info(f"Test completed successfully - Error message: {error_message}")
