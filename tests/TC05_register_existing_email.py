"""
Test Case 5: Register User with existing email
Test Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators

logger = logging.getLogger(__name__)


class TestRegisterExistingEmail:
    """Test suite for registering with existing email"""
    
    @pytest.mark.regression
    @pytest.mark.critical
    def test_register_user_with_existing_email(self, driver, base_url, action_delay):
        """Test registration with existing email"""
        
        # Step 1-2: Launch browser and navigate to URL
        logger.info("Step 1-2: Launching browser and navigating to URL")
        home_page = HomePage(driver)
        home_page.navigate_to(base_url)
        action_delay(1)
        
        # Step 3: Verify that home page is visible successfully
        logger.info("Step 3: Verifying home page is visible")
        assert home_page.is_element_visible(CommonLocators.HOME_PAGE_HEADER), \
            "Home page header not visible"
        action_delay(1)
        
        # Step 4: Click on 'Signup / Login' button
        logger.info("Step 4: Clicking on Signup/Login button")
        home_page.click_signup_login_button()
        action_delay(2)
        
        # Step 5: Verify 'New User Signup!' is visible
        logger.info("Step 5: Verifying New User Signup text is visible")
        login_page = LoginPage(driver)
        assert login_page.is_element_visible(CommonLocators.NEW_USER_SIGNUP), \
            "New User Signup text not visible"
        action_delay(1)
        
        # Step 6: Enter name and already registered email address
        logger.info("Step 6: Entering name and already registered email")
        signup_name = "Test User"
        already_registered_email = "test@example.com"  # Using an already registered email
        
        login_page.enter_signup_name(signup_name)
        action_delay(0.5)
        login_page.enter_signup_email(already_registered_email)
        action_delay(1)
        
        # Step 7: Click 'Signup' button
        logger.info("Step 7: Clicking Signup button")
        login_page.click_signup_button()
        action_delay(2)
        
        # Step 8: Verify error message is visible
        logger.info("Step 8: Verifying error message for existing email")
        error_message = login_page.get_error_message()
        assert error_message and len(error_message) > 0, \
            "Expected error message not found"
        action_delay(1)
        
        logger.info(f"Test completed successfully - Error message: {error_message}")

