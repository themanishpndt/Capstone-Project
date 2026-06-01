"""
Test Case 4: Logout User
Test Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Navigate to login page
6. Enter correct email address and password
7. Click 'login' button
8. Verify user is logged in
9. Click 'Logout' button
10. Verify logout was successful
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestLogoutUser:
    """Test suite for user logout functionality"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_logout_user(self, driver, base_url, action_delay, test_data):
        """Test complete logout functionality"""
        
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
        
        # Step 8: Verify user is logged in
        logger.info("Step 8: Verifying user is logged in")
        is_login_success = login_page.is_login_success_message_visible()
        assert is_login_success, \
            "User login not successful"
        action_delay(1)
        
        # Step 9: Click 'Logout' button
        logger.info("Step 9: Clicking Logout button")
        home_page.click_logout()
        action_delay(2)
        
        # Step 10: Verify logout was successful
        logger.info("Step 10: Verifying logout was successful")
        current_url = login_page.get_current_url()
        assert "login" in current_url.lower() or login_page.is_login_button_displayed(), \
            "User not logged out properly"
        action_delay(1)
        
        logger.info("Test completed successfully - User logout flow validated")
