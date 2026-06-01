"""
Test Case 25: Verify Scroll Up Using Arrow Button
Verify that user can scroll up using the scroll arrow button
"""

import pytest
import allure
import logging
import time
from src.pages.home_page import HomePage
from src.pages.scroll_page import ScrollPage

logger = logging.getLogger(__name__)


class TestScrollUpArrowButton:
    """Test suite for scroll up using arrow button"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC25: Verify Scroll Up Using Arrow Button")
    @allure.description("Verify that user can scroll to top using the scroll up arrow button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_scroll_up_using_arrow_button(self, driver, base_url):
        """Test scrolling up using arrow button"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll down to footer"):
            scroll_page = ScrollPage(driver)
            scroll_page.scroll_down_to_bottom()
        
        with allure.step("Verify scroll button is visible"):
            assert scroll_page.is_scroll_button_visible(), \
                "Scroll up button not visible when scrolled down"
            logger.info("Scroll up button is visible")
        
        with allure.step("Click scroll up button"):
            scroll_page.scroll_to_top_using_button()
            time.sleep(1)  # Wait for scroll animation
        
        with allure.step("Verify page is at top"):
            assert scroll_page.verify_at_top_of_page(), \
                "Page is not at top after clicking scroll button"
            logger.info("Page scrolled to top successfully using arrow button")
    
    @pytest.mark.regression
    @allure.title("TC25: Scroll Button Visibility During Scroll")
    @allure.description("Verify scroll button appears and disappears appropriately")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scroll_button_visibility(self, driver, base_url):
        """Test scroll button visibility during scroll"""
        with allure.step("Navigate to home"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Verify button not visible at top"):
            scroll_page = ScrollPage(driver)
            is_visible_at_top = scroll_page.is_scroll_button_visible()
            logger.info(f"Button visible at top: {is_visible_at_top}")
        
        with allure.step("Scroll down"):
            scroll_page.scroll_down_to_bottom()
        
        with allure.step("Verify button visible after scroll"):
            is_visible_after_scroll = scroll_page.is_scroll_button_visible()
            assert is_visible_after_scroll, "Button should be visible after scrolling"
            logger.info("Button visibility verified after scrolling")
    
    @pytest.mark.regression
    @allure.title("TC25: Multiple Scroll Up Operations")
    @allure.description("Verify scroll up button works for multiple scroll operations")
    @allure.severity(allure.severity_level.NORMAL)
    def test_multiple_scroll_operations(self, driver, base_url):
        """Test multiple scroll operations"""
        with allure.step("Navigate to home"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Perform multiple scroll operations"):
            scroll_page = ScrollPage(driver)
            
            # Scroll down
            scroll_page.scroll_down_to_bottom()
            time.sleep(0.5)
            
            # Scroll up using button
            scroll_page.scroll_to_top_using_button()
            time.sleep(0.5)
            
            # Scroll down again
            scroll_page.scroll_down_to_bottom()
            time.sleep(0.5)
            
            # Scroll up again
            scroll_page.scroll_to_top_using_button()
        
        with allure.step("Verify final scroll position"):
            assert scroll_page.verify_at_top_of_page(), \
                "Page should be at top after multiple scroll operations"
            logger.info("Multiple scroll operations completed successfully")
