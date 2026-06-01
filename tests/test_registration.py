"""
Test User Registration Functionality
Covers account creation scenarios
"""

import pytest
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators


class TestRegistration:
    """Test suite for user registration"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_valid_registration(self, driver, test_data):
        """Test user registration with valid data"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        # Fill registration form
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            test_data["valid_email"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='confirm_password']"),
            test_data["valid_password"]
        )
        
        # Submit registration
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify successful registration
        assert login_page.is_element_visible(CommonLocators.SUCCESS_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_empty_first_name(self, driver, test_data):
        """Test registration with empty first name"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        # Leave first name empty
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            test_data["valid_email"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_empty_email(self, driver, test_data):
        """Test registration with empty email"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        # Leave email empty
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_invalid_email_format(self, driver, test_data):
        """Test registration with invalid email format"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            "invalidemail"
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message for invalid email
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_password_mismatch(self, driver, test_data):
        """Test registration with mismatched passwords"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            test_data["valid_email"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='confirm_password']"),
            "DifferentPassword123!"
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message for password mismatch
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_weak_password(self, driver, test_data):
        """Test registration with weak password"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            test_data["valid_email"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            "weak"
        )
        login_page.enter_text(
            ("xpath", "//input[@name='confirm_password']"),
            "weak"
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message for weak password
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_registration_with_existing_email(self, driver, test_data):
        """Test registration with already existing email"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        login_page.enter_text(
            ("xpath", "//input[@name='first_name']"),
            test_data["first_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='last_name']"),
            test_data["last_name"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='email']"),
            "existing@example.com"
        )
        login_page.enter_text(
            ("xpath", "//input[@name='password']"),
            test_data["valid_password"]
        )
        login_page.enter_text(
            ("xpath", "//input[@name='confirm_password']"),
            test_data["valid_password"]
        )
        
        login_page.click_element(CommonLocators.SUBMIT_BUTTON)
        
        # Verify error message for existing email
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.functional
    def test_registration_form_field_validation(self, driver):
        """Test registration form field validations"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        # Verify all form fields are present
        assert login_page.is_element_visible(("xpath", "//input[@name='first_name']"))
        assert login_page.is_element_visible(("xpath", "//input[@name='last_name']"))
        assert login_page.is_element_visible(("xpath", "//input[@name='email']"))
        assert login_page.is_element_visible(("xpath", "//input[@name='password']"))
        assert login_page.is_element_visible(("xpath", "//input[@name='confirm_password']"))
