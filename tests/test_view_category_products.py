"""
Test Case 18: View Category Products
Verify that user can view products in specific category
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.category_page import CategoryPage

logger = logging.getLogger(__name__)


class TestViewCategoryProducts:
    """Test suite for viewing category products"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC18: View Category Products - Women")
    @allure.description("Verify that user can view products in Women category")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_women_category_products(self, driver, base_url):
        """Test viewing Women category products"""
        with allure.step("Navigate to products"):
            category_page = CategoryPage(driver)
            category_page.navigate_to_products()
        
        with allure.step("Click Women category"):
            category_page.click_women_category()
        
        with allure.step("Verify women products displayed"):
            product_count = category_page.get_product_count()
            assert product_count > 0, "No products found in Women category"
            logger.info(f"Found {product_count} products in Women category")
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC18: View Category Products - Men")
    @allure.description("Verify that user can view products in Men category")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_men_category_products(self, driver, base_url):
        """Test viewing Men category products"""
        with allure.step("Navigate to products"):
            category_page = CategoryPage(driver)
            category_page.navigate_to_products()
        
        with allure.step("Click Men category"):
            category_page.click_men_category()
        
        with allure.step("Verify men products displayed"):
            product_count = category_page.get_product_count()
            assert product_count > 0, "No products found in Men category"
            logger.info(f"Found {product_count} products in Men category")
    
    @pytest.mark.regression
    @allure.title("TC18: View Category Products - Kids")
    @allure.description("Verify that user can view products in Kids category")
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_kids_category_products(self, driver, base_url):
        """Test viewing Kids category products"""
        with allure.step("Navigate to products"):
            category_page = CategoryPage(driver)
            category_page.navigate_to_products()
        
        with allure.step("Click Kids category"):
            category_page.click_kids_category()
        
        with allure.step("Verify kids products displayed"):
            product_count = category_page.get_product_count()
            assert product_count > 0, "No products found in Kids category"
            logger.info(f"Found {product_count} products in Kids category")
    
    @pytest.mark.regression
    @pytest.mark.parametrize("category_name,category_method", [
        ("Women - Dress", "click_women_dress_subcategory"),
        ("Women - Tops", "click_women_tops_subcategory"),
        ("Men - Shirts", "click_men_shirts_subcategory"),
    ])
    @allure.title("TC18: View Subcategory Products")
    @allure.description("Verify that user can view products in subcategories")
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_subcategory_products(self, driver, base_url, category_name, category_method):
        """Test viewing subcategory products"""
        with allure.step(f"Navigate to {category_name} subcategory"):
            category_page = CategoryPage(driver)
            category_page.navigate_to_products()
            
            # Click the subcategory method
            getattr(category_page, category_method)()
        
        with allure.step("Verify products displayed"):
            product_count = category_page.get_product_count()
            assert product_count > 0, f"No products found in {category_name}"
            logger.info(f"Found {product_count} products in {category_name}")
