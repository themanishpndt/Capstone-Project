"""
Locators for Login Page
"""

from selenium.webdriver.common.by import By


class LoginLocators:
    """Login page element locators"""
    
    # URL
    LOGIN_URL = "https://automationexercise.com/login"
    SIGNUP_URL = "https://automationexercise.com/signup"
    
    # Login form
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    
    # Sign Up form
    SIGNUP_NAME_INPUT = (By.NAME, "name")
    SIGNUP_EMAIL_INPUT = (By.NAME, "email")
    SIGNUP_PASSWORD_INPUT = (By.NAME, "password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Signup')]")
    
    # Registration form fields
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Register')]")
    
    # Links
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    SIGN_UP_LINK = (By.XPATH, "//a[contains(text(), 'Signup')]")
    
    # Error messages
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    EMAIL_ERROR = (By.XPATH, "//span[@class='error' and contains(text(), 'email')]")
    PASSWORD_ERROR = (By.XPATH, "//span[@class='error' and contains(text(), 'password')]")
    
    # Remember me and other options
    REMEMBER_ME_CHECKBOX = (By.ID, "remember_me")
    
    # Success messages
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    LOGIN_SUCCESS_TEXT = (By.XPATH, "//span[contains(text(), 'logged in successfully')]")

