"""
Brand Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.brand_locators import BrandLocators


class BrandPage(BasePage):
    """Brand page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = BrandLocators()
    
    def navigate_to_products(self):
        """Navigate to products page"""
        self.navigate_to(self.locators.BRANDS_URL)
        self.logger.info("Navigated to products page")
    
    def click_polo_brand(self):
        """Click on Polo brand"""
        self.click_element(self.locators.POLO_BRAND)
        self.logger.info("Clicked on Polo brand")
    
    def click_h_m_brand(self):
        """Click on H&M brand"""
        self.click_element(self.locators.H_M_BRAND)
        self.logger.info("Clicked on H&M brand")
    
    def click_madame_brand(self):
        """Click on Madame brand"""
        self.click_element(self.locators.MADAME_BRAND)
        self.logger.info("Clicked on Madame brand")
    
    def click_mango_brand(self):
        """Click on Mango brand"""
        self.click_element(self.locators.MANGO_BRAND)
        self.logger.info("Clicked on Mango brand")
    
    def click_allen_solly_brand(self):
        """Click on Allen Solly brand"""
        self.click_element(self.locators.ALLEN_SOLLY_BRAND)
        self.logger.info("Clicked on Allen Solly brand")
    
    def click_babyhug_brand(self):
        """Click on Babyhug brand"""
        self.click_element(self.locators.BABYHUG_BRAND)
        self.logger.info("Clicked on Babyhug brand")
    
    def click_biba_brand(self):
        """Click on Biba brand"""
        self.click_element(self.locators.BIBA_BRAND)
        self.logger.info("Clicked on Biba brand")
    
    def click_aeropostale_brand(self):
        """Click on Aeropostale brand"""
        self.click_element(self.locators.AEROPOSTALE_BRAND)
        self.logger.info("Clicked on Aeropostale brand")
    
    def click_john_miller_brand(self):
        """Click on John Miller brand"""
        self.click_element(self.locators.JOHN_MILLER_BRAND)
        self.logger.info("Clicked on John Miller brand")
    
    def click_nova_brand(self):
        """Click on Nova brand"""
        self.click_element(self.locators.NOVA_BRAND)
        self.logger.info("Clicked on Nova brand")
    
    def get_product_count(self):
        """Get number of products displayed for brand"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        count = len(products)
        self.logger.info(f"Found {count} products for brand")
        return count
    
    def get_product_names(self):
        """Get list of product names for brand"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        names = []
        for product in products:
            try:
                name_element = product.find_element(*self.locators.PRODUCT_NAME)
                names.append(name_element.text)
            except Exception as e:
                self.logger.warning(f"Failed to get product name: {e}")
        self.logger.info(f"Retrieved {len(names)} product names")
        return names
    
    def get_brand_title(self):
        """Get brand title"""
        try:
            title = self.get_text(self.locators.BRAND_TITLE)
            self.logger.info(f"Brand title: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Failed to get brand title: {e}")
            return None
    
    def click_first_product(self):
        """Click on first product for brand"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        if products:
            first_product_link = products[0].find_element(*self.locators.PRODUCT_LINK)
            first_product_link.click()
            self.logger.info("Clicked on first product")
    
    def verify_brand_page_loaded(self):
        """Verify brand page is loaded with products"""
        is_loaded = self.get_product_count() > 0
        self.logger.info(f"Brand page loaded: {is_loaded}")
        return is_loaded
