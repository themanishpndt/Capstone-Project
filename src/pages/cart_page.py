"""
Cart Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.cart_locators import CartLocators


class CartPage(BasePage):
    """Shopping cart page object"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartLocators()
    
    def navigate_to_cart(self):
        """Navigate to shopping cart page"""
        self.navigate_to(self.locators.CART_URL)
        self.logger.info("Navigated to cart page")
    
    def get_cart_item_count(self):
        """Get number of items in cart"""
        items = self.find_elements(self.locators.CART_ITEMS)
        count = len(items)
        self.logger.info(f"Cart item count: {count}")
        return count
    
    def get_cart_items_count(self):
        """Get number of items in cart (alias for get_cart_item_count)"""
        return self.get_cart_item_count()
    
    def get_product_quantity(self):
        """Get product quantity from cart"""
        try:
            quantity_element = self.find_element(self.locators.ITEM_QUANTITY)
            quantity_text = quantity_element.text
            quantity = int(''.join(c for c in quantity_text if c.isdigit()))
            self.logger.info(f"Product quantity: {quantity}")
            return quantity
        except Exception as e:
            self.logger.error(f"Failed to get product quantity: {e}")
            return 0
    
    def increase_product_quantity(self, target_quantity):
        """Increase product quantity to target amount"""
        current = self.get_product_quantity()
        if current < target_quantity:
            for _ in range(target_quantity - current):
                try:
                    button = self.find_element(self.locators.INCREASE_QUANTITY_BUTTON)
                    button.click()
                except Exception as e:
                    self.logger.warning(f"Could not increase quantity: {e}")
        self.logger.info(f"Product quantity set to: {target_quantity}")
    
    def get_cart_items(self):
        """Get list of cart items"""
        items = self.find_elements(self.locators.CART_ITEMS)
        cart_items = []
        for item in items:
            try:
                name = item.find_element(*self.locators.ITEM_NAME).text
                price = item.find_element(*self.locators.ITEM_PRICE).text
                quantity = item.find_element(*self.locators.ITEM_QUANTITY).text
                cart_items.append({
                    'name': name,
                    'price': price,
                    'quantity': quantity
                })
            except Exception as e:
                self.logger.warning(f"Failed to get cart item details: {e}")
        self.logger.info(f"Retrieved {len(cart_items)} items from cart")
        return cart_items
    
    def update_item_quantity(self, item_index, quantity):
        """Update quantity of specific item"""
        try:
            items = self.find_elements(self.locators.CART_ITEMS)
            if item_index < len(items):
                quantity_input = items[item_index].find_element(*self.locators.QUANTITY_INPUT)
                quantity_input.clear()
                quantity_input.send_keys(str(quantity))
                self.logger.info(f"Updated item {item_index} quantity to {quantity}")
        except Exception as e:
            self.logger.error(f"Failed to update item quantity: {e}")
    
    def remove_item(self, item_index):
        """Remove item from cart"""
        try:
            items = self.find_elements(self.locators.CART_ITEMS)
            if item_index < len(items):
                remove_button = items[item_index].find_element(*self.locators.REMOVE_ITEM_BUTTON)
                remove_button.click()
                self.logger.info(f"Removed item {item_index} from cart")
        except Exception as e:
            self.logger.error(f"Failed to remove item: {e}")
    
    def remove_product(self, index):
        """Remove product from cart (alias for remove_item)"""
        self.remove_item(index)
    
    def click_remove_product_button(self, index):
        """Click remove button for product (alias for remove_item)"""
        self.remove_item(index)
    
    def get_subtotal(self):
        """Get cart subtotal"""
        try:
            subtotal = self.get_text(self.locators.SUBTOTAL)
            self.logger.info(f"Subtotal: {subtotal}")
            return subtotal
        except Exception as e:
            self.logger.error(f"Failed to get subtotal: {e}")
            return None
    
    def get_tax(self):
        """Get cart tax amount"""
        try:
            tax = self.get_text(self.locators.TAX)
            self.logger.info(f"Tax: {tax}")
            return tax
        except Exception as e:
            self.logger.error(f"Failed to get tax: {e}")
            return None
    
    def get_total(self):
        """Get cart total"""
        try:
            total = self.get_text(self.locators.TOTAL)
            self.logger.info(f"Total: {total}")
            return total
        except Exception as e:
            self.logger.error(f"Failed to get total: {e}")
            return None
    
    def apply_coupon(self, coupon_code):
        """Apply coupon code to cart"""
        try:
            self.enter_text(self.locators.COUPON_INPUT, coupon_code)
            self.click_element(self.locators.APPLY_COUPON_BUTTON)
            self.logger.info(f"Applied coupon: {coupon_code}")
        except Exception as e:
            self.logger.error(f"Failed to apply coupon: {e}")
    
    def click_proceed_to_checkout(self):
        """Click proceed to checkout button"""
        self.click_element(self.locators.CHECKOUT_BUTTON)
        self.logger.info("Clicked proceed to checkout")
    
    def click_checkout(self):
        """Click checkout button (alias)"""
        self.click_proceed_to_checkout()
    
    def click_continue_shopping(self):
        """Click continue shopping button"""
        try:
            self.click_element(self.locators.CONTINUE_SHOPPING_BUTTON)
            self.logger.info("Clicked continue shopping")
        except Exception as e:
            self.logger.warning(f"Could not click continue shopping: {e}")
    
    def is_cart_empty(self):
        """Check if cart is empty"""
        is_empty = self.is_element_visible(self.locators.EMPTY_CART_MESSAGE)
        self.logger.info(f"Cart empty status: {is_empty}")
        return is_empty

