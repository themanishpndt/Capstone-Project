"""
Test Case 3: Login User with incorrect email and password
Covers invalid login scenarios with error validation
"""

import pytest
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators
import time


class TestLoginIncorrectCredentials:
    """Test suite for login with incorrect credentials"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_with_incorrect_email_and_password(self, driver, base_url, action_delay):
        """
        Test Case 3: Login User with incorrect email and password
        Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter incorrect email address and password
        7. Click 'login' button
        8. Verify error 'Your email or password is incorrect!' is visible
        """
        try:
            # Step 1 & 2: Launch browser and navigate to URL
            driver.get(base_url)
            action_delay(2.5)
            
            # Step 3: Verify home page is visible
            assert driver.title, "Home page should be loaded"
            
            # Step 4: Click on 'Signup / Login' button
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            # Step 5: Verify 'Login to your account' is visible
            login_header = driver.find_elements(*CommonLocators.LOGIN_HEADER)
            assert len(login_header) > 0, "'Login to your account' header should be visible"
            
            # Step 6: Enter incorrect email address and password
            login_page.enter_email("incorrect@example.com")
            action_delay(1.5)
            login_page.enter_password("IncorrectPassword123!")
            action_delay(1.5)
            
            # Step 7: Click 'login' button
            login_page.click_login_button()
            action_delay(2.5)
            
            # Step 8: Verify error 'Your email or password is incorrect!' is visible
            error_message = driver.find_elements(*CommonLocators.ERROR_MESSAGE)
            assert len(error_message) > 0, "Error message should be displayed for incorrect credentials"
            error_text = error_message[0].text if error_message else ""
            assert "incorrect" in error_text.lower(), f"Expected error message containing 'incorrect', got: {error_text}"
            
            print("✓ Test Case 3 PASSED: Error message verified for incorrect credentials")
            
        except AssertionError as e:
            print(f"✗ Test Case 3 FAILED: {str(e)}")
            raise
        except Exception as e:
            print(f"✗ Test Case 3 ERROR: {str(e)}")
            raise
    
    @pytest.mark.regression
    def test_login_with_incorrect_email_only(self, driver, base_url, action_delay):
        """Test login with incorrect email but correct format"""
        try:
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            # Enter non-existent but valid format email
            login_page.enter_email("nonexistent@automationexercise.com")
            action_delay(1.5)
            login_page.enter_password("Password123!")
            action_delay(1.5)
            
            login_page.click_login_button()
            action_delay(2.5)
            
            # Verify error message
            error_message = driver.find_elements(*CommonLocators.ERROR_MESSAGE)
            assert len(error_message) > 0, "Error message should be displayed"
            
            print("✓ Test PASSED: Error message verified for non-existent email")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
    
    @pytest.mark.regression
    def test_login_with_incorrect_password_only(self, driver, base_url, action_delay):
        """Test login with correct email but incorrect password"""
        try:
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            # Enter valid email but incorrect password
            login_page.enter_email("test@example.com")
            action_delay(1.5)
            login_page.enter_password("WrongPassword123!")
            action_delay(1.5)
            
            login_page.click_login_button()
            action_delay(2.5)
            
            # Verify error message
            error_message = driver.find_elements(*CommonLocators.ERROR_MESSAGE)
            assert len(error_message) > 0, "Error message should be displayed"
            
            print("✓ Test PASSED: Error message verified for incorrect password")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
    
    @pytest.mark.regression
    def test_login_with_empty_credentials(self, driver, base_url, action_delay):
        """Test login with empty email and password"""
        try:
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            # Leave fields empty and try to login
            login_page.click_login_button()
            action_delay(2.5)
            
            # Verify error message or validation
            error_message = driver.find_elements(*CommonLocators.ERROR_MESSAGE)
            assert len(error_message) > 0 or driver.current_url.endswith("login"), \
                "Should show error or remain on login page"
            
            print("✓ Test PASSED: Validation verified for empty credentials")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
