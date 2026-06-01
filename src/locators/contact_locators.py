"""
Locators for Contact Us Page
"""

from selenium.webdriver.common.by import By


class ContactLocators:
    """Contact Us page element locators"""
    
    # URL
    CONTACT_URL = "https://automationexercise.com/contact_us"
    
    # Page title
    GET_IN_TOUCH_HEADING = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    CONTACT_TITLE = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    
    # Form fields
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    FILE_INPUT = (By.NAME, "upload_file")
    
    # Buttons
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUBMIT_BUTTON_ALT = (By.XPATH, "//input[@type='submit' and @value='Submit']")
    SUBMIT_BUTTON_FORM = (By.ID, "contact-us-form")
    
    # Success message
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.status.alert.alert-success")
    SUCCESS_MESSAGE_TEXT = (By.XPATH, "//div[@class='status alert alert-success']")
    
    # Form validation
    NAME_ERROR = (By.XPATH, "//input[@name='name']/following-sibling::span[@class='help-block']")
    EMAIL_ERROR = (By.XPATH, "//input[@name='email']/following-sibling::span[@class='help-block']")
    MESSAGE_ERROR = (By.XPATH, "//textarea[@id='message']/following-sibling::span[@class='help-block']")
