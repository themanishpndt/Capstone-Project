"""
Locators for Cart Page
"""

from selenium.webdriver.common.by import By


class CartLocators:
    """Shopping cart page element locators"""
    
    # URL
    CART_URL = "https://automationexercise.com/view_cart"
    
    # Cart items
    CART_ITEMS = (By.XPATH, "//tr[@class='active']")
    ITEM_NAME = (By.XPATH, ".//td[2]/h4/a")
    ITEM_PRICE = (By.XPATH, ".//td[3]")
    ITEM_QUANTITY = (By.XPATH, ".//td[4]/button")
    ITEM_TOTAL = (By.XPATH, ".//td[5]")
    
    # Quantity controls
    QUANTITY_INPUT = (By.XPATH, ".//td[4]//input")
    INCREASE_QUANTITY_BUTTON = (By.XPATH, ".//td[4]//button[contains(text(), '+')]")
    DECREASE_QUANTITY_BUTTON = (By.XPATH, ".//td[4]//button[contains(text(), '-')]")
    
    # Remove item
    REMOVE_ITEM_BUTTON = (By.XPATH, ".//td[6]//a")
    
    # Totals
    SUBTOTAL = (By.XPATH, "//tr[contains(td, 'Subtotal')]//td[2]")
    TAX = (By.XPATH, "//tr[contains(td, 'Tax')]//td[2]")
    TOTAL = (By.XPATH, "//tr[contains(td, 'Total')]//td[2]")
    
    # Discount/Coupon
    COUPON_INPUT = (By.ID, "coupon_code")
    APPLY_COUPON_BUTTON = (By.ID, "apply_coupon")
    
    # Checkout button
    CHECKOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Proceed To Checkout')]")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    
    # Empty cart message
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(), 'Cart is empty')]")

