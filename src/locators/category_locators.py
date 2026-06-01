"""
Locators for Category Page
"""

from selenium.webdriver.common.by import By


class CategoryLocators:
    """Category page element locators"""
    
    # URL (dynamic based on category)
    CATEGORIES_URL = "https://automationexercise.com/product"
    
    # Left sidebar categories
    CATEGORIES_SIDEBAR = (By.CLASS_NAME, "left-sidebar")
    CATEGORY_LIST = (By.XPATH, "//div[@class='left-sidebar']//li")
    
    # Category items (specific categories)
    WOMEN_CATEGORY = (By.XPATH, "//a[contains(text(), 'Women')]")
    MEN_CATEGORY = (By.XPATH, "//a[contains(text(), 'Men')]")
    KIDS_CATEGORY = (By.XPATH, "//a[contains(text(), 'Kids')]")
    
    # Sub-categories
    WOMEN_DRESS_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Dress')]")
    WOMEN_TOPS_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Tops')]")
    WOMEN_SAREE_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Saree')]")
    MEN_SHIRTS_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Shirts')]")
    MEN_TSHIRTS_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Tshirts')]")
    KIDS_DRESS_SUBCATEGORY = (By.XPATH, "//a[contains(text(), 'Dress')]")
    
    # Products in category
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='product-image-wrapper']")
    PRODUCT_NAME = (By.XPATH, ".//p[@class='product-name']")
    PRODUCT_PRICE = (By.XPATH, ".//h2[contains(@class, 'price')]")
    PRODUCT_LINK = (By.XPATH, ".//a[contains(@href, '/product_details')]")
    
    # Category title/header
    CATEGORY_TITLE = (By.XPATH, "//h2[@class='title text-center']")
