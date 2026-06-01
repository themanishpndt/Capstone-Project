"""
Test Case 19: View Brand Products
Verify that user can view products by specific brand
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.brand_page import BrandPage

logger = logging.getLogger(__name__)


class TestViewBrandProducts:
    """Test suite for viewing brand products"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC19: View Brand Products - Polo")
    @allure.description("Verify that user can view Polo brand products")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_polo_brand_products(self, driver, base_url):
        """Test viewing Polo brand products"""
        with allure.step("Navigate to products"):
            brand_page = BrandPage(driver)
            brand_page.navigate_to_products()
        
        with allure.step("Click Polo brand"):
            brand_page.click_polo_brand()
        
        with allure.step("Verify Polo products displayed"):
            product_count = brand_page.get_product_count()
            assert product_count > 0, "No products found for Polo brand"
            logger.info(f"Found {product_count} Polo brand products")
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC19: View Brand Products - H&M")
    @allure.description("Verify that user can view H&M brand products")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_h_m_brand_products(self, driver, base_url):
        """Test viewing H&M brand products"""
        with allure.step("Navigate to products"):
            brand_page = BrandPage(driver)
            brand_page.navigate_to_products()
        
        with allure.step("Click H&M brand"):
            brand_page.click_h_m_brand()
        
        with allure.step("Verify H&M products displayed"):
            product_count = brand_page.get_product_count()
            assert product_count > 0, "No products found for H&M brand"
            logger.info(f"Found {product_count} H&M brand products")
    
    @pytest.mark.regression
    @pytest.mark.parametrize("brand_name,brand_method", [
        ("Madame", "click_madame_brand"),
        ("Mango", "click_mango_brand"),
        ("Allen Solly", "click_allen_solly_brand"),
        ("Babyhug", "click_babyhug_brand"),
    ])
    @allure.title("TC19: View Products by Various Brands")
    @allure.description("Verify that user can view products for different brands")
    @allure.severity(allure.severity_level.NORMAL)
    def test_view_various_brand_products(self, driver, base_url, brand_name, brand_method):
        """Test viewing various brand products"""
        with allure.step(f"Navigate to {brand_name} brand products"):
            brand_page = BrandPage(driver)
            brand_page.navigate_to_products()
            
            # Click the brand method
            getattr(brand_page, brand_method)()
        
        with allure.step("Verify brand products displayed"):
            product_count = brand_page.get_product_count()
            assert product_count > 0, f"No products found for {brand_name} brand"
            logger.info(f"Found {product_count} {brand_name} brand products")
