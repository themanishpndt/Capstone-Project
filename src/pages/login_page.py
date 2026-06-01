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
        try:
            # Try to find error message element
            try:
                return self.get_text(self.common_locators.ERROR_MESSAGE)
            except:
                # If class-based locator fails, use JavaScript to find any error text
                error_text = self.driver.execute_script("""
                    // Look for common error message patterns
                    const pageText = document.body.innerText.toLowerCase();
                    if (pageText.includes('your email or password is incorrect')) {
                        return 'Your email or password is incorrect!';
                    }
                    if (pageText.includes('invalid email')) {
                        return 'Invalid email address';
                    }
                    if (pageText.includes('error')) {
                        return 'Error found on page';
                    }
                    return null;
                """)
                return error_text if error_text else "No specific error found"
        except Exception as e:
            self.logger.warning(f"Could not get error message: {e}")
            return None
    
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
            # Use JavaScript to check if the text exists on the page
            result = self.driver.execute_script("""
                const bodyText = document.body.innerText;
                return bodyText.includes('logged in successfully');
            """)
            self.logger.info(f"Login success message visible (via JavaScript): {result}")
            return result
        except Exception as e:
            self.logger.warning(f"Could not verify login success: {e}")
            return False
    
    # Registration form methods
    def is_account_info_visible(self):
        """Verify ENTER ACCOUNT INFORMATION section is visible"""
        try:
            # Use JavaScript to check if the text exists on the page
            result = self.driver.execute_script("""
                const bodyText = document.body.innerText;
                return bodyText.includes('ENTER ACCOUNT INFORMATION');
            """)
            self.logger.info(f"Account info heading visible (via JavaScript): {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error checking account info visibility: {e}")
            return False
    
    def select_title_mr(self):
        """Select Mr. title"""
        self.click_element(self.locators.TITLE_MR_RADIO)
        self.logger.info("Selected Title: Mr.")
    
    def select_title_mrs(self):
        """Select Mrs. title"""
        self.click_element(self.locators.TITLE_MRS_RADIO)
        self.logger.info("Selected Title: Mrs.")
    
    def enter_reg_name(self, name):
        """Enter name in registration form"""
        self.enter_text(self.locators.NAME_INPUT, name)
        self.logger.info(f"Entered registration name: {name}")
    
    def enter_reg_email(self, email):
        """Enter email in registration form"""
        self.enter_text(self.locators.REG_EMAIL_INPUT, email)
        self.logger.info(f"Entered registration email: {email}")
    
    def enter_reg_password(self, password):
        """Enter password in registration form"""
        self.enter_text(self.locators.REG_PASSWORD_INPUT, password)
        self.logger.info("Entered registration password")
    
    def select_date_of_birth(self, day, month, year):
        """Select date of birth from dropdown menus"""
        from selenium.webdriver.support.select import Select
        
        # Select day
        day_dropdown = self.find_element(self.locators.DATE_OF_BIRTH_DAY)
        Select(day_dropdown).select_by_value(day)
        self.logger.info(f"Selected day: {day}")
        
        # Select month - try both zero-padded and regular values
        month_dropdown = self.find_element(self.locators.DATE_OF_BIRTH_MONTH)
        try:
            Select(month_dropdown).select_by_value(month)
        except:
            # Try without zero padding (e.g., "5" instead of "05")
            month_str = str(int(month))
            Select(month_dropdown).select_by_value(month_str)
        self.logger.info(f"Selected month: {month}")
        
        # Select year
        year_dropdown = self.find_element(self.locators.DATE_OF_BIRTH_YEAR)
        Select(year_dropdown).select_by_value(year)
        self.logger.info(f"Selected year: {year}")
    
    def check_newsletter(self):
        """Check newsletter checkbox"""
        self.click_element(self.locators.NEWSLETTER_CHECKBOX)
        self.logger.info("Checked newsletter checkbox")
    
    def check_special_offers(self):
        """Check special offers checkbox"""
        self.click_element(self.locators.SPECIAL_OFFERS_CHECKBOX)
        self.logger.info("Checked special offers checkbox")
    
    def enter_company(self, company):
        """Enter company name"""
        self.enter_text(self.locators.COMPANY_INPUT, company)
        self.logger.info(f"Entered company: {company}")
    
    def enter_address(self, address):
        """Enter address"""
        self.enter_text(self.locators.ADDRESS_INPUT, address)
        self.logger.info(f"Entered address: {address}")
    
    def enter_address2(self, address2):
        """Enter address 2"""
        self.enter_text(self.locators.ADDRESS2_INPUT, address2)
        self.logger.info(f"Entered address 2: {address2}")
    
    def select_country(self, country):
        """Select country from dropdown"""
        from selenium.webdriver.support.select import Select
        dropdown = self.find_element(self.locators.COUNTRY_DROPDOWN)
        Select(dropdown).select_by_value(country)
        self.logger.info(f"Selected country: {country}")
    
    def enter_state(self, state):
        """Enter state"""
        self.enter_text(self.locators.STATE_INPUT, state)
        self.logger.info(f"Entered state: {state}")
    
    def enter_city(self, city):
        """Enter city"""
        self.enter_text(self.locators.CITY_INPUT, city)
        self.logger.info(f"Entered city: {city}")
    
    def enter_zipcode(self, zipcode):
        """Enter zipcode"""
        self.enter_text(self.locators.ZIPCODE_INPUT, zipcode)
        self.logger.info(f"Entered zipcode: {zipcode}")
    
    def enter_mobile_number(self, mobile):
        """Enter mobile number"""
        self.enter_text(self.locators.MOBILE_NUMBER_INPUT, mobile)
        self.logger.info(f"Entered mobile number: {mobile}")
    
    def click_create_account(self):
        """Click Create Account button"""
        self.click_element(self.locators.CREATE_ACCOUNT_BUTTON)
        self.logger.info("Clicked Create Account button")
    
    def is_account_created_visible(self):
        """Verify ACCOUNT CREATED message is visible"""
        try:
            # Use JavaScript to check if the text exists on the page
            result = self.driver.execute_script("""
                const bodyText = document.body.innerText;
                return bodyText.includes('ACCOUNT CREATED');
            """)
            self.logger.info(f"Account created message visible (via JavaScript): {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error checking account created visibility: {e}")
            return False
    
    def click_continue(self):
        """Click Continue button"""
        self.click_element(self.locators.CONTINUE_BUTTON)
        self.logger.info("Clicked Continue button")
    
    def is_logged_in_visible(self):
        """Verify 'Logged in as' message is visible"""
        try:
            # Try to close any modal ads first
            try:
                from selenium.webdriver.common.by import By
                close_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Close')]")
                if close_buttons:
                    import time
                    self.driver.execute_script("arguments[0].click();", close_buttons[0])
                    time.sleep(1)
            except:
                pass
            
            # Use JavaScript to check if the text exists on the page
            result = self.driver.execute_script("""
                const bodyText = document.body.innerText;
                return bodyText.includes('Logged in as');
            """)
            self.logger.info(f"Logged in message visible (via JavaScript): {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error checking logged in visibility: {e}")
            return False
    
    def click_delete_account(self):
        """Click Delete Account button"""
        self.click_element(self.locators.DELETE_ACCOUNT_BUTTON)
        self.logger.info("Clicked Delete Account button")
    
    def is_account_deleted_visible(self):
        """Verify ACCOUNT DELETED message is visible"""
        try:
            # Use JavaScript to check if the text exists on the page
            result = self.driver.execute_script("""
                const bodyText = document.body.innerText;
                return bodyText.includes('ACCOUNT DELETED');
            """)
            self.logger.info(f"Account deleted message visible (via JavaScript): {result}")
            return result
        except Exception as e:
            self.logger.error(f"Error checking account deleted visibility: {e}")
            return False

