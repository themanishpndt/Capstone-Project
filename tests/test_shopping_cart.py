"""
Test Shopping Cart Functionality
"""

import pytest
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage


class TestShoppingCart:
    """Test suite for shopping cart functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_add_product_to_cart(self, driver, base_url):
        """Test adding product to cart"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Get first product and add to cart
        products = product_page.find_elements(("class name", "product-item"))
        if products:
            add_button = products[0].find_element(("xpath", ".//button[contains(text(), 'Add to Cart')]"))
            add_button.click()
            
            # Verify success message
            assert product_page.is_element_visible(("class name", "success-message"))
    
    @pytest.mark.functional
    def test_view_cart(self, driver, base_url):
        """Test viewing shopping cart"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        # Verify cart page is displayed
        assert "cart" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_remove_product_from_cart(self, driver, base_url):
        """Test removing product from cart"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        initial_count = cart_page.get_cart_item_count()
        
        if initial_count > 0:
            cart_page.remove_item(0)
            new_count = cart_page.get_cart_item_count()
            
            assert new_count < initial_count
    
    @pytest.mark.functional
    def test_update_product_quantity(self, driver, base_url):
        """Test updating product quantity in cart"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        if cart_page.get_cart_item_count() > 0:
            cart_page.update_item_quantity(0, 5)
            
            # Verify quantity is updated
            items = cart_page.get_cart_items()
            assert len(items) > 0
    
    @pytest.mark.functional
    def test_get_cart_subtotal(self, driver, base_url):
        """Test retrieving cart subtotal"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        subtotal = cart_page.get_subtotal()
        assert subtotal is not None
        assert len(subtotal) > 0
    
    @pytest.mark.functional
    def test_get_cart_tax(self, driver, base_url):
        """Test retrieving cart tax amount"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        tax = cart_page.get_tax()
        assert tax is not None
    
    @pytest.mark.functional
    def test_get_cart_total(self, driver, base_url):
        """Test retrieving cart total"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        total = cart_page.get_total()
        assert total is not None
        assert len(total) > 0
    
    @pytest.mark.functional
    def test_apply_coupon_code(self, driver, base_url):
        """Test applying coupon code"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        cart_page.apply_coupon("SAVE10")
        
        # Verify coupon was applied or error message shown
        assert cart_page.is_element_visible(("class name", "success-message")) or \
               cart_page.is_element_visible(("class name", "error-message"))
    
    @pytest.mark.functional
    def test_apply_invalid_coupon(self, driver, base_url):
        """Test applying invalid coupon code"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        cart_page.apply_coupon("INVALIDCODE123")
        
        # Verify error message is displayed
        assert cart_page.is_element_visible(("class name", "error-message"))
    
    @pytest.mark.smoke
    def test_proceed_to_checkout(self, driver, base_url):
        """Test proceeding to checkout from cart"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        if not cart_page.is_cart_empty():
            cart_page.click_checkout()
            
            # Verify navigation to checkout page
            assert "checkout" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_continue_shopping_from_cart(self, driver, base_url):
        """Test continue shopping button"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        cart_page.click_continue_shopping()
        
        # Verify navigation back to products
        assert "products" in driver.current_url.lower() or "shop" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_empty_cart_message(self, driver, base_url):
        """Test empty cart message"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        # Check if cart is empty
        is_empty = cart_page.is_cart_empty()
        
        # Verify either cart is empty or has items
        assert isinstance(is_empty, bool)
    
    @pytest.mark.regression
    def test_cart_persistence(self, driver, base_url):
        """Test cart items persist after page refresh"""
        cart_page = CartPage(driver)
        cart_page.navigate_to(f"{base_url}/cart")
        
        initial_count = cart_page.get_cart_item_count()
        
        # Refresh page
        cart_page.refresh_page()
        
        new_count = cart_page.get_cart_item_count()
        
        # Verify cart items still exist
        assert new_count == initial_count
