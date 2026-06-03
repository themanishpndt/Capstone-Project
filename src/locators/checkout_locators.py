"""
Locators for Checkout Page
"""

from selenium.webdriver.common.by import By


class CheckoutLocators:
    """Checkout page element locators"""
    
    # URL
    CHECKOUT_URL = "https://automationexercise.com/checkout"
    
    # Shipping address
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    ADDRESS_INPUT = (By.NAME, "address1")
    CITY_INPUT = (By.NAME, "city")
    STATE_INPUT = (By.NAME, "state")
    ZIP_CODE_INPUT = (By.NAME, "zipcode")
    COUNTRY_INPUT = (By.NAME, "country")
    
    # Billing and Delivery sections
    BILLING_ADDRESS_SECTION = (By.ID, "address_invoice")
    DELIVERY_ADDRESS_SECTION = (By.ID, "address_delivery")
    
    # Billing address
    SAME_AS_SHIPPING_CHECKBOX = (By.ID, "same-as-shipping")
    
    # Shipping method
    SHIPPING_METHOD_RADIO = (By.NAME, "shipping_method")
    SHIPPING_COST = (By.CLASS_NAME, "shipping-cost")
    
    # Payment method
    PAYMENT_METHOD_RADIO = (By.NAME, "payment_method")
    
    # Credit card details
    CARD_NUMBER_INPUT = (By.NAME, "card_number")
    CARD_EXPIRY_MONTH_INPUT = (By.NAME, "expiry_month")
    CARD_EXPIRY_YEAR_INPUT = (By.NAME, "expiry_year")
    CARD_EXPIRY_INPUT = (By.XPATH, "//input[@name='card_expiry' or @name='expiry']")
    CARD_CVC_INPUT = (By.NAME, "cvc")
    CARD_NAME_INPUT = (By.NAME, "name_on_card")
    
    # Order summary
    ORDER_TOTAL = (By.XPATH, "//h4/strong[contains(text(), 'Total')]")
    ORDER_ITEMS = (By.XPATH, "//tr[starts-with(@id, 'product-')]")
    
    # Order comment
    ORDER_COMMENT_TEXTAREA = (By.XPATH, "//textarea[@name='message' or @name='order_comment' or @id='order_comment']")
    ORDER_COMMENT = ORDER_COMMENT_TEXTAREA
    
    # Buttons
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[contains(text(), 'Place Order')] | //button[contains(text(), 'Place Order')]")
    BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Back')]")
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[contains(text(), 'Download Invoice')]")
    REGISTER_LOGIN_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'modal')]//a[contains(., 'Register') or contains(., 'Login')]"
        " | //a[contains(., 'Register / Login')]"
        " | //a[contains(text(), 'Signup / Login')]"
    )
    PAY_AND_CONFIRM_BUTTON = (By.XPATH, "//button[@data-qa='pay-button' or @id='submit' or contains(text(), 'Pay') or contains(text(), 'Confirm')] | //input[@value='Pay and Confirm Order']")
    
    # Confirmation
    ORDER_CONFIRMATION_MESSAGE = (By.XPATH, "//*[contains(text(), 'Congratulations') or contains(text(), 'order has been confirmed')]")
    ORDER_NUMBER = (By.XPATH, "//span[@class='order-id']")
    
    # Registration during checkout
    REGISTER_NAME_INPUT = (By.NAME, "name")
    REGISTER_EMAIL_INPUT = (By.NAME, "email")
    REGISTER_PASSWORD_INPUT = (By.NAME, "password")
    REGISTER_DURING_CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Account')]")

