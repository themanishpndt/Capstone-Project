"""
Locators for Review Page (Product Details with Reviews)
"""

from selenium.webdriver.common.by import By


class ReviewLocators:
    """Review/Product Details page element locators"""
    
    # URL (dynamic based on product)
    PRODUCT_DETAILS_URL = "https://automationexercise.com/product_details"
    
    # Product details section
    PRODUCT_IMAGE = (By.XPATH, "//div[@class='product-image']//img")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-details']//h2")
    PRODUCT_PRICE = (By.XPATH, "//span[@id='productPrice']")
    PRODUCT_RATING = (By.XPATH, "//div[@class='product-details']//b")
    PRODUCT_AVAILABILITY = (By.XPATH, "//p[contains(text(), 'Availability')]")
    PRODUCT_CONDITION = (By.XPATH, "//p[contains(text(), 'Condition')]")
    PRODUCT_SKU = (By.XPATH, "//p[contains(text(), 'SKU')]")
    
    # Reviews section
    REVIEWS_SECTION = (By.ID, "review")
    REVIEW_TAB = (By.XPATH, "//a[@href='#reviews']")
    
    # Review form fields
    REVIEW_NAME_INPUT = (By.ID, "name")
    REVIEW_EMAIL_INPUT = (By.ID, "email")
    REVIEW_TEXTAREA = (By.ID, "review")
    REVIEW_RATING_RADIO = (By.NAME, "rating")
    REVIEW_RATING_5_STAR = (By.XPATH, "//input[@name='rating'][@value='5']")
    
    # Review submission
    SUBMIT_REVIEW_BUTTON = (By.ID, "button-review")
    
    # Review success message
    REVIEW_SUCCESS_MESSAGE = (By.XPATH, "//span[contains(text(), 'Thank you for your review')]")
    
    # Existing reviews
    EXISTING_REVIEWS = (By.XPATH, "//div[@class='review-item']")
    REVIEW_NAME = (By.XPATH, ".//strong")
    REVIEW_RATING = (By.XPATH, ".//div[@class='rating']")
    REVIEW_TEXT = (By.XPATH, ".//p[@class='review']")
