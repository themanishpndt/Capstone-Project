"""
Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Scroll down page to bottom
5. Verify 'SUBSCRIPTION' is visible
6. Scroll up page to top
7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
Workflow: Navigate home → Scroll down → Verify subscription → Scroll up without button → Verify scrolled to top
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.scroll_page import ScrollPage

logger = logging.getLogger(__name__)


class TestVerifyScrollUpWithoutArrowButtonTC26:
    """Test suite for Verify Scroll Up without Arrow button - TC26"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_verify_scroll_up_without_arrow_button(self, driver, base_url, action_delay):
        """Test scroll up functionality without using arrow button"""
        
        home_page = HomePage(driver)
        scroll_page = ScrollPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2 & 3: Navigating to home page and verifying")
        home_page.navigate_to_home()
        action_delay(2)
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info("Home page verified")
        action_delay(1)
        
        logger.info("Step 4: Scrolling down page to bottom")
        scroll_page.scroll_down_to_bottom()
        action_delay(2)
        
        logger.info("Step 5: Verifying 'SUBSCRIPTION' is visible")
        page_text = driver.execute_script("return document.body.innerText;")
        assert "SUBSCRIPTION" in page_text or "subscription" in page_text.lower()
        logger.info("SUBSCRIPTION section verified")
        action_delay(1)
        
        logger.info("Step 6: Scrolling up page to top without using arrow button")
        scroll_page.scroll_to_top_without_button()
        action_delay(2)
        
        logger.info("Step 7: Verifying page is scrolled to top and full-fledged text is visible")
        scroll_position = scroll_page.get_scroll_position()
        assert scroll_position == 0 or scroll_position < 100
        
        page_text = driver.execute_script("return document.body.innerText;")
        assert "Full-Fledged practice website for Automation Engineers" in page_text or "Full-Fledged" in page_text
        logger.info("Page scrolled to top successfully and text verified")
        logger.info("Verify scroll up without arrow button test completed successfully")
