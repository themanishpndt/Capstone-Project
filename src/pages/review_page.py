"""
Review Page class - Page Object Model (Product Details with Reviews)
"""

import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.base_page import BasePage
from src.locators.review_locators import ReviewLocators


class ReviewPage(BasePage):
    """Review/Product Details page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ReviewLocators()
    
    def get_product_name(self):
        """Get product name"""
        try:
            name = self.get_text(self.locators.PRODUCT_NAME)
            self.logger.info(f"Product name: {name}")
            return name
        except Exception as e:
            self.logger.error(f"Failed to get product name: {e}")
            return None
    
    def get_product_price(self):
        """Get product price"""
        try:
            price = self.get_text(self.locators.PRODUCT_PRICE)
            self.logger.info(f"Product price: {price}")
            return price
        except Exception as e:
            self.logger.error(f"Failed to get product price: {e}")
            return None
    
    def get_product_rating(self):
        """Get product rating"""
        try:
            rating = self.get_text(self.locators.PRODUCT_RATING)
            self.logger.info(f"Product rating: {rating}")
            return rating
        except Exception as e:
            self.logger.error(f"Failed to get product rating: {e}")
            return None
    
    def get_product_availability(self):
        """Get product availability"""
        try:
            availability = self.get_text(self.locators.PRODUCT_AVAILABILITY)
            self.logger.info(f"Product availability: {availability}")
            return availability
        except Exception as e:
            self.logger.error(f"Failed to get product availability: {e}")
            return None
    
    def scroll_to_reviews_section(self):
        """Scroll to reviews section"""
        try:
            reviews_section = self.find_element(self.locators.REVIEWS_SECTION)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", reviews_section)
            self.logger.info("Scrolled to reviews section")
        except Exception as e:
            self.logger.error(f"Failed to scroll to reviews section: {e}")
    
    def click_review_tab(self):
        """Click on review tab"""
        try:
            self.click_element(self.locators.REVIEW_TAB)
            self.logger.info("Clicked on review tab")
        except Exception as e:
            self.logger.error(f"Failed to click review tab: {e}")
    
    def enter_review_name(self, name):
        """Enter reviewer name"""
        self.enter_text(self.locators.REVIEW_NAME_INPUT, name)
        self.logger.info(f"Entered review name: {name}")
    
    def enter_review_email(self, email):
        """Enter reviewer email"""
        self.enter_text(self.locators.REVIEW_EMAIL_INPUT, email)
        self.logger.info(f"Entered review email: {email}")
    
    def enter_review_text(self, review_text):
        """Enter review text"""
        self.enter_text(self.locators.REVIEW_TEXTAREA, review_text)
        self.logger.info(f"Entered review text: {review_text}")
    
    def set_review_rating(self, rating):
        """Set review rating (1-5)"""
        implicit_wait = int(os.getenv("IMPLICIT_WAIT", 10))
        self.driver.implicitly_wait(0)
        try:
            radio_buttons = self.driver.find_elements(*self.locators.REVIEW_RATING_RADIO)
        finally:
            self.driver.implicitly_wait(implicit_wait)

        if not radio_buttons:
            self.logger.info("Review rating controls are not present; skipping rating selection")
            return

        if rating <= len(radio_buttons):
            radio_buttons[rating - 1].click()
            self.logger.info(f"Set review rating: {rating} stars")
    
    def click_submit_review(self):
        """Click submit review button"""
        self.wait.until(EC.visibility_of_element_located(self.locators.REVIEW_NAME_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.locators.REVIEW_EMAIL_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.locators.REVIEW_TEXTAREA))

        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: driver.execute_script(
                    "return document.readyState !== 'loading' && !!window.jQuery;"
                )
            )
        except TimeoutException:
            self.logger.warning("Review scripts were slow to report ready; submitting with visible form controls")

        self.click_element(self.locators.SUBMIT_REVIEW_BUTTON)
        self.logger.info("Clicked submit review button")
    
    def is_review_success_message_visible(self):
        """Check if review success message is visible"""
        is_visible = self.is_element_visible(self.locators.REVIEW_SUCCESS_MESSAGE)
        self.logger.info(f"Review success message visible: {is_visible}")
        return is_visible
    
    def get_existing_reviews_count(self):
        """Get count of existing reviews"""
        reviews = self.find_elements(self.locators.EXISTING_REVIEWS)
        count = len(reviews)
        self.logger.info(f"Found {count} existing reviews")
        return count
    
    def submit_product_review(self, name, email, review_text, rating):
        """Submit a complete product review"""
        self.enter_review_name(name)
        self.enter_review_email(email)
        self.enter_review_text(review_text)
        self.set_review_rating(rating)
        self.click_submit_review()
        self.logger.info("Product review submitted")
    
    def verify_review_section_visible(self):
        """Verify review section is visible"""
        is_visible = self.is_element_visible(self.locators.REVIEWS_SECTION)
        self.logger.info(f"Review section visible: {is_visible}")
        return is_visible
    
    def submit_review(self):
        """Submit review (alias for click_submit_review)"""
        self.click_submit_review()
