"""
Test Case 17: Remove Products From Cart

1. Launch browser
2. Navigate to url 'https://automationexercise.com'
3. Verify that home page is visible successfully
4. Add product to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click 'X' button corresponding to particular product
8. Verify that product is removed from the cart
"""

import logging
import pytest

from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


class TestRemoveProductFromCartTC17:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_remove_product_from_cart(
        self,
        driver,
        base_url,
        action_delay
    ):
        logger.info("TC17 - Remove Product From Cart")

        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)

        # Step 1 & 2
        home_page.navigate_to_home()
        action_delay(2)

        assert "automationexercise.com" in driver.current_url
        logger.info("Home page displayed successfully")

        # Step 3 & 4
        home_page.click_products()
        action_delay(2)

        product_page.add_first_product_to_cart(
            view_cart=False
        )
        action_delay(2)

        # Step 5
        home_page.click_cart()
        action_delay(2)

        # Step 6
        assert "/view_cart" in driver.current_url

        initial_count = cart_page.get_cart_item_count()
        assert initial_count > 0

        logger.info(
            f"Cart contains {initial_count} product(s)"
        )

        # Step 7
        cart_page.remove_item(0)
        action_delay(3)

        # Step 8
        final_count = cart_page.get_cart_item_count()

        assert final_count == initial_count - 1, (
            f"Expected {initial_count - 1} items, "
            f"but found {final_count}"
        )

        logger.info(
            "TC17 PASSED - Product removed successfully"
        )