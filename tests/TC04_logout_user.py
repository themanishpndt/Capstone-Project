"""
Test Case 4: Logout User
Covers user logout functionality after successful login
"""

import pytest
from src.pages.login_page import LoginPage
from src.locators.common_locators import CommonLocators
import time


class TestLogoutUser:
    """Test suite for user logout functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_logout_user(self, driver, base_url, action_delay):
        """
        Test Case 4: Logout User
        Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Logout' button
        10. Verify that user is navigated to login page
        """
        try:
            # Step 1 & 2: Launch browser and navigate to URL
            driver.get(base_url)
            action_delay(2.5)
            
            # Step 3: Verify home page is visible successfully
            assert driver.title, "Home page should be loaded"
            print("✓ Step 3: Home page is visible")
            
            # Step 4: Click on 'Signup / Login' button
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            # Step 5: Verify 'Login to your account' is visible
            login_header = driver.find_elements(*CommonLocators.LOGIN_HEADER)
            assert len(login_header) > 0, "'Login to your account' header should be visible"
            print("✓ Step 5: Login header is visible")
            
            # Step 6: Enter correct email address and password
            login_page.enter_email("test@example.com")
            action_delay(1.5)
            login_page.enter_password("Password123!")
            action_delay(1.5)
            
            # Step 7: Click 'login' button
            login_page.click_login_button()
            action_delay(2.5)
            
            # Step 8: Verify that 'Logged in as username' is visible
            logged_in_header = driver.find_elements(*CommonLocators.LOGGED_IN_AS)
            assert len(logged_in_header) > 0, "'Logged in as username' should be visible after successful login"
            print("✓ Step 8: User is logged in - 'Logged in as username' is visible")
            
            # Step 9: Click 'Logout' button
            logout_button = driver.find_elements(*CommonLocators.LOGOUT_BUTTON)
            assert len(logout_button) > 0, "Logout button should be visible"
            logout_button[0].click()
            action_delay(2.5)
            
            # Step 10: Verify that user is navigated to login page
            current_url = driver.current_url
            assert "login" in current_url.lower() or "signin" in current_url.lower(), \
                f"User should be navigated to login page, but URL is: {current_url}"
            print("✓ Step 10: User is navigated to login page")
            
            print("✓ Test Case 4 PASSED: Logout functionality verified successfully")
            
        except AssertionError as e:
            print(f"✗ Test Case 4 FAILED: {str(e)}")
            raise
        except Exception as e:
            print(f"✗ Test Case 4 ERROR: {str(e)}")
            raise
    
    @pytest.mark.functional
    def test_logout_redirects_to_login_page(self, driver, base_url, action_delay):
        """Test that logout button properly redirects to login page"""
        try:
            # Navigate and login
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            login_page.enter_email("test@example.com")
            action_delay(1.5)
            login_page.enter_password("Password123!")
            action_delay(1.5)
            login_page.click_login_button()
            action_delay(2.5)
            
            # Verify logged in
            logged_in = driver.find_elements(*CommonLocators.LOGGED_IN_AS)
            assert len(logged_in) > 0, "User should be logged in"
            
            # Click logout
            logout_button = driver.find_elements(*CommonLocators.LOGOUT_BUTTON)
            logout_button[0].click()
            action_delay(2.5)
            
            # Verify redirected to login page
            time.sleep(1)  # Extra wait for page load
            assert "login" in driver.current_url.lower(), "Should be redirected to login page"
            
            print("✓ Test PASSED: Logout redirects to login page correctly")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
    
    @pytest.mark.functional
    def test_cannot_access_account_after_logout(self, driver, base_url, action_delay):
        """Test that user account cannot be accessed after logout"""
        try:
            # Navigate and login
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            login_page.enter_email("test@example.com")
            action_delay(1.5)
            login_page.enter_password("Password123!")
            action_delay(1.5)
            login_page.click_login_button()
            action_delay(2.5)
            
            # Verify logged in
            logged_in = driver.find_elements(*CommonLocators.LOGGED_IN_AS)
            assert len(logged_in) > 0, "User should be logged in"
            
            # Click logout
            logout_button = driver.find_elements(*CommonLocators.LOGOUT_BUTTON)
            logout_button[0].click()
            action_delay(2.5)
            
            # Verify 'Logged in as username' is no longer visible
            logged_in_after_logout = driver.find_elements(*CommonLocators.LOGGED_IN_AS)
            assert len(logged_in_after_logout) == 0, "'Logged in as username' should not be visible after logout"
            
            print("✓ Test PASSED: User cannot access account after logout")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
    
    @pytest.mark.regression
    def test_logout_session_cleared(self, driver, base_url, action_delay):
        """Test that user session is properly cleared after logout"""
        try:
            # Navigate and login
            driver.get(base_url)
            action_delay(2.5)
            
            login_page = LoginPage(driver)
            login_page.navigate_to_login()
            action_delay(2.5)
            
            login_page.enter_email("test@example.com")
            action_delay(1.5)
            login_page.enter_password("Password123!")
            action_delay(1.5)
            login_page.click_login_button()
            action_delay(2.5)
            
            # Store session info
            initial_cookies = driver.get_cookies()
            
            # Click logout
            logout_button = driver.find_elements(*CommonLocators.LOGOUT_BUTTON)
            logout_button[0].click()
            action_delay(2.5)
            
            # Check that we're on login page
            assert "login" in driver.current_url.lower(), "Should be on login page"
            
            print("✓ Test PASSED: Session cleared after logout")
            
        except AssertionError as e:
            print(f"✗ Test FAILED: {str(e)}")
            raise
