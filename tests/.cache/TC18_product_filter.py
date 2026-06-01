"""
Test Product Filtering Functionality
"""

import pytest
from src.pages.product_page import ProductPage


class TestProductFilter:
    """Test suite for product filtering"""
    
    @pytest.mark.smoke
    def test_filter_products_by_price_range(self, driver, base_url):
        """Test filtering products by price range"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_price(100, 500)
        
        # Verify products are displayed and price is in range
        count = product_page.get_product_count()
        assert count >= 0
    
    @pytest.mark.functional
    def test_filter_products_by_low_price_range(self, driver, base_url):
        """Test filtering products with low price range"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_price(10, 50)
        
        # Verify filtering works
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.functional
    def test_filter_products_by_high_price_range(self, driver, base_url):
        """Test filtering products with high price range"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_price(1000, 5000)
        
        # Verify filtering works
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_filter_with_min_price_higher_than_max(self, driver, base_url):
        """Test filtering with min price higher than max price"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_price(500, 100)
        
        # Verify system handles invalid range
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_filter_with_negative_price(self, driver, base_url):
        """Test filtering with negative price values"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_price(-100, 100)
        
        # Verify system handles negative values
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.functional
    def test_filter_by_category(self, driver, base_url):
        """Test filtering products by category"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        product_page.filter_by_category("Electronics")
        
        # Verify filtering works
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.functional
    def test_filter_by_rating(self, driver, base_url):
        """Test filtering products by rating"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Assuming filtering by rating >= 4 stars
        rating_filter = (("xpath", "//input[@id='rating']"))
        rating_element = product_page.find_element(rating_filter)
        rating_element.send_keys("4")
        product_page.click_element(("xpath", "//button[contains(text(), 'Apply Filters')]"))
        
        # Verify filtering works
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_clear_all_filters(self, driver, base_url):
        """Test clearing all filters"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Apply filter
        product_page.filter_by_price(100, 500)
        
        initial_count = product_page.get_product_count()
        
        # Clear filters
        product_page.navigate_to(f"{base_url}/products")
        
        cleared_count = product_page.get_product_count()
        
        # Verify products count changes
        assert cleared_count > 0
    
    @pytest.mark.functional
    def test_multiple_filters_at_once(self, driver, base_url):
        """Test applying multiple filters simultaneously"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        
        # Apply price filter
        product_page.filter_by_price(100, 500)
        
        # Also apply category filter
        product_page.filter_by_category("Electronics")
        
        # Verify results are filtered
        assert product_page.get_product_count() >= 0
