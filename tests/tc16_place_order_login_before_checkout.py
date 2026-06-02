"""
Test Case 16: Place Order: Login before Checkout
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Signup / Login' button
5. Fill email, password and click 'Login' button
6. Verify 'Logged in as username' at top
7. Add products to cart
8. Click 'Cart' button
9. Verify that cart page is displayed
10. Click Proceed To Checkout
11. Verify Address Details and Review Your Order
12. Enter description in comment text area and click 'Place Order'
13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
14. Click 'Pay and Confirm Order' button
15. Verify success message 'Congratulations! Your order has been confirmed!'
Workflow: Register Account → Logout → Login → Add Products → Cart → Checkout → Payment → Order Confirmation
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

class TestPlaceOrderLoginBeforeCheckoutTC16:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_place_order_login_before_checkout(self, driver, base_url, action_delay):

        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        cart_page = CartPage(driver)
        login_page = LoginPage(driver)

        unique_email = f"testuser_{int(time.time())}@example.com"
        password = "TestPass123!"

        logger.info("Step 1")
        home_page.navigate_to_home()
        action_delay(2)

        logger.info("Step 2")
        assert "automationexercise.com" in driver.current_url
        action_delay(1)

        logger.info("Step 3")
        home_page.click_signup_login()
        action_delay(2)

        logger.info("Register Account")

        login_page.enter_signup_name("Test User")
        login_page.enter_signup_email(unique_email)
        login_page.click_signup_button()

        action_delay(2)

        login_page.select_title_mr()
        login_page.enter_reg_password(password)
        login_page.select_date_of_birth("15", "05", "1990")

        action_delay(1)
        driver.execute_script("window.scrollBy(0, 300)")
        action_delay(1)

        login_page.enter_first_name("Test")
        login_page.enter_last_name("User")

        login_page.enter_company("Test Company")
        login_page.enter_address("123 Test Street")
        login_page.select_country("United States")
        login_page.enter_state("Texas")
        login_page.enter_city("Houston")
        login_page.enter_zipcode("77001")
        login_page.enter_mobile_number("1234567890")

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

        login_page.click_create_account()

        action_delay(3)

        assert login_page.is_account_created_visible()

        login_page.click_continue()

        action_delay(3)

        logger.info("Logout")

        driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Logout')]"
        ).click()

        action_delay(3)

        logger.info("Login")

        login_page.enter_login_email(unique_email)
        login_page.enter_login_password(password)
        login_page.click_login_button()

        action_delay(3)

        page_text = driver.execute_script(
            "return document.body.innerText;"
        )

        assert "Logged in as" in page_text

        logger.info("Add Products")

        home_page.click_products()

        action_delay(2)

        product_page.add_first_product_to_cart(
            view_cart=False
        )

        action_delay(2)

        home_page.click_cart()

        action_delay(2)

        assert "/view_cart" in driver.current_url

        assert cart_page.get_cart_item_count() > 0

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

        comment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.NAME, "message")
            )
        )

        comment_box.send_keys(
            "Please deliver carefully"
        )

        place_order_btn = driver.find_element(
            By.XPATH,
            "//a[contains(text(),'Place Order')]"
        )

        place_order_btn.click()

        action_delay(2)

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
        ).send_keys("2028")

        pay_btn = driver.find_element(
            By.ID,
            "submit"
        )

        pay_btn.click()

        action_delay(4)

        page_text = driver.execute_script(
            "return document.body.innerText;"
        )

        assert (
            "Congratulations" in page_text
            or "Your order has been placed successfully!" in page_text
            or "Order Confirmed" in page_text
        )