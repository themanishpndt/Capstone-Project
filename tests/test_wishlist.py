"""
Test Wishlist and Favorites Functionality
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWishlist:
    """Test suite for wishlist functionality"""

    @pytest.mark.smoke
    def test_add_product_to_wishlist(self, driver, base_url):
        """Test adding product to wishlist"""

        driver.get(f"{base_url}/products")

        add_wishlist_buttons = driver.find_elements(
            By.XPATH,
            "//button[@title='Add to Wishlist']"
        )

        if add_wishlist_buttons:
            add_wishlist_buttons[0].click()

            success_messages = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "success-message")
                )
            )

            assert len(success_messages) > 0, \
                "Wishlist success message not displayed"

    @pytest.mark.functional
    def test_view_wishlist(self, driver, base_url):
        """Test viewing wishlist"""

        driver.get(f"{base_url}/wishlist")

        assert "wishlist" in driver.current_url.lower(), \
            "Wishlist page not displayed"

    @pytest.mark.functional
    def test_remove_product_from_wishlist(self, driver, base_url):
        """Test removing product from wishlist"""

        driver.get(f"{base_url}/wishlist")

        remove_buttons = driver.find_elements(
            By.XPATH,
            "//button[@title='Remove from Wishlist']"
        )

        if remove_buttons:

            initial_count = len(
                driver.find_elements(
                    By.CLASS_NAME,
                    "wishlist-item"
                )
            )

            remove_buttons[0].click()

            WebDriverWait(driver, 10).until(
                lambda d: len(
                    d.find_elements(By.CLASS_NAME, "wishlist-item")
                ) < initial_count
            )

            new_count = len(
                driver.find_elements(
                    By.CLASS_NAME,
                    "wishlist-item"
                )
            )

            assert new_count < initial_count, \
                "Product was not removed from wishlist"

    @pytest.mark.functional
    def test_move_wishlist_item_to_cart(self, driver, base_url):
        """Test moving item from wishlist to cart"""

        driver.get(f"{base_url}/wishlist")

        move_buttons = driver.find_elements(
            By.XPATH,
            "//button[@title='Move to Cart']"
        )

        if move_buttons:
            move_buttons[0].click()

            success_messages = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "success-message")
                )
            )

            assert len(success_messages) > 0, \
                "Move to cart success message not displayed"

    @pytest.mark.functional
    def test_wishlist_empty_state(self, driver, base_url):
        """Test empty wishlist message"""

        driver.get(f"{base_url}/wishlist")

        empty_messages = driver.find_elements(
            By.CLASS_NAME,
            "empty-wishlist-message"
        )

        wishlist_items = driver.find_elements(
            By.CLASS_NAME,
            "wishlist-item"
        )

        assert (
            len(empty_messages) > 0 or
            len(wishlist_items) > 0
        ), "Wishlist page is displaying invalid state"

    @pytest.mark.regression
    def test_wishlist_persistence(self, driver, base_url):
        """Test wishlist items persist after page refresh"""

        driver.get(f"{base_url}/wishlist")

        initial_count = len(
            driver.find_elements(
                By.CLASS_NAME,
                "wishlist-item"
            )
        )

        driver.refresh()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        new_count = len(
            driver.find_elements(
                By.CLASS_NAME,
                "wishlist-item"
            )
        )

        assert new_count == initial_count, \
            "Wishlist items did not persist after refresh"

    @pytest.mark.functional
    def test_share_wishlist(self, driver, base_url):
        """Test sharing wishlist"""

        driver.get(f"{base_url}/wishlist")

        share_buttons = driver.find_elements(
            By.XPATH,
            "//button[@title='Share Wishlist']"
        )

        if share_buttons:
            share_buttons[0].click()

            share_dialogs = driver.find_elements(
                By.CLASS_NAME,
                "share-dialog"
            )

            modals = driver.find_elements(
                By.CLASS_NAME,
                "modal"
            )

            assert (
                len(share_dialogs) > 0 or
                len(modals) > 0
            ), "Share dialog was not displayed"