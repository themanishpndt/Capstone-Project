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
    
    # Brand items - using more flexible selectors
    POLO_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Polo')]")
    H_M_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'H&M') or contains(., 'H & M')]")
    MADAME_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Madame')]")
    MANGO_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Mango')]")
    ALLEN_SOLLY_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Allen')]")
    BABYHUG_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Babyhug')]")
    BIBA_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Biba')]")
    AEROPOSTALE_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Aeropostale')]")
    JOHN_MILLER_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'John Miller')]")
    NOVA_BRAND = (By.XPATH, "//div[contains(@class, 'brands-name')]//a[contains(., 'Nova')]")
    
    # Products in brand
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='product-image-wrapper']")
    PRODUCT_NAME = (By.XPATH, ".//p[@class='product-name']")
    PRODUCT_PRICE = (By.XPATH, ".//h2[contains(@class, 'price')]")
    PRODUCT_LINK = (By.XPATH, ".//a[contains(@href, '/product_details')]")
    
    # Brand title/header
    BRAND_TITLE = (By.XPATH, "//h2[@class='title text-center']")
