"""
Home Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.home_locators import HomeLocators
from src.locators.subscription_locators import SubscriptionLocators
from src.locators.common_locators import CommonLocators
from src.locators.login_locators import LoginLocators


class HomePage(BasePage):
    """Home page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.home_locators = HomeLocators()
        self.subscription_locators = SubscriptionLocators()
        self.common_locators = CommonLocators()
        self.login_locators = LoginLocators()
    
    def navigate_to_home(self):
        """Navigate to home page"""
        self.navigate_to(self.home_locators.HOME_URL)
        self.logger.info("Navigated to home page")
    
    def click_signup_login(self):
        """Click on Signup/Login link"""
        self.click_element(self.home_locators.SIGNUP_LOGIN_LINK)
        self.logger.info("Clicked on Signup/Login link")
    
    def click_products(self):
        """Click on Products link"""
        self.click_element(self.home_locators.PRODUCTS_LINK)
        self.logger.info("Clicked on Products link")
    
    def click_cart(self):
        """Click on Cart link"""
        self.click_element(self.home_locators.CART_LINK)
        self.logger.info("Clicked on Cart link")
    
    def click_test_cases(self):
        """Click on Test Cases link"""
        self.click_element(self.home_locators.TEST_CASES_LINK)
        self.logger.info("Clicked on Test Cases link")
    
    def click_contact_us(self):
        """Click on Contact Us link"""
        self.click_element(self.home_locators.CONTACT_US_LINK)
        self.logger.info("Clicked on Contact Us link")
    
    def verify_logged_in_user(self, expected_email):
        """Verify user is logged in"""
        logged_in_text = self.get_text(self.home_locators.LOGGED_IN_USER_TEXT)
        is_logged_in = expected_email in logged_in_text
        self.logger.info(f"User logged in verification: {is_logged_in}")
        return is_logged_in
    
    def click_logout(self):
        """Click logout link"""
        self.click_element(self.home_locators.LOGOUT_LINK)
        self.logger.info("Clicked logout link")
    
    def click_delete_account(self):
        """Click delete account link"""
        self.click_element(self.login_locators.DELETE_ACCOUNT_BUTTON)
        self.logger.info("Clicked delete account button")
    
    def subscribe_email_home(self, email):
        """Subscribe using email in home page section"""
        self.enter_text(self.subscription_locators.SUBSCRIPTION_EMAIL_INPUT, email)
        self.click_element(self.subscription_locators.SUBSCRIPTION_BUTTON)
        self.logger.info(f"Subscribed with email: {email} in home section")
    
    def is_subscription_success_visible(self):
        """Check if subscription success message is visible"""
        is_visible = self.is_element_visible(self.subscription_locators.SUBSCRIPTION_SUCCESS_MESSAGE)
        self.logger.info(f"Subscription success message visible: {is_visible}")
        return is_visible
    
    def subscribe_email_footer(self, email):
        """Subscribe using email in footer"""
        self.enter_text(self.subscription_locators.FOOTER_SUBSCRIPTION_EMAIL, email)
        self.click_element(self.subscription_locators.FOOTER_SUBSCRIPTION_BUTTON)
        self.logger.info(f"Subscribed with email: {email} in footer")
    
    def is_footer_subscription_success_visible(self):
        """Check if footer subscription success message is visible"""
        is_visible = self.is_element_visible(self.subscription_locators.FOOTER_SUBSCRIPTION_SUCCESS)
        self.logger.info(f"Footer subscription success message visible: {is_visible}")
        return is_visible
    
    def get_recommended_products_count(self):
        """Get count of recommended products"""
        products = self.find_elements(self.home_locators.RECOMMENDED_PRODUCTS)
        count = len(products)
        self.logger.info(f"Found {count} recommended products")
        return count
    
    def add_first_recommended_product_to_cart(self):
        """Add first recommended product to cart"""
        buttons = self.find_elements(self.home_locators.RECOMMENDED_ADD_TO_CART_BUTTONS)
        visible_buttons = [button for button in buttons if button.is_displayed()]
        if not visible_buttons:
            raise AssertionError("No visible recommended add-to-cart buttons found")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", visible_buttons[0])
        self.driver.execute_script("arguments[0].click();", visible_buttons[0])
        if self.is_element_visible(self.home_locators.CART_MODAL):
            self.click_element(self.home_locators.CART_MODAL_VIEW_CART_LINK)
        self.logger.info("Added first recommended product to cart")
    
    def scroll_to_footer(self):
        """Scroll to footer section"""
        footer = self.find_element(self.home_locators.FOOTER_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        self.logger.info("Scrolled to footer")
    
    def scroll_up_using_arrow(self):
        """Scroll to top using scroll up arrow button"""
        scroll_button = self.find_element(self.home_locators.SCROLL_TOP_ARROW)
        scroll_button.click()
        self.logger.info("Scrolled to top using arrow button")
    
    def scroll_up_without_arrow(self):
        """Scroll to top without using arrow button"""
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.logger.info("Scrolled to top without arrow button")
    
    def is_scroll_button_visible(self):
        """Check if scroll up button is visible"""
        is_visible = self.is_element_visible(self.home_locators.SCROLL_TOP_ARROW)
        self.logger.info(f"Scroll up button visible: {is_visible}")
        return is_visible
    
    def verify_home_page_loaded(self):
        """Verify home page is loaded"""
        is_loaded = self.is_element_visible(self.home_locators.FEATURED_ITEMS_SECTION)
        self.logger.info(f"Home page loaded: {is_loaded}")
        return is_loaded
