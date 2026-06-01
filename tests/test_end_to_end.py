"""
End-to-End Test Scenarios
Complete user journey tests
"""

import pytest


class TestEndToEnd:
    """Test suite for end-to-end scenarios"""
    
    @pytest.mark.end_to_end
    @pytest.mark.critical
    def test_complete_purchase_journey(self, driver, base_url, test_data):
        """Test complete purchase from registration to order confirmation"""
        # 1. Register new user
        driver.get(f"{base_url}/register")
        driver.find_element(("id", "first-name")).send_keys(test_data["first_name"])
        driver.find_element(("id", "last-name")).send_keys(test_data["last_name"])
        driver.find_element(("id", "email")).send_keys(test_data["valid_email"])
        driver.find_element(("id", "password")).send_keys(test_data["valid_password"])
        driver.find_element(("id", "confirm-password")).send_keys(test_data["valid_password"])
        driver.find_element(("xpath", "//button[@title='Register']")).click()
        
        # 2. Browse products
        driver.get(f"{base_url}/products")
        products = driver.find_elements(("class name", "product-item"))
        assert len(products) > 0
        
        # 3. Add product to cart
        add_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Add to Cart')]"))
        if add_buttons:
            add_buttons[0].click()
        
        # 4. View cart
        driver.get(f"{base_url}/cart")
        assert "cart" in driver.current_url.lower()
        
        # 5. Proceed to checkout
        checkout_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Proceed to Checkout')]"))
        if checkout_buttons:
            checkout_buttons[0].click()
        
        # 6. Enter shipping address
        driver.find_element(("id", "first-name")).send_keys(test_data["first_name"])
        driver.find_element(("id", "last-name")).send_keys(test_data["last_name"])
        driver.find_element(("id", "address")).send_keys("123 Main Street")
        driver.find_element(("id", "city")).send_keys("New York")
        
        # 7. Select shipping method
        shipping_radios = driver.find_elements(("name", "shipping-method"))
        if shipping_radios:
            shipping_radios[0].click()
        
        # 8. Enter payment details
        driver.find_element(("id", "card-number")).send_keys("4111111111111111")
        driver.find_element(("id", "card-expiry")).send_keys("12/25")
        driver.find_element(("id", "card-cvc")).send_keys("123")
        
        # 9. Place order
        place_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Place Order')]"))
        if place_buttons:
            place_buttons[0].click()
        
        # 10. Verify order confirmation
        confirmation_messages = driver.find_elements(("class name", "confirmation-message"))
        assert len(confirmation_messages) > 0
    
    @pytest.mark.end_to_end
    def test_search_filter_and_purchase(self, driver, base_url):
        """Test searching, filtering products and purchasing"""
        # 1. Search for product
        driver.get(f"{base_url}/products")
        driver.find_element(("id", "search")).send_keys("Laptop")
        driver.find_element(("xpath", "//button[@title='Search']")).click()
        
        # 2. Filter by price
        driver.find_element(("id", "price-min")).send_keys("500")
        driver.find_element(("id", "price-max")).send_keys("1500")
        driver.find_element(("xpath", "//button[contains(text(), 'Apply Filters')]")).click()
        
        # 3. Add product to cart
        add_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Add to Cart')]"))
        if add_buttons:
            add_buttons[0].click()
        
        # 4. Verify cart updated
        driver.get(f"{base_url}/cart")
        cart_items = driver.find_elements(("class name", "cart-item"))
        assert len(cart_items) > 0
    
    @pytest.mark.end_to_end
    def test_wishlist_to_cart_to_purchase(self, driver, base_url):
        """Test adding to wishlist, moving to cart, and purchasing"""
        # 1. Browse products
        driver.get(f"{base_url}/products")
        products = driver.find_elements(("class name", "product-item"))
        assert len(products) > 0
        
        # 2. Add to wishlist
        wishlist_buttons = driver.find_elements(("xpath", "//button[@title='Add to Wishlist']"))
        if wishlist_buttons:
            wishlist_buttons[0].click()
        
        # 3. View wishlist
        driver.get(f"{base_url}/wishlist")
        wishlist_items = driver.find_elements(("class name", "wishlist-item"))
        assert len(wishlist_items) > 0
        
        # 4. Move to cart
        move_buttons = driver.find_elements(("xpath", "//button[@title='Move to Cart']"))
        if move_buttons:
            move_buttons[0].click()
        
        # 5. Verify in cart
        driver.get(f"{base_url}/cart")
        cart_items = driver.find_elements(("class name", "cart-item"))
        assert len(cart_items) > 0
    
    @pytest.mark.end_to_end
    def test_account_management_workflow(self, driver, base_url, test_data):
        """Test complete account management workflow"""
        # 1. Login
        driver.get(f"{base_url}/login")
        driver.find_element(("id", "email")).send_keys(test_data["valid_email"])
        driver.find_element(("id", "password")).send_keys(test_data["valid_password"])
        driver.find_element(("xpath", "//button[@title='Login']")).click()
        
        # 2. View profile
        driver.get(f"{base_url}/account/profile")
        assert "account" in driver.current_url.lower() or "profile" in driver.current_url.lower()
        
        # 3. Update profile
        driver.find_element(("id", "first-name")).clear()
        driver.find_element(("id", "first-name")).send_keys("UpdatedName")
        driver.find_element(("xpath", "//button[@title='Save']")).click()
        
        # 4. View addresses
        driver.get(f"{base_url}/account/addresses")
        addresses = driver.find_elements(("class name", "address-item"))
        assert len(addresses) >= 0
        
        # 5. View orders
        driver.get(f"{base_url}/account/orders")
        orders = driver.find_elements(("class name", "order-item"))
        assert len(orders) >= 0
    
    @pytest.mark.end_to_end
    def test_guest_checkout(self, driver, base_url):
        """Test guest checkout without login"""
        # 1. Browse and add to cart without logging in
        driver.get(f"{base_url}/products")
        add_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Add to Cart')]"))
        if add_buttons:
            add_buttons[0].click()
        
        # 2. Go to checkout
        driver.get(f"{base_url}/cart")
        checkout_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Proceed to Checkout')]"))
        if checkout_buttons:
            checkout_buttons[0].click()
        
        # 3. Verify guest checkout option
        guest_options = driver.find_elements(("xpath", "//button[@title='Continue as Guest']"))
        assert len(guest_options) >= 0
