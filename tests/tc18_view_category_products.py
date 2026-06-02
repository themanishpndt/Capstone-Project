"""
Test Case 18: View Category Products
"""

import logging
import pytest

from src.pages.home_page import HomePage
from src.pages.category_page import CategoryPage

logger = logging.getLogger(__name__)


class TestViewCategoryProductsTC18:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_view_category_products(
        self,
        driver,
        action_delay
    ):
        """
        TC18 - View Category Products
        """

        home_page = HomePage(driver)
        category_page = CategoryPage(driver)

        logger.info(
            "Step 1: Navigate to home page"
        )
        home_page.navigate_to_home()
        action_delay(2)

        logger.info(
            "Step 2: Verify home page visible"
        )
        assert (
            "automationexercise.com"
            in driver.current_url
        )

        logger.info(
            "Step 3: Scroll to category section"
        )
        driver.execute_script(
            "window.scrollTo(0, 600);"
        )
        action_delay(2)

        logger.info(
            "Step 4: Verify categories visible"
        )
        assert (
            category_page.is_category_section_visible()
        ), "Category section not visible"

        logger.info(
            "Step 5: Click Women category"
        )
        category_page.click_women_category()
        action_delay(2)

        logger.info(
            "Step 6: Click Dress subcategory"
        )
        category_page.click_women_dress_subcategory()
        action_delay(3)

        title = (
            category_page.get_category_title()
        )

        assert (
            "WOMEN"
            in title.upper()
        ), f"Unexpected title: {title}"

        logger.info(
            f"Women category title: {title}"
        )

        logger.info(
            "Step 7: Click Men category"
        )
        category_page.click_men_category()
        action_delay(2)

        logger.info(
            "Step 8: Click Men Tshirts"
        )
        category_page.click_men_tshirts_subcategory()
        action_delay(3)

        title = (
            category_page.get_category_title()
        )

        assert (
            "MEN"
            in title.upper()
        ), f"Unexpected title: {title}"

        assert (
            category_page.get_product_count() > 0
        ), "No products displayed"

        logger.info(
            "TC18 PASSED - Category products displayed successfully"
        )