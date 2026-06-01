"""
Locators for Invoice Page
"""

from selenium.webdriver.common.by import By


class InvoiceLocators:
    """Invoice page element locators"""
    
    # URL
    INVOICE_URL = "https://automationexercise.com/order_details"
    
    # Invoice header
    INVOICE_TITLE = (By.XPATH, "//h2[contains(text(), 'Invoice')]")
    INVOICE_NUMBER = (By.XPATH, "//span[contains(text(), 'Invoice #')]")
    INVOICE_DATE = (By.XPATH, "//span[contains(text(), 'Invoice Date')]")
    
    # Order details
    ORDER_NUMBER = (By.XPATH, "//span[contains(text(), 'Order #')]")
    ORDER_DATE = (By.XPATH, "//span[contains(text(), 'Order Date')]")
    
    # Shipping information
    SHIPPING_INFO = (By.XPATH, "//h4[contains(text(), 'Shipping Information')]")
    SHIPPING_ADDRESS = (By.XPATH, "//div[contains(text(), 'Shipping Address')]")
    
    # Billing information
    BILLING_INFO = (By.XPATH, "//h4[contains(text(), 'Billing Information')]")
    BILLING_ADDRESS = (By.XPATH, "//div[contains(text(), 'Billing Address')]")
    
    # Order items table
    ORDER_ITEMS_TABLE = (By.XPATH, "//table[@class='table table-bordered']")
    ORDER_ITEMS = (By.XPATH, "//table[@class='table table-bordered']//tr")
    ITEM_NAME = (By.XPATH, ".//td[1]")
    ITEM_QUANTITY = (By.XPATH, ".//td[2]")
    ITEM_PRICE = (By.XPATH, ".//td[3]")
    ITEM_TOTAL = (By.XPATH, ".//td[4]")
    
    # Order totals
    SUBTOTAL = (By.XPATH, "//td[contains(text(), 'Subtotal')]")
    SHIPPING_COST = (By.XPATH, "//td[contains(text(), 'Shipping')]")
    TAX = (By.XPATH, "//td[contains(text(), 'Tax')]")
    TOTAL = (By.XPATH, "//td[contains(text(), 'Total')]")
    TOTAL_AMOUNT = (By.XPATH, "//td[contains(text(), 'Total')]//following-sibling::td")
    
    # Buttons
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[contains(text(), 'Download Invoice')]")
    PRINT_BUTTON = (By.XPATH, "//button[contains(text(), 'Print')]")
    BACK_TO_ORDERS_BUTTON = (By.XPATH, "//a[contains(text(), 'Back to Orders')]")
