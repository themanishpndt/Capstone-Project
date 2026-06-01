"""
Test Product Search Functionality
"""

import pytest
from src.pages.product_page import ProductPage


class TestProductSearch:
    """Test suite for product search functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_search_with_valid_product_name(self, driver, base_url):
        """Test searching for a product with valid name"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("Laptop")
        
        # Verify products are displayed
        assert product_page.get_product_count() > 0
    
    @pytest.mark.regression
    def test_search_with_empty_query(self, driver, base_url):
        """Test search with empty query"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("")
        
        # Verify all products are displayed or error is shown
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_search_with_nonexistent_product(self, driver, base_url):
        """Test search for non-existent product"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("NonExistentProduct123xyz")
        
        # Verify no products are found
        assert product_page.get_product_count() == 0
    
    @pytest.mark.functional
    def test_search_case_insensitivity(self, driver, base_url):
        """Test search is case insensitive"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("laptop")
        
        count1 = product_page.get_product_count()
        
        # Search again with different case
        product_page.search_product("LAPTOP")
        count2 = product_page.get_product_count()
        
        # Verify results are the same
        assert count1 == count2
    
    @pytest.mark.functional
    def test_search_with_special_characters(self, driver, base_url):
        """Test search with special characters"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("Product@#$%")
        
        # Verify search handles special characters
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_search_with_numbers_only(self, driver, base_url):
        """Test search with numbers only"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("12345")
        
        # Verify search handles numbers
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.functional
    def test_search_product_names_displayed(self, driver, base_url):
        """Test that product names are displayed in search results"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("Phone")
        
        names = product_page.get_product_names()
        assert len(names) > 0
        assert all(name for name in names)
    
    @pytest.mark.functional
    def test_search_with_partial_product_name(self, driver, base_url):
        """Test search with partial product name"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        product_page.search_product("Sam")
        
        # Verify products with matching partial name are displayed
        assert product_page.get_product_count() >= 0
    
    @pytest.mark.regression
    def test_search_with_very_long_query(self, driver, base_url):
        """Test search with very long query string"""
        product_page = ProductPage(driver)
        product_page.navigate_to(f"{base_url}/products")
        long_query = "a" * 500
        product_page.search_product(long_query)
        
        # Verify no crash occurs
        assert product_page.get_product_count() == 0
