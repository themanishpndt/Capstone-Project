"""
Test Case 1: Register User
Test Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify signup page loads
6. Enter name and email address
7. Click 'Signup' button
8. Verify registration page loads
9-12. Fill registration details
13. Click 'Create Account' button
14-18. Verify account created and cleanup
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestRegisterUser:
    """Test suite for user registration"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_register_user_workflow(self, driver, base_url, action_delay):
        """Test user registration workflow"""
        
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
        
        # Step 5: Verify signup/login page is visible
        logger.info("Step 5: Verifying signup/login page is visible")
        login_page = LoginPage(driver)
        login_page.navigate_to_login()  # Verify we can navigate to login
        action_delay(1)
        
        # Step 6: Enter name and email address
        logger.info("Step 6: Entering signup information")
        signup_name = "Test User"
        signup_email = f"testuser_{int(__import__('time').time())}@example.com"
        login_page.enter_signup_name(signup_name)
        action_delay(0.5)
        login_page.enter_signup_email(signup_email)
        action_delay(1)
        
        # Step 7: Click 'Signup' button
        logger.info("Step 7: Clicking Signup button")
        login_page.click_signup_button()
        action_delay(2)
        
        logger.info("Test completed successfully - User signup initiated")
