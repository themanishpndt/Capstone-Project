"""
Invoice Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.invoice_locators import InvoiceLocators


class InvoicePage(BasePage):
    """Invoice page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = InvoiceLocators()
    
    def navigate_to_order_details(self, order_id):
        """Navigate to order details page"""
        url = f"{self.locators.INVOICE_URL}/{order_id}"
        self.navigate_to(url)
        self.logger.info(f"Navigated to order details for order ID: {order_id}")
    
    def verify_invoice_title(self):
        """Verify invoice title is visible"""
        is_visible = self.is_element_visible(self.locators.INVOICE_TITLE)
        self.logger.info(f"Invoice title visible: {is_visible}")
        return is_visible
    
    def get_invoice_number(self):
        """Get invoice number"""
        try:
            invoice_num = self.get_text(self.locators.INVOICE_NUMBER)
            self.logger.info(f"Invoice number: {invoice_num}")
            return invoice_num
        except Exception as e:
            self.logger.error(f"Failed to get invoice number: {e}")
            return None
    
    def get_invoice_date(self):
        """Get invoice date"""
        try:
            invoice_date = self.get_text(self.locators.INVOICE_DATE)
            self.logger.info(f"Invoice date: {invoice_date}")
            return invoice_date
        except Exception as e:
            self.logger.error(f"Failed to get invoice date: {e}")
            return None
    
    def get_order_number(self):
        """Get order number"""
        try:
            order_num = self.get_text(self.locators.ORDER_NUMBER)
            self.logger.info(f"Order number: {order_num}")
            return order_num
        except Exception as e:
            self.logger.error(f"Failed to get order number: {e}")
            return None
    
    def get_order_date(self):
        """Get order date"""
        try:
            order_date = self.get_text(self.locators.ORDER_DATE)
            self.logger.info(f"Order date: {order_date}")
            return order_date
        except Exception as e:
            self.logger.error(f"Failed to get order date: {e}")
            return None
    
    def verify_shipping_info_visible(self):
        """Verify shipping information section is visible"""
        is_visible = self.is_element_visible(self.locators.SHIPPING_INFO)
        self.logger.info(f"Shipping info visible: {is_visible}")
        return is_visible
    
    def verify_billing_info_visible(self):
        """Verify billing information section is visible"""
        is_visible = self.is_element_visible(self.locators.BILLING_INFO)
        self.logger.info(f"Billing info visible: {is_visible}")
        return is_visible
    
    def get_order_items_count(self):
        """Get count of items in order"""
        items = self.find_elements(self.locators.ORDER_ITEMS)
        # Subtract 1 for header row
        count = max(0, len(items) - 1)
        self.logger.info(f"Order items count: {count}")
        return count
    
    def get_total_amount(self):
        """Get order total amount"""
        try:
            total_text = self.get_text(self.locators.TOTAL_AMOUNT)
            self.logger.info(f"Total amount: {total_text}")
            return total_text
        except Exception as e:
            self.logger.error(f"Failed to get total amount: {e}")
            return None
    
    def click_download_invoice(self):
        """Click download invoice button"""
        self.click_element(self.locators.DOWNLOAD_INVOICE_BUTTON)
        self.logger.info("Clicked download invoice button")
    
    def click_print(self):
        """Click print button"""
        try:
            self.click_element(self.locators.PRINT_BUTTON)
            self.logger.info("Clicked print button")
        except Exception as e:
            self.logger.warning(f"Failed to click print button: {e}")
    
    def click_back_to_orders(self):
        """Click back to orders button"""
        self.click_element(self.locators.BACK_TO_ORDERS_BUTTON)
        self.logger.info("Clicked back to orders button")
    
    def verify_invoice_page_loaded(self):
        """Verify invoice page is loaded"""
        is_loaded = self.verify_invoice_title() and self.verify_shipping_info_visible()
        self.logger.info(f"Invoice page loaded: {is_loaded}")
        return is_loaded
    
    def get_order_items_details(self):
        """Get details of all items in order"""
        items_details = []
        try:
            items = self.find_elements(self.locators.ORDER_ITEMS)
            for item in items[1:]:  # Skip header row
                try:
                    name = item.find_element(*self.locators.ITEM_NAME).text
                    quantity = item.find_element(*self.locators.ITEM_QUANTITY).text
                    price = item.find_element(*self.locators.ITEM_PRICE).text
                    total = item.find_element(*self.locators.ITEM_TOTAL).text
                    items_details.append({
                        'name': name,
                        'quantity': quantity,
                        'price': price,
                        'total': total
                    })
                except Exception as e:
                    self.logger.warning(f"Failed to get item details: {e}")
            self.logger.info(f"Retrieved details for {len(items_details)} items")
        except Exception as e:
            self.logger.error(f"Failed to get order items details: {e}")
        return items_details
