"""
Product Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.product_locators import ProductLocators


class ProductPage(BasePage):
    """Product page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()
    
    def search_product(self, product_name):
        """Search for a product"""
        self.enter_text(self.locators.SEARCH_INPUT, product_name)
        self.click_element(self.locators.SEARCH_BUTTON)
    
    def get_product_count(self):
        """Get number of products displayed"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        return len(products)

    def open_first_product_details(self):
        """Open the details page for the first displayed product."""
        product_links = self.find_elements(self.locators.VIEW_PRODUCT_LINKS)
        if not product_links:
            raise AssertionError("No product detail links found")

        product_url = product_links[0].get_attribute("href")
        if not product_url:
            raise AssertionError("First product detail link does not have an href")

        self.navigate_to(product_url)
        self.wait_for_url_contains("/product_details/")

    def add_first_product_to_cart(self, view_cart=False):
        """Add the first visible product to the cart."""
        buttons = self.find_elements(self.locators.ADD_TO_CART_BUTTONS)
        visible_buttons = [button for button in buttons if button.is_displayed()]
        if not visible_buttons:
            raise AssertionError("No visible add-to-cart buttons found")

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", visible_buttons[0])
        self.driver.execute_script("arguments[0].click();", visible_buttons[0])
        if self.is_element_visible(self.locators.CART_MODAL):
            modal_action = (
                self.locators.CART_MODAL_VIEW_CART_LINK
                if view_cart
                else self.locators.CART_MODAL_CONTINUE_BUTTON
            )
            self.click_element(modal_action)
    
    def get_product_names(self):
        """Get list of product names"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        names = []
        for product in products:
            name = product.find_element(*self.locators.PRODUCT_NAME).text
            names.append(name)
        return names
    
    def filter_by_price(self, min_price, max_price):
        """Filter products by price range"""
        self.enter_text(self.locators.PRICE_FILTER_MIN, str(min_price))
        self.enter_text(self.locators.PRICE_FILTER_MAX, str(max_price))
        self.click_element(self.locators.APPLY_FILTER_BUTTON)
    
    def filter_by_category(self, category):
        """Filter products by category"""
        category_element = self.find_element(self.locators.CATEGORY_FILTER)
        category_element.send_keys(category)
        self.click_element(self.locators.APPLY_FILTER_BUTTON)
    
    def sort_products(self, sort_option):
        """Sort products"""
        sort_element = self.find_element(self.locators.SORT_DROPDOWN)
        sort_element.send_keys(sort_option)
    
    def click_next_page(self):
        """Click next page button"""
        self.click_element(self.locators.NEXT_PAGE_BUTTON)
    
    def click_previous_page(self):
        """Click previous page button"""
        self.click_element(self.locators.PREVIOUS_PAGE_BUTTON)
    
    def get_first_product_price(self):
        """Get price of first product"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        if products:
            price = products[0].find_element(*self.locators.PRODUCT_PRICE).text
            return price
        return None
