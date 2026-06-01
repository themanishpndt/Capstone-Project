"""
Test Case 26: Verify Scroll Up Without Arrow Button
Verify that user can scroll up without using the arrow button
"""

import pytest
import allure
import logging
import time
from src.pages.home_page import HomePage
from src.pages.scroll_page import ScrollPage

logger = logging.getLogger(__name__)


class TestScrollUpWithoutArrowButton:
    """Test suite for scroll up without arrow button"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC26: Verify Scroll Up Without Arrow Button")
    @allure.description("Verify that user can scroll to top without using the arrow button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_scroll_up_without_arrow_button(self, driver, base_url):
        """Test scrolling up without arrow button"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll down to footer"):
            scroll_page = ScrollPage(driver)
            scroll_page.scroll_down_to_bottom()
        
        with allure.step("Verify page is at bottom"):
            assert scroll_page.verify_at_bottom_of_page(), \
                "Page is not at bottom"
            logger.info("Page scrolled to bottom")
        
        with allure.step("Scroll to top without button"):
            scroll_page.scroll_to_top_without_button()
            time.sleep(0.5)  # Wait for scroll
        
        with allure.step("Verify page is at top"):
            assert scroll_page.verify_at_top_of_page(), \
                "Page is not at top after scrolling without button"
            logger.info("Page scrolled to top successfully without arrow button")
    
    @pytest.mark.regression
    @allure.title("TC26: Scroll by Pixels")
    @allure.description("Verify page scroll by specific pixel amount")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scroll_by_pixels(self, driver, base_url):
        """Test scrolling by specific pixels"""
        with allure.step("Navigate to home"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll by 500 pixels"):
            scroll_page = ScrollPage(driver)
            scroll_page.scroll_page_by_pixels(500)
            time.sleep(0.5)
        
        with allure.step("Verify scroll position"):
            position = scroll_page.get_scroll_position()
            assert position > 0, "Page should be scrolled down"
            logger.info(f"Current scroll position: {position}px")
        
        with allure.step("Scroll back to top"):
            scroll_page.scroll_to_top_without_button()
        
        with allure.step("Verify at top"):
            assert scroll_page.verify_at_top_of_page(), "Should be at top"
            logger.info("Scroll position verification completed")
    
    @pytest.mark.regression
    @allure.title("TC26: Verify Scroll Position Tracking")
    @allure.description("Verify that scroll position can be tracked accurately")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scroll_position_tracking(self, driver, base_url):
        """Test scroll position tracking"""
        with allure.step("Navigate to home"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Check position at top"):
            scroll_page = ScrollPage(driver)
            top_position = scroll_page.get_scroll_position()
            assert top_position == 0, "Should be at position 0 at top"
            logger.info(f"Position at top: {top_position}px")
        
        with allure.step("Scroll down and track position"):
            scroll_page.scroll_page_by_pixels(300)
            mid_position = scroll_page.get_scroll_position()
            logger.info(f"Position after scrolling 300px: {mid_position}px")
        
        with allure.step("Scroll more and track"):
            scroll_page.scroll_page_by_pixels(300)
            final_position = scroll_page.get_scroll_position()
            logger.info(f"Final scroll position: {final_position}px")
        
        with allure.step("Verify positions are different"):
            assert final_position > mid_position > top_position, \
                "Scroll positions should increase"
            logger.info("Scroll position tracking verified")
