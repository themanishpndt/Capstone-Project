"""
Test Case 6: Contact Us Form
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Contact Us' button
5. Verify 'GET IN TOUCH' is visible
6. Enter name, email, subject and message
7. Upload file
8. Click 'Submit' button
9. Click OK button
10. Verify success message 'Success! Your details have been submitted successfully.' is visible
11. Click 'Home' button and verify that landed to home page successfully
Workflow: Navigate to Home → Click Contact Us → Fill Form → Submit → Verify Success
"""

import pytest

import logging
import os
from src.pages.home_page import HomePage
from src.pages.contact_page import ContactPage

logger = logging.getLogger(__name__)


class TestContactUsTC06:
    """Test suite for Contact Us form - TC06"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_contact_us_form_submission(self, driver, base_url, action_delay):
        """Test Contact Us form submission workflow"""
        
        home_page = HomePage(driver)
        contact_page = ContactPage(driver)
        
        logger.info("Step 1: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 2: Verifying home page is visible")
        assert driver.title
        logger.info(f"Home page title: {driver.title}")
        action_delay(1)
        
        logger.info("Step 3: Clicking Contact Us button")
        home_page.click_contact_us()
        action_delay(2)
        driver.execute_script("window.scrollTo(0, 0);")
        action_delay(0.5)
        
        logger.info("Step 4: Verifying GET IN TOUCH heading")
        assert contact_page.verify_get_in_touch_heading()
        action_delay(1)
        
        logger.info("Step 5: Entering form information")
        contact_page.enter_name("Test User")
        action_delay(0.5)
        contact_page.enter_email("testuser@example.com")
        action_delay(0.5)
        contact_page.enter_subject("Test Subject")
        action_delay(0.5)
        contact_page.enter_message("This is a test message for contact form submission.")
        action_delay(1)
        
        logger.info("Step 6: Uploading file")
        test_file_path = os.path.join(
            os.path.dirname(__file__), 
            "..", 
            "test_data", 
            "contact_upload.txt"
        )
        test_file_path = os.path.abspath(test_file_path)
        
        if os.path.exists(test_file_path):
            logger.info(f"Uploading file: {test_file_path}")
            contact_page.upload_file(test_file_path)
            action_delay(1)
        else:
            logger.warning(f"Test file not found at {test_file_path}")
        
        logger.info("Step 7: Clicking Submit button")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        action_delay(0.5)
        contact_page.click_submit()
        action_delay(3)
        
        logger.info("Step 8: Handling alert popup")
        contact_page.handle_alert_popup()
        action_delay(2)
        
        logger.info("Step 9: Verifying success message")
        success_visible = contact_page.is_success_message_visible()
        assert success_visible
        logger.info("Success message verified")
        
        logger.info("Step 10: Clicking Home button")
        home_page.click_element(home_page.home_locators.HOME_LINK)
        action_delay(2)
        assert "automationexercise.com" in driver.current_url
        logger.info("Contact Us test completed successfully")
