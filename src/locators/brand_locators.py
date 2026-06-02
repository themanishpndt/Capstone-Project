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
    POLO_BRAND = (By.XPATH, "//a[contains(text(), 'Polo') or contains(@href, 'polo')]/ancestor::li//a | //li//a[normalize-space()='Polo']")
    H_M_BRAND = (By.XPATH, "//a[contains(text(), 'H&M') or contains(text(), 'H & M') or contains(@href, 'hm')]/ancestor::li//a | //li//a[contains(normalize-space(), 'H')]")
    MADAME_BRAND = (By.XPATH, "//a[contains(text(), 'Madame')]/ancestor::li//a | //li//a[normalize-space()='Madame']")
    MANGO_BRAND = (By.XPATH, "//a[contains(text(), 'Mango')]/ancestor::li//a | //li//a[normalize-space()='Mango']")
    ALLEN_SOLLY_BRAND = (By.XPATH, "//a[contains(text(), 'Allen')]/ancestor::li//a | //li//a[contains(normalize-space(), 'Allen')]")
    BABYHUG_BRAND = (By.XPATH, "//a[contains(text(), 'Babyhug')]/ancestor::li//a | //li//a[normalize-space()='Babyhug']")
    BIBA_BRAND = (By.XPATH, "//a[contains(text(), 'Biba')]/ancestor::li//a | //li//a[normalize-space()='Biba']")
    AEROPOSTALE_BRAND = (By.XPATH, "//a[contains(text(), 'Aeropostale')]/ancestor::li//a | //li//a[normalize-space()='Aeropostale']")
    JOHN_MILLER_BRAND = (By.XPATH, "//a[contains(text(), 'John Miller')]/ancestor::li//a | //li//a[contains(normalize-space(), 'John')]")
    NOVA_BRAND = (By.XPATH, "//a[contains(text(), 'Nova')]/ancestor::li//a | //li//a[normalize-space()='Nova']")
    
    # Products in brand
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='product-image-wrapper']")
    PRODUCT_NAME = (By.XPATH, ".//p[@class='product-name']")
    PRODUCT_PRICE = (By.XPATH, ".//h2[contains(@class, 'price')]")
    PRODUCT_LINK = (By.XPATH, ".//a[contains(@href, '/product_details')]")
    
    # Brand title/header
    BRAND_TITLE = (By.XPATH, "//h2[@class='title text-center']")
