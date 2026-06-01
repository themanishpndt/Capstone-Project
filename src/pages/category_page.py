"""
Category Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.category_locators import CategoryLocators


class CategoryPage(BasePage):
    """Category page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()
    
    def navigate_to_products(self):
        """Navigate to products page"""
        self.navigate_to(self.locators.CATEGORIES_URL)
        self.logger.info("Navigated to products page")
    
    def click_women_category(self):
        """Click on Women category"""
        self.click_element(self.locators.WOMEN_CATEGORY)
        self.logger.info("Clicked on Women category")
    
    def click_men_category(self):
        """Click on Men category"""
        self.click_element(self.locators.MEN_CATEGORY)
        self.logger.info("Clicked on Men category")
    
    def click_kids_category(self):
        """Click on Kids category"""
        self.click_element(self.locators.KIDS_CATEGORY)
        self.logger.info("Clicked on Kids category")
    
    def click_women_dress_subcategory(self):
        """Click on Women > Dress subcategory"""
        self.click_element(self.locators.WOMEN_DRESS_SUBCATEGORY)
        self.logger.info("Clicked on Women > Dress subcategory")
    
    def click_women_tops_subcategory(self):
        """Click on Women > Tops subcategory"""
        self.click_element(self.locators.WOMEN_TOPS_SUBCATEGORY)
        self.logger.info("Clicked on Women > Tops subcategory")
    
    def click_women_saree_subcategory(self):
        """Click on Women > Saree subcategory"""
        self.click_element(self.locators.WOMEN_SAREE_SUBCATEGORY)
        self.logger.info("Clicked on Women > Saree subcategory")
    
    def click_men_shirts_subcategory(self):
        """Click on Men > Shirts subcategory"""
        self.click_element(self.locators.MEN_SHIRTS_SUBCATEGORY)
        self.logger.info("Clicked on Men > Shirts subcategory")
    
    def click_men_tshirts_subcategory(self):
        """Click on Men > Tshirts subcategory"""
        self.click_element(self.locators.MEN_TSHIRTS_SUBCATEGORY)
        self.logger.info("Clicked on Men > Tshirts subcategory")
    
    def click_kids_dress_subcategory(self):
        """Click on Kids > Dress subcategory"""
        self.click_element(self.locators.KIDS_DRESS_SUBCATEGORY)
        self.logger.info("Clicked on Kids > Dress subcategory")
    
    def get_product_count(self):
        """Get number of products displayed in category"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        count = len(products)
        self.logger.info(f"Found {count} products in category")
        return count
    
    def get_product_names(self):
        """Get list of product names in category"""
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
    
    def get_category_title(self):
        """Get category title"""
        try:
            title = self.get_text(self.locators.CATEGORY_TITLE)
            self.logger.info(f"Category title: {title}")
            return title
        except Exception as e:
            self.logger.error(f"Failed to get category title: {e}")
            return None
    
    def click_first_product(self):
        """Click on first product in category"""
        products = self.find_elements(self.locators.PRODUCT_ITEMS)
        if products:
            first_product_link = products[0].find_element(*self.locators.PRODUCT_LINK)
            first_product_link.click()
            self.logger.info("Clicked on first product")
    
    def verify_category_page_loaded(self):
        """Verify category page is loaded with products"""
        is_loaded = self.get_product_count() > 0
        self.logger.info(f"Category page loaded: {is_loaded}")
        return is_loaded
