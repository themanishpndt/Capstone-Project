"""
Test Case 05: Register User with Existing Email
Verify that registering with an email that already exists shows an error
"""

import pytest
import allure
import logging
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators

logger = logging.getLogger(__name__)


class TestRegisterExistingEmail:
    """Test suite for registering with existing email"""
    
    @pytest.mark.regression
    @pytest.mark.critical
    @allure.title("TC05: Register User with Existing Email")
    @allure.description("Verify that user cannot register with an email that already exists in the system")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_user_with_existing_email(self, driver, base_url):
        """Test registration with existing email"""
        with allure.step("Navigate to registration page"):
            login_page = LoginPage(driver)
            login_page.navigate_to(f"{base_url}/login")
        
        with allure.step("Click Sign Up button"):
            login_page.click_sign_up()
        
        with allure.step("Fill registration form with existing email"):
            # Using a known existing email from test data
            login_page.enter_email("test@example.com")
            login_page.enter_text(login_page.locators.FIRST_NAME_INPUT, "John")
            login_page.enter_text(login_page.locators.LAST_NAME_INPUT, "Doe")
            login_page.enter_text(login_page.locators.PASSWORD_INPUT, "Password123!")
        
        with allure.step("Submit registration form"):
            login_page.click_element(login_page.locators.REGISTER_BUTTON)
        
        with allure.step("Verify error message is displayed"):
            # Error should be shown as email already exists
            error_visible = login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
            assert error_visible, "Expected error message for existing email not displayed"
            logger.info("Error message correctly displayed for existing email")
    
    @pytest.mark.regression
    @allure.title("TC05: Verify Registration Error Message Content")
    @allure.description("Verify that the error message contains correct text about email already existing")
    @allure.severity(allure.severity_level.NORMAL)
    def test_existing_email_error_message_content(self, driver, base_url):
        """Test that error message has correct content"""
        with allure.step("Navigate to registration page and attempt registration"):
            login_page = LoginPage(driver)
            login_page.navigate_to(f"{base_url}/login")
            login_page.click_sign_up()
        
        with allure.step("Fill form with existing email"):
            login_page.enter_email("test@example.com")
            login_page.enter_text(login_page.locators.FIRST_NAME_INPUT, "John")
            login_page.enter_text(login_page.locators.LAST_NAME_INPUT, "Doe")
            login_page.enter_text(login_page.locators.PASSWORD_INPUT, "Password123!")
            login_page.click_element(login_page.locators.REGISTER_BUTTON)
        
        with allure.step("Get and verify error message"):
            error_message = login_page.get_text(CommonLocators.ERROR_MESSAGE)
            assert "already exists" in error_message.lower() or "exists" in error_message.lower(), \
                f"Expected error about existing email, got: {error_message}"
            logger.info(f"Error message verified: {error_message}")
