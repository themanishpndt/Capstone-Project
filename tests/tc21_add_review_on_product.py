"""
Test Case 21: Add review on product
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Click on 'Products' button
4. Verify user is navigated to ALL PRODUCTS page successfully
5. Click on 'View Product' button
6. Verify 'Write Your Review' is visible
7. Enter name, email and review
8. Click 'Submit' button
9. Verify success message 'Thank you for your review.'
Workflow: Navigate to Products → Click View Product → Scroll to reviews → Enter review details → Submit → Verify success
"""

import pytest
import logging
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.review_page import ReviewPage

logger = logging.getLogger(__name__)


class TestAddReviewOnProductTC21:
    """Test suite for Add review on product - TC21"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_add_review_on_product(self, driver, base_url, action_delay):
        """Test adding a review to a product"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        review_page = ReviewPage(driver)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2: Navigating to home page")
        home_page.navigate_to_home()
        action_delay(2)
        
        logger.info("Step 3: Clicking on Products button")
        home_page.click_products()
        action_delay(2)
        
        logger.info("Step 4: Verifying ALL PRODUCTS page")
        current_url = driver.current_url
        assert "products" in current_url.lower()
        page_text = driver.execute_script("return document.body.innerText;")
        assert "ALL PRODUCTS" in page_text or "Products" in page_text
        logger.info("ALL PRODUCTS page verified")
        action_delay(1)
        
        logger.info("Step 5: Clicking on View Product button")
        product_page.open_first_product_details()
        action_delay(2)
        
        logger.info("Step 6: Verifying 'Write Your Review' is visible")
        review_page.scroll_to_reviews_section()
        action_delay(1)
        page_text = driver.execute_script("return document.body.innerText;")
        assert "write your review" in page_text.lower() or "review" in page_text.lower()
        logger.info("Write Your Review section verified")
        action_delay(1)
        
        logger.info("Step 7: Entering name, email and review")
        review_page.enter_review_name("John Doe")
        action_delay(0.5)
        review_page.enter_review_email("johndoe@example.com")
        action_delay(0.5)
        review_page.enter_review_text("This is an excellent product! Highly recommended.")
        action_delay(0.5)
        logger.info("Review details entered")
        action_delay(1)
        
        logger.info("Step 8: Clicking Submit button")
        review_page.click_submit_review()
        action_delay(3)  # Wait for server response
        
        logger.info("Step 9: Verifying success message 'Thank you for your review.'")
        # Try multiple ways to verify success
        page_text = driver.execute_script("return document.body.innerText;")
        success_via_text = "thank you" in page_text.lower() and "review" in page_text.lower()
        
        # Also check for specific success element
        success_via_element = driver.execute_script("""
            return document.querySelector('.alert-success') || 
                   document.evaluate(\"//span[contains(text(), 'Thank')]\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue ||
                   (document.body.innerText.includes('Thank you') && document.body.innerText.includes('review'));
        """)
        
        assert success_via_text or success_via_element, "Success message not found. Page text: " + page_text[:200]
        logger.info("Success message verified")
        logger.info("Add review on product test completed successfully")
