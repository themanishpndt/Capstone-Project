"""
Test Case 21: Add Review on Product
Verify that user can add review on product
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.review_page import ReviewPage

logger = logging.getLogger(__name__)


class TestAddProductReview:
    """Test suite for adding product reviews"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC21: Add Review on Product")
    @allure.description("Verify that user can add a review to a product")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_review(self, driver, base_url):
        """Test adding review to product"""
        with allure.step("Login to account"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
            
            login_page = LoginPage(driver)
            login_page.login("test@example.com", "Password123!")
        
        with allure.step("Navigate to products"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
        
        with allure.step("Click on first product"):
            product_page.open_first_product_details()
        
        with allure.step("Submit product review"):
            review_page = ReviewPage(driver)
            review_page.submit_product_review(
                name="Test User",
                email="testuser@example.com",
                review_text="Great product! Highly recommended.",
                rating=5
            )
        
        with allure.step("Verify review submitted"):
            assert review_page.is_review_success_message_visible(), \
                "Review success message not displayed"
            logger.info("Product review submitted successfully")
    
    @pytest.mark.regression
    @allure.title("TC21: Review with Different Ratings")
    @allure.description("Verify review can be submitted with different star ratings")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("rating", [1, 2, 3, 4, 5])
    def test_review_with_different_ratings(self, driver, base_url, rating):
        """Test adding review with different ratings"""
        with allure.step("Navigate to product and submit review"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            home_page.click_signup_login()
            
            login_page = LoginPage(driver)
            login_page.login("test@example.com", "Password123!")
        
        with allure.step("View product"):
            product_page = ProductPage(driver)
            product_page.navigate_to(f"{base_url}/products")
            product_page.open_first_product_details()
        
        with allure.step(f"Submit review with {rating} stars"):
            review_page = ReviewPage(driver)
            review_page.submit_product_review(
                name="Test User",
                email=f"testuser{rating}@example.com",
                review_text=f"Rated {rating} stars",
                rating=rating
            )
            logger.info(f"Review submitted with {rating} star rating")
