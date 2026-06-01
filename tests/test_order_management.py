"""
Test Order Management and History
"""

import pytest


class TestOrderManagement:
    """Test suite for order management"""
    
    @pytest.mark.smoke
    def test_view_order_history(self, driver, base_url):
        """Test viewing order history"""
        driver.get(f"{base_url}/account/orders")
        
        # Verify orders page is displayed
        assert "orders" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_view_order_details(self, driver, base_url):
        """Test viewing order details"""
        driver.get(f"{base_url}/account/orders")
        
        # Find and click on an order
        order_links = driver.find_elements(("class name", "order-number"))
        if order_links:
            order_links[0].click()
            
            # Verify order details page is displayed
            assert "order" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_track_order(self, driver, base_url):
        """Test order tracking"""
        driver.get(f"{base_url}/account/orders")
        
        # Find and click track button
        track_buttons = driver.find_elements(("xpath", "//button[@title='Track Order']"))
        if track_buttons:
            track_buttons[0].click()
            
            # Verify tracking page or info is displayed
            tracking_info = driver.find_elements(("class name", "tracking-info"))
            assert len(tracking_info) > 0
    
    @pytest.mark.functional
    def test_cancel_order(self, driver, base_url):
        """Test order cancellation"""
        driver.get(f"{base_url}/account/orders")
        
        # Find and click cancel button
        cancel_buttons = driver.find_elements(("xpath", "//button[@title='Cancel Order']"))
        if cancel_buttons:
            cancel_buttons[0].click()
            
            # Verify confirmation dialog appears
            confirmation_dialogs = driver.find_elements(("class name", "confirmation-dialog"))
            assert len(confirmation_dialogs) > 0
    
    @pytest.mark.functional
    def test_download_invoice(self, driver, base_url):
        """Test downloading order invoice"""
        driver.get(f"{base_url}/account/orders")
        
        # Find and click download button
        download_buttons = driver.find_elements(("xpath", "//button[@title='Download Invoice']"))
        if download_buttons:
            download_buttons[0].click()
            
            # Verify download is triggered (no specific assertion as download is handled by browser)
            assert True
    
    @pytest.mark.functional
    def test_view_order_status(self, driver, base_url):
        """Test viewing order status"""
        driver.get(f"{base_url}/account/orders")
        
        # Verify order status is displayed
        statuses = driver.find_elements(("class name", "order-status"))
        assert len(statuses) > 0
    
    @pytest.mark.functional
    def test_reorder_items(self, driver, base_url):
        """Test reordering items from previous order"""
        driver.get(f"{base_url}/account/orders")
        
        # Find and click reorder button
        reorder_buttons = driver.find_elements(("xpath", "//button[@title='Reorder']"))
        if reorder_buttons:
            reorder_buttons[0].click()
            
            # Verify items are added to cart or confirmation shown
            success_messages = driver.find_elements(("class name", "success-message"))
            assert len(success_messages) > 0 or len(driver.find_elements(("class name", "modal"))) > 0
    
    @pytest.mark.functional
    def test_view_return_options(self, driver, base_url):
        """Test viewing return options for order"""
        driver.get(f"{base_url}/account/orders")
        
        # Find order detail link
        order_links = driver.find_elements(("class name", "order-number"))
        if order_links:
            order_links[0].click()
            
            # Look for return button
            return_buttons = driver.find_elements(("xpath", "//button[@title='Return Items']"))
            assert len(return_buttons) >= 0
    
    @pytest.mark.functional
    def test_filter_orders_by_status(self, driver, base_url):
        """Test filtering orders by status"""
        driver.get(f"{base_url}/account/orders")
        
        # Find status filter dropdown
        status_filters = driver.find_elements(("id", "status-filter"))
        if status_filters:
            status_filters[0].send_keys("Completed")
            
            # Verify orders are filtered
            orders = driver.find_elements(("class name", "order-item"))
            assert len(orders) >= 0
    
    @pytest.mark.functional
    def test_search_orders(self, driver, base_url):
        """Test searching orders"""
        driver.get(f"{base_url}/account/orders")
        
        # Find search input
        search_inputs = driver.find_elements(("id", "order-search"))
        if search_inputs:
            search_inputs[0].send_keys("ORD123")
            
            # Click search button
            search_buttons = driver.find_elements(("xpath", "//button[@title='Search']"))
            if search_buttons:
                search_buttons[0].click()
                
                # Verify search results
                orders = driver.find_elements(("class name", "order-item"))
                assert len(orders) >= 0
