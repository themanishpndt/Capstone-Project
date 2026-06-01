"""
Login Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.login_locators import LoginLocators
from src.locators.common_locators import CommonLocators


class LoginPage(BasePage):
    """Login page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()
        self.common_locators = CommonLocators()
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate_to(self.locators.LOGIN_URL)
        self.logger.info("Navigated to login page")
    
    def navigate_to_signup(self):
        """Navigate to signup page"""
        self.navigate_to(self.locators.SIGNUP_URL)
        self.logger.info("Navigated to signup page")
    
    def enter_email(self, email):
        """Enter email in email field"""
        self.enter_text(self.locators.EMAIL_INPUT, email)
        self.logger.info(f"Entered email: {email}")
    
    def enter_password(self, password):
        """Enter password in password field"""
        self.enter_text(self.locators.PASSWORD_INPUT, password)
        self.logger.info("Entered password")
    
    def click_login_button(self):
        """Click login button"""
        self.click_element(self.locators.LOGIN_BUTTON)
        self.logger.info("Clicked login button")
    
    def click_forgot_password(self):
        """Click forgot password link"""
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)
        self.logger.info("Clicked forgot password link")
    
    def click_sign_up(self):
        """Click sign up link"""
        self.click_element(self.locators.SIGN_UP_LINK)
        self.logger.info("Clicked sign up link")
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.common_locators.ERROR_MESSAGE)
    
    def is_login_button_displayed(self):
        """Check if login button is displayed"""
        return self.is_element_visible(self.locators.LOGIN_BUTTON)
    
    def login(self, email, password):
        """Complete login with email and password"""
        self.navigate_to_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.logger.info(f"Login completed for user: {email}")
    
    def check_remember_me(self):
        """Check remember me checkbox"""
        self.click_element(self.locators.REMEMBER_ME_CHECKBOX)
        self.logger.info("Checked remember me checkbox")
    
    def enter_signup_name(self, name):
        """Enter name in signup form"""
        self.enter_text(self.locators.SIGNUP_NAME_INPUT, name)
        self.logger.info(f"Entered signup name: {name}")
    
    def enter_signup_email(self, email):
        """Enter email in signup form"""
        self.enter_text(self.locators.SIGNUP_EMAIL_INPUT, email)
        self.logger.info(f"Entered signup email: {email}")
    
    def enter_signup_password(self, password):
        """Enter password in signup form"""
        self.enter_text(self.locators.SIGNUP_PASSWORD_INPUT, password)
        self.logger.info("Entered signup password")
    
    def click_signup_button(self):
        """Click signup button"""
        self.click_element(self.locators.SIGNUP_BUTTON)
        self.logger.info("Clicked signup button")
    
    def enter_first_name(self, first_name):
        """Enter first name in registration form"""
        self.enter_text(self.locators.FIRST_NAME_INPUT, first_name)
        self.logger.info(f"Entered first name: {first_name}")
    
    def enter_last_name(self, last_name):
        """Enter last name in registration form"""
        self.enter_text(self.locators.LAST_NAME_INPUT, last_name)
        self.logger.info(f"Entered last name: {last_name}")
    
    def click_register_button(self):
        """Click register button"""
        self.click_element(self.locators.REGISTER_BUTTON)
        self.logger.info("Clicked register button")
    
    def fill_registration_form(self, name, email, password, first_name, last_name):
        """Fill complete registration form"""
        self.navigate_to_signup()
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.enter_signup_password(password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.click_register_button()
        self.logger.info(f"Registration form filled for: {email}")
    
    def get_current_url(self):
        """Get current page URL"""
        current_url = self.driver.current_url
        self.logger.info(f"Current URL: {current_url}")
        return current_url
    
    def is_login_success_message_visible(self):
        """Check if login success message is visible"""
        try:
            return self.is_element_visible(self.locators.LOGIN_SUCCESS_TEXT)
        except Exception as e:
            self.logger.warning(f"Could not verify login success: {e}")
            return False

