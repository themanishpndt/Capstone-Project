"""
Test Login and Logout Functionality
Covers user authentication scenarios
"""

import pytest
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators


class TestLoginLogout:
    """Test suite for login and logout functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_valid_login(self, driver, base_url):
        """Test login with valid credentials"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.login("test@example.com", "Password123!")
        
        # Verify successful login
        assert login_page.get_current_url() != LoginPage.locators.LOGIN_URL
    
    @pytest.mark.smoke
    def test_login_with_empty_email(self, driver):
        """Test login with empty email field"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("")
        login_page.enter_password("Password123!")
        login_page.click_login_button()
        
        # Verify error message is displayed
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.smoke
    def test_login_with_empty_password(self, driver):
        """Test login with empty password field"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("test@example.com")
        login_page.enter_password("")
        login_page.click_login_button()
        
        # Verify error message is displayed
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_login_with_invalid_email_format(self, driver):
        """Test login with invalid email format"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("invalidemail")
        login_page.enter_password("Password123!")
        login_page.click_login_button()
        
        # Verify error message for invalid email
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_login_with_incorrect_password(self, driver):
        """Test login with incorrect password"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("test@example.com")
        login_page.enter_password("WrongPassword123!")
        login_page.click_login_button()
        
        # Verify error message for incorrect credentials
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_login_with_nonexistent_user(self, driver):
        """Test login with non-existent user account"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("nonexistent@example.com")
        login_page.enter_password("Password123!")
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.functional
    def test_remember_me_checkbox(self, driver):
        """Test remember me checkbox functionality"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.check_remember_me()
        
        # Verify checkbox is checked
        checkbox = login_page.find_element(LoginPage.locators.REMEMBER_ME_CHECKBOX)
        assert checkbox.is_selected()
    
    @pytest.mark.functional
    def test_forgot_password_link(self, driver):
        """Test forgot password link"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_forgot_password()
        
        # Verify navigation to forgot password page
        assert "forgot" in driver.current_url.lower() or "reset" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_sign_up_link(self, driver):
        """Test sign up link"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.click_sign_up()
        
        # Verify navigation to sign up page
        assert "signup" in driver.current_url.lower() or "register" in driver.current_url.lower()
    
    @pytest.mark.smoke
    def test_login_button_visibility(self, driver):
        """Test login button is visible on login page"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Verify login button is displayed
        assert login_page.is_login_button_displayed()
    
    @pytest.mark.regression
    def test_login_with_sql_injection_attempt(self, driver):
        """Test login with SQL injection attempt"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("' OR '1'='1")
        login_page.enter_password("' OR '1'='1")
        login_page.click_login_button()
        
        # Verify system handles SQL injection safely
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE)
    
    @pytest.mark.regression
    def test_login_with_special_characters_in_password(self, driver):
        """Test login with special characters in password"""
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        login_page.enter_email("test@example.com")
        login_page.enter_password("P@$$w0rd!#%")
        login_page.click_login_button()
        
        # Verify special characters are handled correctly
        assert login_page.is_element_visible(CommonLocators.ERROR_MESSAGE) or \
               login_page.get_current_url() != LoginPage.locators.LOGIN_URL
    
    @pytest.mark.functional
    def test_logout_functionality(self, driver):
        """Test logout functionality"""
        login_page = LoginPage(driver)
        login_page.login("test@example.com", "Password123!")
        
        # Click logout
        login_page.click_element(CommonLocators.LOGOUT_LINK)
        
        # Verify user is logged out
        assert login_page.get_current_url() != LoginPage.locators.LOGIN_URL
