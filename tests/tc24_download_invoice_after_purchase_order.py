"""
Test Case 24: Download Invoice after purchase order
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify ' Logged in as username' at top
12. Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Congratulations! Your order has been confirmed!'
19. Click 'Download Invoice' button and verify invoice is downloaded successfully
20. Click 'Continue' button
21. Click 'Delete Account' button
22. Verify 'ACCOUNT DELETED!' and click 'Continue' button
Workflow: Add to cart → Checkout → Register → Complete payment → Download invoice → Delete account
"""

import pytest
import logging
import os
import time
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage
from src.pages.checkout_page import CheckoutPage
from src.pages.invoice_page import InvoicePage
from tests.helpers import build_user, create_account_from_signup_page

logger = logging.getLogger(__name__)


def wait_for_invoice_download(download_dir, before_files, started_at, timeout=30):
    """Wait until Chrome finishes downloading an invoice file."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not os.path.isdir(download_dir):
            time.sleep(0.5)
            continue

        current_files = set(os.listdir(download_dir))
        completed_files = {
            file_name for file_name in current_files
            if not file_name.endswith(".crdownload")
        }
        new_files = completed_files - before_files
        invoice_files = [
            file_name for file_name in new_files
            if "invoice" in file_name.lower() or file_name.lower().endswith(".txt")
        ]
        if invoice_files:
            return os.path.join(download_dir, invoice_files[0])

        updated_invoice_files = [
            file_name for file_name in completed_files
            if (
                ("invoice" in file_name.lower() or file_name.lower().endswith(".txt"))
                and os.path.getmtime(os.path.join(download_dir, file_name)) >= started_at
            )
        ]
        if updated_invoice_files:
            return os.path.join(download_dir, updated_invoice_files[0])

        time.sleep(0.5)

    raise AssertionError("Invoice file was not downloaded")


class TestDownloadInvoiceAfterPurchaseOrderTC24:
    """Test suite for Download Invoice after purchase order - TC24"""

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_download_invoice_after_purchase_order(self, driver, base_url, action_delay):
        """Test invoice download after purchase order completion"""
        
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)
        invoice_page = InvoicePage(driver)
        user = build_user("tc24")
        download_dir = os.path.abspath(os.getenv("DOWNLOAD_DIR", "reports/downloads"))
        os.makedirs(download_dir, exist_ok=True)
        
        logger.info("Step 1: Browser launched")
        
        logger.info("Step 2 & 3: Navigating to home page and verifying")
        home_page.navigate_to_home()
        action_delay(2)
        assert driver.title
        assert "automationexercise.com" in driver.current_url
        logger.info("Home page verified")
        action_delay(1)
        
        logger.info("Step 4: Adding products to cart")
        home_page.click_products()
        action_delay(2)
        product_page.add_first_product_to_cart(view_cart=False)
        action_delay(1)
        logger.info("Product added to cart")
        
        logger.info("Step 5: Clicking Cart button")
        home_page.click_cart()
        action_delay(2)

        logger.info("Step 6: Verifying cart page is displayed")
        assert "cart" in driver.current_url.lower()
        assert cart_page.get_cart_items_count() > 0
        logger.info("Cart page verified")
        action_delay(1)
        
        logger.info("Step 7: Clicking Proceed To Checkout")
        cart_page.click_proceed_to_checkout()
        action_delay(2)
        logger.info("Proceeded to checkout")

        logger.info("Step 8: Clicking Register / Login button")
        checkout_page.click_register_login()
        action_delay(1)

        logger.info("Step 9-11: Creating account and verifying logged-in state")
        create_account_from_signup_page(login_page, action_delay, user)

        logger.info("Step 12: Clicking Cart button")
        home_page.click_cart()
        action_delay(2)

        logger.info("Step 13: Clicking Proceed To Checkout button")
        cart_page.click_proceed_to_checkout()
        action_delay(2)

        logger.info("Step 14: Verifying address details and review order")
        delivery_address = checkout_page.get_delivery_address()
        billing_address = checkout_page.get_billing_address()
        assert user["address1"] in delivery_address
        assert user["address1"] in billing_address
        assert checkout_page.get_order_items_count() > 0

        logger.info("Step 15: Entering order comment and placing order")
        checkout_page.enter_order_comment("Please deliver this order carefully.")
        checkout_page.click_place_order()
        action_delay(2)

        logger.info("Step 16: Entering payment details")
        checkout_page.enter_payment_details_name("Test User")
        checkout_page.enter_card_number("4111111111111111")
        checkout_page.enter_card_cvc("123")
        checkout_page.enter_card_expiry_date("12", "2030")
        action_delay(1)

        logger.info("Step 17: Clicking Pay and Confirm Order button")
        checkout_page.click_pay_and_confirm_order()
        action_delay(2)

        logger.info("Step 18: Verifying order confirmation message")
        confirmation_message = checkout_page.get_confirmation_message()
        assert "congratulations" in confirmation_message.lower()
        assert "confirmed" in confirmation_message.lower()

        logger.info("Step 19: Downloading invoice")
        before_files = {
            file_name for file_name in os.listdir(download_dir)
            if not file_name.endswith(".crdownload")
        }
        download_started_at = time.time()
        invoice_page.click_download_invoice()
        downloaded_invoice = wait_for_invoice_download(
            download_dir,
            before_files,
            download_started_at,
        )
        assert os.path.exists(downloaded_invoice)
        logger.info(f"Invoice downloaded successfully: {downloaded_invoice}")

        logger.info("Step 20: Clicking Continue button")
        invoice_page.click_continue_button()
        action_delay(2)

        logger.info("Step 21: Clicking Delete Account button")
        login_page.click_delete_account()
        action_delay(1)

        logger.info("Step 22: Verifying account deleted")
        assert login_page.is_account_deleted_visible()
        login_page.click_continue()
        action_delay(1)
        logger.info("Download invoice after purchase order test completed successfully")
