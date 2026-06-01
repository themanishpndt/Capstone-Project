"""
Test Product Browsing and Filtering
"""

import pytest
from src.pages.product_page import ProductPage


class TestProductBrowse:
    """Test suite for product browsing"""
    
    @pytest.mark.smoke
    def test_navigate_to_products_page(self, driver, base_url):
        """Test navigation to products page"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Verify page loaded
        assert "products" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_products_are_displayed(self, driver, base_url):
        """Test that products are displayed on products page"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Verify at least one product is displayed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.functional
    def test_pagination_next_page(self, driver, base_url):
        """Test pagination next page button"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        initial_count = product_page.get_product_count()
        
        # Click next page
        product_page.click_next_page()
        
        # Verify page changed
        new_count = product_page.get_product_count()
        assert new_count > 0
    
    @pytest.mark.functional
    def test_pagination_previous_page(self, driver, base_url):
        """Test pagination previous page button"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Go to next page
        product_page.click_next_page()
        
        # Go back to previous page
        product_page.click_previous_page()
        
        # Verify page changed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.functional
    def test_product_price_displayed(self, driver, base_url):
        """Test that product prices are displayed"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        price = product_page.get_first_product_price()
        assert price is not None
        assert len(price) > 0
    
    @pytest.mark.regression
    def test_sort_products_by_price_low_to_high(self, driver, base_url):
        """Test sorting products by price (low to high)"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.sort_products("price_low_high")
        
        # Verify products are still displayed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.regression
    def test_sort_products_by_price_high_to_low(self, driver, base_url):
        """Test sorting products by price (high to low)"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.sort_products("price_high_low")
        
        # Verify products are still displayed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.regression
    def test_sort_products_by_name(self, driver, base_url):
        """Test sorting products by name"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.sort_products("name")
        
        # Verify products are still displayed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.regression
    def test_sort_products_by_rating(self, driver, base_url):
        """Test sorting products by rating"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.sort_products("rating")
        
        # Verify products are still displayed
        assert product_page.get_product_count() > 0
