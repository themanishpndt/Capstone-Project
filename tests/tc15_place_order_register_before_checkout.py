"""
Test Case 15: Place Order - Register before Checkout
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill all details in Signup and create account
6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
7. Verify ' Logged in as username' at top
8. Add products to cart
9. Click 'Cart' button
10. Verify that cart page is displayed
11. Click Proceed To Checkout
12. Verify Address Details and Review Your Order
13. Enter description in comment text area and click 'Place Order'
14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
15. Click 'Pay and Confirm Order' button
16. Verify success message 'Congratulations! Your order has been confirmed!'
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' and click 'Continue' button
Workflow: Register → Add products → Cart → Checkout → Payment → Order confirmation → Delete account
"""

import pytest
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage
from src.pages.login_page import LoginPage

logger = logging.getLogger(__name__)


class TestPlaceOrderRegisterBeforeCheckoutTC15:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_place_order_register_before_checkout(
        self,
        driver,
        base_url,
        action_delay
    ):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        unique_email = f"testuser_{int(time.time())}@example.com"

        logger.info("Step 1")
        home_page.navigate_to_home()
        action_delay(2)

        logger.info("Step 2")
        assert "automationexercise.com" in driver.current_url
        action_delay(1)

        logger.info("Step 3")
        home_page.click_signup_login()
        action_delay(2)

        logger.info("Step 4")
        login_page.enter_signup_name("Test User")
        login_page.enter_signup_email(unique_email)
        login_page.click_signup_button()
        action_delay(2)

        logger.info("Step 5")
        assert login_page.is_account_info_visible()

        login_page.select_title_mr()
        login_page.enter_reg_password("TestPass123!")
        login_page.select_date_of_birth("15", "05", "1990")

        login_page.check_newsletter()
        login_page.check_special_offers()

        login_page.enter_first_name("Test")
        login_page.enter_last_name("User")
        login_page.enter_company("Test Company")
        login_page.enter_address("123 Test Street")
        login_page.enter_address2("Apt 101")
        login_page.select_country("United States")
        login_page.enter_state("Texas")
        login_page.enter_city("Houston")
        login_page.enter_zipcode("77001")
        login_page.enter_mobile_number("1234567890")

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        action_delay(1)

        login_page.click_create_account()
        action_delay(3)

        logger.info("Step 6")
        assert login_page.is_account_created_visible()
        login_page.click_continue()
        action_delay(3)

        logger.info("Step 7")
        assert login_page.is_logged_in_visible()
        action_delay(1)

        logger.info("Step 8")
        home_page.click_products()
        action_delay(2)

        product_page.add_first_product_to_cart(
            view_cart=False
        )
        action_delay(2)

        logger.info("Step 9")
        home_page.click_cart()
        action_delay(2)

        logger.info("Step 10")
        assert "/view_cart" in driver.current_url
        assert cart_page.get_cart_item_count() > 0
        action_delay(1)

        logger.info("Step 11")

        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(text(),'Proceed To Checkout')]"
                )
            )
        )
        checkout_btn.click()
        action_delay(3)

        logger.info("Step 12")

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert (
            "Address Details" in page_text
            or "Review Your Order" in page_text
            or "Delivery Address" in page_text
        )

        action_delay(1)

        logger.info("Step 13")

        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.NAME,
                    "message"
                )
            )
        )

        comment_box.send_keys(
            "Please deliver carefully."
        )

        place_order_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(text(),'Place Order')]"
                )
            )
        )

        place_order_btn.click()
        action_delay(3)

        logger.info("Step 14")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.NAME,
                    "name_on_card"
                )
            )
        ).send_keys("Test User")

        driver.find_element(
            By.NAME,
            "card_number"
        ).send_keys("4111111111111111")

        driver.find_element(
            By.NAME,
            "cvc"
        ).send_keys("123")

        driver.find_element(
            By.NAME,
            "expiry_month"
        ).send_keys("12")

        driver.find_element(
            By.NAME,
            "expiry_year"
        ).send_keys("2030")

        action_delay(1)

        logger.info("Step 15")

        pay_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "submit"
                )
            )
        )

        pay_btn.click()
        action_delay(4)

        logger.info("Step 16")

        confirmation_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert (
            "Congratulations" in confirmation_text
            or "confirmed" in confirmation_text.lower()
        )

        logger.info("Step 17")

        login_page.click_delete_account()
        action_delay(3)

        logger.info("Step 18")

        assert login_page.is_account_deleted_visible()

        login_page.click_continue()
        action_delay(2)

        logger.info("TC15 completed successfully")