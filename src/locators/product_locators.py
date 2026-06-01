"""
Locators for Product Page
"""

from selenium.webdriver.common.by import By


class ProductLocators:
    """Product page element locators"""
    
    # URL
    PRODUCTS_URL = "https://automationexercise.com/products"
    
    # Product list
    PRODUCT_ITEMS = (By.XPATH, "//div[@class='product-image-wrapper']")
    VIEW_PRODUCT_LINKS = (By.XPATH, "//a[contains(@href, '/product_details/') and contains(., 'View Product')]")
    PRODUCT_NAME = (By.XPATH, ".//div[contains(@class, 'productinfo')]//p")
    PRODUCT_PRICE = (By.XPATH, ".//h2")
    PRODUCT_RATING = (By.XPATH, ".//div[@class='rating']")
    
    # Add to cart
    ADD_TO_CART_BUTTON = (By.XPATH, ".//a[@class='btn btn-default add-to-cart']")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//a[contains(@class, 'add-to-cart')]")
    CART_MODAL = (By.ID, "cartModal")
    CART_MODAL_VIEW_CART_LINK = (By.XPATH, "//div[@id='cartModal']//u[contains(text(), 'View Cart')]/ancestor::a")
    CART_MODAL_CONTINUE_BUTTON = (By.XPATH, "//div[@id='cartModal']//button[contains(text(), 'Continue Shopping')]")
    
    # Search and filter
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    
    # Filters
    PRICE_FILTER_MIN = (By.ID, "price-min")
    PRICE_FILTER_MAX = (By.ID, "price-max")
    CATEGORY_FILTER = (By.ID, "category")
    RATING_FILTER = (By.ID, "rating")
    APPLY_FILTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Apply Filters')]")
    
    # Sorting
    SORT_DROPDOWN = (By.ID, "sort-by")
    
    # Pagination
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Next page']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@aria-label='Previous page']")
    PAGE_NUMBER = (By.CLASS_NAME, "page-number")

