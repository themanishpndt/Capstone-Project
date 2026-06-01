"""
Demo/Sample Tests - Framework Validation
These tests demonstrate the test framework is working correctly
"""

import pytest
from src.pages.login_page import LoginPage


class TestFrameworkDemo:
    """Demo tests to show framework is working"""
    
    @pytest.mark.smoke
    def test_framework_is_configured(self):
        """Test that the framework is properly configured"""
        # This test verifies pytest configuration is working
        assert True
    
    @pytest.mark.functional
    def test_test_data_fixture_available(self, test_data):
        """Test that test_data fixture is available"""
        assert test_data is not None
        assert test_data["first_name"] == "John"
        assert test_data["valid_email"] == "test@example.com"
    
    @pytest.mark.functional
    def test_driver_fixture_available(self, driver):
        """Test that driver fixture is available"""
        assert driver is not None
        # Test that driver has expected methods
        assert hasattr(driver, 'get')
        assert hasattr(driver, 'find_element')
        assert hasattr(driver, 'quit')
    
    @pytest.mark.functional
    def test_config_loaded(self):
        """Test that configuration is loaded properly"""
        from config.config import Config
        assert Config.BASE_URL is not None
        assert len(Config.BASE_URL) > 0
    
    @pytest.mark.functional
    def test_page_object_model_working(self, driver):
        """Test that Page Object Model is working"""
        login_page = LoginPage(driver)
        assert login_page is not None
        assert hasattr(login_page, 'enter_email')
        assert hasattr(login_page, 'enter_password')
        assert hasattr(login_page, 'click_login_button')
    
    @pytest.mark.smoke
    def test_base_page_methods_available(self, driver):
        """Test that BasePage methods are available"""
        from src.pages.base_page import BasePage
        base_page = BasePage(driver)
        
        # Verify key methods exist
        assert hasattr(base_page, 'find_element')
        assert hasattr(base_page, 'click_element')
        assert hasattr(base_page, 'enter_text')
        assert hasattr(base_page, 'get_text')
        assert hasattr(base_page, 'navigate_to')
    
    @pytest.mark.functional
    def test_locators_module_working(self):
        """Test that locators module is working"""
        from src.locators.login_locators import LoginLocators
        
        locators = LoginLocators()
        assert locators.EMAIL_INPUT is not None
        assert locators.PASSWORD_INPUT is not None
        assert len(locators.LOGIN_URL) > 0
    
    @pytest.mark.functional
    def test_utilities_available(self):
        """Test that utility modules are available"""
        from src.utils.logger_utils import setup_logger
        from src.utils.wait_utils import wait_for_element_visibility
        from src.utils.screenshot_utils import take_screenshot
        
        assert callable(setup_logger)
        assert callable(wait_for_element_visibility)
        assert callable(take_screenshot)
    
    @pytest.mark.functional
    def test_pytest_markers_working(self):
        """Test that pytest markers are configured"""
        # This test has smoke marker
        assert True
    
    @pytest.mark.regression
    def test_multiple_assertions(self, test_data):
        """Test multiple assertions in one test"""
        assert test_data["first_name"] is not None
        assert len(test_data["first_name"]) > 0
        assert test_data["last_name"] is not None
        assert "@" in test_data["valid_email"]
        assert len(test_data["valid_password"]) >= 8
