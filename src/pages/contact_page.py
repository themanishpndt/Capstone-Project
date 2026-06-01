"""
Contact Us Page class - Page Object Model
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from src.locators.contact_locators import ContactLocators
import time


class ContactPage(BasePage):
    """Contact Us page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ContactLocators()
    
    def navigate_to_contact(self):
        """Navigate to contact us page"""
        self.navigate_to(self.locators.CONTACT_URL)
        self.logger.info("Navigated to Contact Us page")
    
    def verify_page_title(self):
        """Verify contact page title is visible"""
        is_visible = self.is_element_visible(self.locators.CONTACT_TITLE)
        self.logger.info(f"Contact page title visible: {is_visible}")
        return is_visible
    
    def enter_name(self, name):
        """Enter name in contact form"""
        self.enter_text(self.locators.NAME_INPUT, name)
        self.logger.info(f"Entered name: {name}")
    
    def enter_email(self, email):
        """Enter email in contact form"""
        self.enter_text(self.locators.EMAIL_INPUT, email)
        self.logger.info(f"Entered email: {email}")
    
    def enter_subject(self, subject):
        """Enter subject in contact form"""
        self.enter_text(self.locators.SUBJECT_INPUT, subject)
        self.logger.info(f"Entered subject: {subject}")
    
    def enter_message(self, message):
        """Enter message in contact form"""
        self.enter_text(self.locators.MESSAGE_TEXTAREA, message)
        self.logger.info(f"Entered message: {message}")
    
    def upload_file(self, file_path):
        """Upload file in contact form"""
        file_input = self.find_element(self.locators.FILE_INPUT)
        file_input.send_keys(file_path)
        self.logger.info(f"Uploaded file: {file_path}")
    
    def click_submit(self):
        """Click submit button"""
        try:
            self.click_element(self.locators.SUBMIT_BUTTON)
            self.logger.info("Clicked submit button")
        except:
            try:
                self.click_element(self.locators.SUBMIT_BUTTON_ALT)
                self.logger.info("Clicked submit button (alt)")
            except:
                # Try JavaScript to submit the form
                try:
                    self.driver.execute_script("document.getElementById('contact-us-form').submit();")
                    self.logger.info("Submitted form via JavaScript")
                except Exception as e:
                    self.logger.error(f"Failed to submit form: {e}")
                    raise
    
    def is_success_message_visible(self):
        """Check if success message is visible"""
        try:
            # Check if the success message element is displayed
            success_element = self.find_element(self.locators.SUCCESS_MESSAGE)
            is_displayed = success_element.is_displayed()
            self.logger.info(f"Success message visible: {is_displayed}")
            return is_displayed
        except Exception as e:
            self.logger.warning(f"Success message not found: {e}")
            return False
    
    def get_success_message_text(self):
        """Get success message text"""
        try:
            message = self.get_text(self.locators.SUCCESS_MESSAGE_TEXT)
            self.logger.info(f"Success message: {message}")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get success message: {e}")
            return None
    
    def fill_and_submit_contact_form(self, name, email, subject, message, file_path=None):
        """Fill and submit contact form"""
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)
        if file_path:
            self.upload_file(file_path)
        self.click_submit()
        self.logger.info("Contact form submitted")
    
    def verify_name_error(self):
        """Verify name field error"""
        return self.is_element_visible(self.locators.NAME_ERROR)
    
    def verify_email_error(self):
        """Verify email field error"""
        return self.is_element_visible(self.locators.EMAIL_ERROR)
    
    def verify_message_error(self):
        """Verify message field error"""
        return self.is_element_visible(self.locators.MESSAGE_ERROR)
    
    def verify_get_in_touch_heading(self):
        """Verify GET IN TOUCH heading is visible"""
        is_visible = self.is_element_visible(self.locators.GET_IN_TOUCH_HEADING)
        self.logger.info(f"GET IN TOUCH heading visible: {is_visible}")
        return is_visible
    
    def handle_alert_popup(self):
        """Handle OK button in alert popup after form submission"""
        try:
            wait = WebDriverWait(self.driver, 15)
            alert = wait.until(EC.alert_is_present())
            self.logger.info("Alert detected, clicking OK")
            alert.accept()
            self.logger.info("Alert accepted")
            return True
        except Exception as e:
            self.logger.warning(f"No alert found or error handling alert: {e}")
            return False
