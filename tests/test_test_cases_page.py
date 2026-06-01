"""
Test Case 07: Verify Test Cases Page
Verify that the Test Cases page is accessible and displays all test cases
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage

logger = logging.getLogger(__name__)


class TestTestCasesPage:
    """Test suite for Test Cases page"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC07: Verify Test Cases Page")
    @allure.description("Verify that Test Cases page is accessible and loads correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_test_cases_page_accessibility(self, driver, base_url):
        """Test Test Cases page is accessible"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Click Test Cases link"):
            home_page.click_test_cases()
        
        with allure.step("Verify Test Cases page loaded"):
            # Wait for page to load
            import time
            time.sleep(2)
            
            # Check current URL contains test_cases
            current_url = driver.current_url
            assert "test_cases" in current_url.lower(), f"Expected test_cases in URL, got: {current_url}"
            logger.info(f"Test Cases page accessed: {current_url}")
    
    @pytest.mark.regression
    @allure.title("TC07: Test Cases Page Title Verification")
    @allure.description("Verify that Test Cases page has the correct title")
    @allure.severity(allure.severity_level.NORMAL)
    def test_test_cases_page_title(self, driver, base_url):
        """Test Test Cases page title"""
        with allure.step("Navigate to Test Cases page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_test_cases()
        
        with allure.step("Verify page title"):
            page_title = driver.title
            # Test Cases page should have specific title
            assert "test" in page_title.lower() or "case" in page_title.lower(), \
                f"Expected test cases in title, got: {page_title}"
            logger.info(f"Page title verified: {page_title}")
    
    @pytest.mark.regression
    @allure.title("TC07: Test Cases Page Content Verification")
    @allure.description("Verify that Test Cases page displays test case information")
    @allure.severity(allure.severity_level.NORMAL)
    def test_test_cases_page_content(self, driver, base_url):
        """Test that Test Cases page has content"""
        with allure.step("Navigate to Test Cases page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_test_cases()
        
        with allure.step("Verify page content"):
            import time
            time.sleep(2)
            
            # Check if page has content
            body = driver.find_element("tag name", "body")
            page_source = body.text
            
            # Should contain test case information
            assert len(page_source) > 100, "Test Cases page appears to have no content"
            logger.info("Test Cases page contains expected content")
