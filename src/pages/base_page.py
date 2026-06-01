"""
Base Page class containing common functionality for all pages
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logger
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            elements = self.driver.find_elements(*locator)
            self.logger.info(f"Found {len(elements)} elements: {locator}")
            return elements
        except NoSuchElementException:
            self.logger.error(f"Elements not found: {locator}")
            return []
    
    def click_element(self, locator):
        """Click on element"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            try:
                element.click()
            except (ElementClickInterceptedException, TimeoutException, WebDriverException) as e:
                self.logger.warning(f"Native click failed for {locator}; using JavaScript click: {e}")
                self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Clicked element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise
    
    def enter_text(self, locator, text):
        """Enter text in an element"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' in element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to enter text: {e}")
            raise
    
    def get_text(self, locator):
        """Get text from element"""
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.info(f"Retrieved text from element: {locator} = '{text}'")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text: {e}")
            raise
    
    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"Element is not visible: {locator}")
            return False
    
    def wait_for_url_contains(self, url_fragment):
        """Wait for URL to contain specific fragment"""
        try:
            self.wait.until(EC.url_contains(url_fragment))
            self.logger.info(f"URL contains: {url_fragment}")
        except TimeoutException:
            self.logger.error(f"URL does not contain: {url_fragment}")
            raise
    
    def navigate_to(self, url):
        """Navigate to specific URL"""
        try:
            self.driver.get(url)
            try:
                self.driver.execute_script("window.stop();")
            except WebDriverException:
                pass
            self.logger.info(f"Navigated to: {url}")
        except TimeoutException:
            self.logger.warning(f"Page load timed out for {url}; stopping load and continuing")
            try:
                self.driver.execute_script("window.stop();")
                self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            except WebDriverException as e:
                self.logger.error(f"Page was not usable after timeout for {url}: {e}")
                raise
        except Exception as e:
            self.logger.error(f"Failed to navigate to {url}: {e}")
            raise
    
    def refresh_page(self):
        """Refresh the page"""
        self.driver.refresh()
        self.logger.info("Page refreshed")
    
    def get_current_url(self):
        """Get current page URL"""
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url
    
    def go_back(self):
        """Navigate back"""
        self.driver.back()
        self.logger.info("Navigated back")
    
    def go_forward(self):
        """Navigate forward"""
        self.driver.forward()
        self.logger.info("Navigated forward")
