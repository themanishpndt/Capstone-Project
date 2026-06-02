"""
Test Case 14: Place Order - Register while Checkout
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
19. Click 'Delete Account' button
20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
Workflow: Add products → Cart → Checkout → Register → Address → Payment → Order confirmation → Delete account
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


class TestPlaceOrderRegisterCheckoutTC14:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_place_order_register_during_checkout(
        self,
        driver,
        base_url,
        action_delay
    ):

        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        signup_email = f"testuser_{int(time.time())}@example.com"
        password = "TestPass123!"

        logger.info("Navigate to home page")

        home_page.navigate_to_home()
        action_delay(2)

        assert "automationexercise.com" in driver.current_url
        assert "Automation Exercise" in driver.title

        logger.info("Add product to cart")

        home_page.click_products()
        action_delay(2)

        product_page.add_first_product_to_cart(view_cart=False)
        action_delay(2)

        home_page.click_cart()
        action_delay(2)

        assert "/view_cart" in driver.current_url

        cart_count = cart_page.get_cart_item_count()
        assert cart_count > 0

        logger.info("Proceed to checkout")

        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(text(),'Proceed To Checkout')]"
                )
            )
        )
        checkout_btn.click()

        action_delay(2)

        logger.info("Register during checkout")

        register_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//u[contains(text(),'Register / Login')]"
                )
            )
        )
        register_btn.click()

        action_delay(2)

        login_page.enter_signup_name("Test User")
        login_page.enter_signup_email(signup_email)
        login_page.click_signup_button()

        action_delay(2)

        assert login_page.is_account_info_visible()

        login_page.select_title_mr()
        login_page.enter_reg_name("Test User")
        login_page.enter_reg_password(password)

        login_page.select_date_of_birth(
            "15",
            "05",
            "1990"
        )

        login_page.check_newsletter()
        login_page.check_special_offers()

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight * 0.5)"
        )

        action_delay(1)

        login_page.enter_first_name("Test")
        login_page.enter_last_name("User")
        login_page.enter_company("Test Company")
        login_page.enter_address("123 Test Street")
        login_page.enter_address2("Apartment 101")
        login_page.select_country("United States")
        login_page.enter_state("Texas")
        login_page.enter_city("Houston")
        login_page.enter_zipcode("77001")
        login_page.enter_mobile_number("1234567890")

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

        action_delay(1)

        login_page.click_create_account()

        action_delay(3)

        assert login_page.is_account_created_visible()

        login_page.click_continue()

        action_delay(3)

        assert login_page.is_logged_in_visible()

        logger.info("Open cart again")

        home_page.click_cart()

        action_delay(2)

        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(text(),'Proceed To Checkout')]"
                )
            )
        )
        checkout_btn.click()

        action_delay(2)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "Address Details" in page_text
        assert "Review Your Order" in page_text

        logger.info("Place order")

        comment_box = driver.find_element(
            By.NAME,
            "message"
        )

        comment_box.send_keys(
            "Please deliver carefully"
        )

        driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Place Order')]"
        ).click()

        action_delay(2)

        logger.info("Enter payment details")

        driver.find_element(
            By.NAME,
            "name_on_card"
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

        driver.find_element(
            By.ID,
            "submit"
        ).click()

        action_delay(3)

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Congratulations') or contains(text(),'Your order has been placed successfully')]"
                )
            )
        )

        assert success_message.is_displayed()

        logger.info("Delete account")

        login_page.click_delete_account()

        action_delay(2)

        assert login_page.is_account_deleted_visible()

        login_page.click_continue()

        action_delay(2)

        logger.info("TC14 completed successfully")

