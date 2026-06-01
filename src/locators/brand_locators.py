"""
Locators for Brand Page
"""

from selenium.webdriver.common.by import By


class BrandLocators:
    """Brand page element locators"""
    
    # URL (dynamic based on brand)
    BRANDS_URL = "https://automationexercise.com/product"
    
    # Left sidebar brands
    BRANDS_SIDEBAR = (By.CLASS_NAME, "left-sidebar")
    BRAND_LIST = (By.XPATH, "//div[@class='left-sidebar']//li")
    
    # Brand items
    POLO_BRAND = (By.XPATH, "//a[contains(text(), 'Polo')]")
    H_M_BRAND = (By.XPATH, "//a[contains(text(), 'H&M')]")
    MADAME_BRAND = (By.XPATH, "//a[contains(text(), 'Madame')]")
    MANGO_BRAND = (By.XPATH, "//a[contains(text(), 'Mango')]")
    ALLEN_SOLLY_BRAND = (By.XPATH, "//a[contains(text(), 'Allen Solly')]")
    BABYHUG_BRAND = (By.XPATH, "//a[contains(text(), 'Babyhug')]")
    BIBA_BRAND = (By.XPATH, "//a[contains(text(), 'Biba')]")
    AEROPOSTALE_BRAND = (By.XPATH, "//a[contains(text(), 'Aeropostale')]")
    JOHN_MILLER_BRAND = (By.XPATH, "//a[contains(text(), 'John Miller')]")
    NOVA_BRAND = (By.XPATH, "//a[contains(text(), 'Nova')]")
    
    # Products in brand
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='product-image-wrapper']")
    PRODUCT_NAME = (By.XPATH, ".//p[@class='product-name']")
    PRODUCT_PRICE = (By.XPATH, ".//h2[contains(@class, 'price')]")
    PRODUCT_LINK = (By.XPATH, ".//a[contains(@href, '/product_details')]")
    
    # Brand title/header
    BRAND_TITLE = (By.XPATH, "//h2[@class='title text-center']")
