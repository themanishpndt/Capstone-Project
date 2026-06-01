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
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_PASSWORD_INPUT = (By.NAME, "password")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
    # Registration form - Account Information
    ENTER_ACCOUNT_INFO_HEADING = (By.XPATH, "//*[contains(normalize-space(), 'ENTER ACCOUNT INFORMATION')]")
    TITLE_MR_RADIO = (By.ID, "id_gender1")
    TITLE_MRS_RADIO = (By.ID, "id_gender2")
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='password']")
    DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, "select[data-qa='days']")
    DATE_OF_BIRTH_MONTH = (By.CSS_SELECTOR, "select[data-qa='months']")
    DATE_OF_BIRTH_YEAR = (By.CSS_SELECTOR, "select[data-qa='years']")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")
    
    # Registration form - Address Information
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='first_name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='last_name']")
    COMPANY_INPUT = (By.CSS_SELECTOR, "input[data-qa='company']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-qa='address']")
    ADDRESS2_INPUT = (By.CSS_SELECTOR, "input[data-qa='address2']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select[data-qa='country']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-qa='state']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-qa='city']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, "input[data-qa='zipcode']")
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    
    # Buttons
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    CONTINUE_BUTTON = (By.XPATH, "//a[contains(text(), 'Continue')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(), 'Delete Account')]")
    
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
    ACCOUNT_CREATED_MESSAGE = (By.XPATH, "//h2[contains(text(), 'ACCOUNT CREATED')]")
    ACCOUNT_DELETED_MESSAGE = (By.XPATH, "//h2[contains(text(), 'ACCOUNT DELETED')]")
    LOGGED_IN_AS_MESSAGE = (By.XPATH, "//li[contains(text(), 'Logged in as')]")

