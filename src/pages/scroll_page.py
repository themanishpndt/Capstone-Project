"""
Scroll Page class - Page Object Model (for scroll functionality tests)
"""

from src.pages.base_page import BasePage
from src.locators.scroll_locators import ScrollLocators
from selenium.webdriver.common.action_chains import ActionChains


class ScrollPage(BasePage):
    """Scroll functionality page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ScrollLocators()
        self.actions = ActionChains(driver)
    
    def scroll_down_to_footer(self):
        """Scroll down to footer"""
        footer = self.find_element(self.locators.FOOTER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        self.logger.info("Scrolled down to footer")
    
    def scroll_down_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("Scrolled to bottom of page")
    
    def scroll_to_top_using_button(self):
        """Scroll to top using scroll up button"""
        try:
            scroll_button = self.find_element(self.locators.SCROLL_UP_BUTTON)
            scroll_button.click()
            self.logger.info("Scrolled to top using scroll button")
        except Exception as e:
            self.logger.error(f"Failed to scroll using button: {e}")
            raise
    
    def scroll_to_top_without_button(self):
        """Scroll to top without using button"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.logger.info("Scrolled to top without button")
    
    def is_scroll_button_visible(self):
        """Check if scroll to top button is visible"""
        is_visible = self.is_element_visible(self.locators.SCROLL_UP_BUTTON)
        self.logger.info(f"Scroll up button visible: {is_visible}")
        return is_visible
    
    def get_scroll_position(self):
        """Get current scroll position"""
        scroll_y = self.driver.execute_script("return window.pageYOffset;")
        self.logger.info(f"Current scroll position: {scroll_y}")
        return scroll_y
    
    def wait_for_scroll_button_visibility(self, timeout=10):
        """Wait for scroll button to become visible"""
        try:
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
            
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(self.locators.SCROLL_UP_BUTTON))
            self.logger.info("Scroll button became visible")
            return True
        except Exception as e:
            self.logger.error(f"Scroll button did not become visible: {e}")
            return False
    
    def wait_for_scroll_button_invisibility(self, timeout=10):
        """Wait for scroll button to become invisible"""
        try:
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
            
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(self.locators.SCROLL_UP_BUTTON))
            self.logger.info("Scroll button became invisible")
            return True
        except Exception as e:
            self.logger.error(f"Scroll button did not become invisible: {e}")
            return False
    
    def scroll_page_by_pixels(self, pixels):
        """Scroll page by specific number of pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        self.logger.info(f"Scrolled by {pixels} pixels")
    
    def verify_at_top_of_page(self):
        """Verify page is scrolled to top"""
        scroll_position = self.get_scroll_position()
        is_at_top = scroll_position == 0
        self.logger.info(f"Page at top: {is_at_top}")
        return is_at_top
    
    def verify_at_bottom_of_page(self):
        """Verify page is scrolled to bottom"""
        current_scroll = self.driver.execute_script("return window.pageYOffset;")
        total_height = self.driver.execute_script("return document.body.scrollHeight;")
        window_height = self.driver.execute_script("return window.innerHeight;")
        is_at_bottom = (current_scroll + window_height) >= (total_height - 1)
        self.logger.info(f"Page at bottom: {is_at_bottom}")
        return is_at_bottom
