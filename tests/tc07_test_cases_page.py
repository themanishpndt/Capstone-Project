"""
Test Case 7: Verify Test Cases Page
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Test Cases' button
5. Verify user is navigated to test cases page successfully
Workflow: Navigate to home → Click Test Cases → Verify navigation
"""

import pytest
import logging
from src.pages.home_page import HomePage

logger = logging.getLogger(__name__)


class TestTestCasesPageTC07:
    """Test suite for Test Cases page - TC07"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_test_cases_page(self, driver, base_url, action_delay):
        """Test Test Cases page accessibility and navigation"""
        
        home_page = HomePage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Verifying home page is visible")
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info(f"Home page verified: {driver.title}")
        action_delay(1)
        
        logger.info("Step 4: Clicking on Test Cases button")
        home_page.click_test_cases()
        action_delay(2)
        
        logger.info("Step 5: Verifying navigation to Test Cases page")
        current_url = driver.current_url
        assert "test_cases" in current_url.lower() or "test-cases" in current_url.lower()
        page_text = driver.execute_script("return document.body.innerText;")
        assert len(page_text) > 100
        logger.info(f"Test Cases page verified: {current_url}")
        logger.info("Test Cases page test completed successfully")
