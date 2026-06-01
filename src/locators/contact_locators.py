"""
Locators for Contact Us Page
"""

from selenium.webdriver.common.by import By


class ContactLocators:
    """Contact Us page element locators"""
    
    # URL
    CONTACT_URL = "https://automationexercise.com/contact_us"
    
    # Page title
    CONTACT_TITLE = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    
    # Form fields
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_TEXTAREA = (By.ID, "message")
    FILE_INPUT = (By.NAME, "upload_file")
    
    # Buttons
    SUBMIT_BUTTON = (By.ID, "contact-us-form")
    
    # Success message
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success']")
    SUCCESS_MESSAGE_TEXT = (By.XPATH, "//span[contains(text(), 'Success! Your details have been submitted successfully.')]")
    
    # Form validation
    NAME_ERROR = (By.XPATH, "//input[@name='name']/following-sibling::span[@class='help-block']")
    EMAIL_ERROR = (By.XPATH, "//input[@name='email']/following-sibling::span[@class='help-block']")
    MESSAGE_ERROR = (By.XPATH, "//textarea[@id='message']/following-sibling::span[@class='help-block']")
