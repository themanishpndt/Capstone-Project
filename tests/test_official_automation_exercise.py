"""
Official AutomationExercise capstone suite.

This file maps one-to-one to the 26 public test cases from automationexercise.com.
"""

import logging
from pathlib import Path
from uuid import uuid4

import allure
import pytest

from src.pages.automation_exercise_page import AutomationExercisePage


pytestmark = [pytest.mark.official, pytest.mark.ui]
logger = logging.getLogger(__name__)

DOWNLOAD_DIR = Path("reports/downloads").resolve()
UPLOAD_FILE = Path(__file__).resolve().parents[1] / "test_data" / "contact_upload.txt"


@pytest.fixture
def app(driver, base_url):
    return AutomationExercisePage(driver, base_url)


def make_user(label):
    suffix = uuid4().hex[:8]
    safe_label = label.replace(" ", "").lower()
    return {
        "title": "Mr",
        "name": f"{label} {suffix}",
        "email": f"{safe_label}_{suffix}@example.com",
        "password": "Password123!",
        "day": "10",
        "month": "May",
        "year": "1995",
        "first_name": label.replace(" ", ""),
        "last_name": "Tester",
        "company": "Capstone QA",
        "address1": "123 Selenium Street",
        "address2": "Suite 26",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "M5V2T6",
        "mobile": "1234567890",
    }


def cleanup_account(app, user):
    try:
        if not app.is_logged_in():
            app.login_user(user["email"], user["password"], expect_success=True)
        app.delete_account_if_logged_in()
    except Exception:
        logger.warning("Account cleanup did not complete for %s", user["email"], exc_info=True)


@allure.feature("Official AutomationExercise Cases")
class TestOfficialAutomationExercise:
    @allure.title("TC01: Register User")
    def test_01_register_user(self, app):
        user = make_user("TC01 User")
        try:
            app.open_home()
            app.register_new_user(user)
        finally:
            cleanup_account(app, user)

    @allure.title("TC02: Login User with correct email and password")
    def test_02_login_user_with_correct_credentials(self, app):
        user = make_user("TC02 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.logout()
            app.login_user(user["email"], user["password"], expect_success=True)
            app.assert_logged_in_as(user["name"])
        finally:
            cleanup_account(app, user)

    @allure.title("TC03: Login User with incorrect email and password")
    def test_03_login_user_with_incorrect_credentials(self, app):
        app.open_home()
        app.click_signup_login()
        app.login_user(f"missing_{uuid4().hex[:8]}@example.com", "WrongPassword!", expect_success=False)
        app.assert_login_error()

    @allure.title("TC04: Logout User")
    def test_04_logout_user(self, app):
        user = make_user("TC04 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.logout()
            app.login_user(user["email"], user["password"], expect_success=True)
            app.logout()
            assert "login" in app.driver.current_url
        finally:
            cleanup_account(app, user)

    @allure.title("TC05: Register User with existing email")
    def test_05_register_user_with_existing_email(self, app):
        user = make_user("TC05 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.logout()
            app.signup_new_user(user)
            app.assert_existing_email_error()
        finally:
            cleanup_account(app, user)

    @allure.title("TC06: Contact Us Form")
    def test_06_contact_us_form(self, app):
        app.open_home()
        app.click_contact_us()
        app.submit_contact_form(
            name="Capstone Tester",
            email="contact@example.com",
            subject="Automation test message",
            message="This contact form submission is created by the Selenium capstone suite.",
            upload_path=UPLOAD_FILE,
        )
        app.click_home_button()

    @allure.title("TC07: Verify Test Cases Page")
    def test_07_verify_test_cases_page(self, app):
        app.open_home()
        app.click_test_cases()
        app.assert_test_cases_page()

    @allure.title("TC08: Verify All Products and product detail page")
    def test_08_verify_products_and_product_detail(self, app):
        app.open_home()
        app.click_products()
        app.view_first_product()
        app.assert_product_details_visible()

    @allure.title("TC09: Search Product")
    def test_09_search_product(self, app):
        app.open_home()
        app.click_products()
        app.search_product("Tshirt")

    @allure.title("TC10: Verify Subscription in home page")
    def test_10_home_page_subscription(self, app):
        app.open_home()
        app.assert_subscription_visible()
        app.subscribe(f"home_{uuid4().hex[:8]}@example.com")

    @allure.title("TC11: Verify Subscription in Cart page")
    def test_11_cart_page_subscription(self, app):
        app.open_home()
        app.click_cart()
        app.assert_subscription_visible()
        app.subscribe(f"cart_{uuid4().hex[:8]}@example.com")

    @allure.title("TC12: Add Products in Cart")
    def test_12_add_products_in_cart(self, app):
        app.open_home()
        app.click_products()
        app.add_product_to_cart(product_id="1", view_cart=False)
        app.add_product_to_cart(product_id="2", view_cart=True)
        app.assert_cart_contains_product_ids(["1", "2"])
        app.assert_cart_item_calculations()

    @allure.title("TC13: Verify Product quantity in Cart")
    def test_13_verify_product_quantity_in_cart(self, app):
        app.open_home()
        app.open_product_details(product_id=1)
        app.set_product_quantity_and_add_to_cart(quantity=4)
        assert app.cart_quantity_for_product("1") == 4

    @allure.title("TC14: Place Order - Register while Checkout")
    def test_14_place_order_register_while_checkout(self, app):
        user = make_user("TC14 User")
        try:
            app.open_home()
            app.click_products()
            app.add_product_to_cart(product_id="1", view_cart=True)
            app.proceed_to_checkout()
            app.click_register_login_from_checkout_modal()
            app.signup_new_user(user)
            app.fill_account_information(user)
            app.complete_account_creation()
            app.assert_logged_in_as(user["name"])
            app.open_cart()
            app.proceed_to_checkout()
            app.assert_checkout_page()
            app.place_order()
            app.pay_and_confirm_order()
        finally:
            cleanup_account(app, user)

    @allure.title("TC15: Place Order - Register before Checkout")
    def test_15_place_order_register_before_checkout(self, app):
        user = make_user("TC15 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.click_products()
            app.add_product_to_cart(product_id="1", view_cart=True)
            app.proceed_to_checkout()
            app.assert_checkout_page()
            app.place_order()
            app.pay_and_confirm_order()
        finally:
            cleanup_account(app, user)

    @allure.title("TC16: Place Order - Login before Checkout")
    def test_16_place_order_login_before_checkout(self, app):
        user = make_user("TC16 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.logout()
            app.login_user(user["email"], user["password"], expect_success=True)
            app.click_products()
            app.add_product_to_cart(product_id="1", view_cart=True)
            app.proceed_to_checkout()
            app.assert_checkout_page()
            app.place_order()
            app.pay_and_confirm_order()
        finally:
            cleanup_account(app, user)

    @allure.title("TC17: Remove Products From Cart")
    def test_17_remove_products_from_cart(self, app):
        app.open_home()
        app.click_products()
        app.add_product_to_cart(product_id="1", view_cart=True)
        app.assert_cart_contains_product_ids(["1"])
        app.remove_cart_item("1")
        app.assert_cart_empty()

    @allure.title("TC18: View Category Products")
    def test_18_view_category_products(self, app):
        app.open_home()
        app.view_category_products()

    @allure.title("TC19: View & Cart Brand Products")
    def test_19_view_brand_products(self, app):
        app.open_home()
        app.click_products()
        app.assert_brands_visible()
        app.click_brand("Polo")
        app.assert_brand_page("Polo")
        app.click_brand("H&M")
        app.assert_brand_page("H&M")

    @allure.title("TC20: Search Products and Verify Cart After Login")
    def test_20_search_products_and_cart_after_login(self, app):
        user = make_user("TC20 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.logout()
            app.open_products()
            app.search_product("Top")
            product_ids = app.visible_product_ids(limit=2)
            assert product_ids, "No searched products were available to add to cart"
            for index, product_id in enumerate(product_ids):
                app.add_product_to_cart(product_id=product_id, view_cart=index == len(product_ids) - 1)
            app.assert_cart_contains_product_ids(product_ids)
            app.click_signup_login()
            app.login_user(user["email"], user["password"], expect_success=True)
            app.open_cart()
            app.assert_cart_contains_product_ids(product_ids)
            app.remove_all_cart_items()
            app.assert_cart_empty()
        finally:
            cleanup_account(app, user)

    @allure.title("TC21: Add review on product")
    def test_21_add_review_on_product(self, app):
        app.open_home()
        app.click_products()
        app.view_first_product()
        app.submit_product_review(
            name="Capstone Reviewer",
            email=f"review_{uuid4().hex[:8]}@example.com",
            review="Great product. Review submitted from the capstone automation suite.",
        )

    @allure.title("TC22: Add to cart from Recommended items")
    def test_22_add_to_cart_from_recommended_items(self, app):
        app.open_home()
        app.scroll_to_bottom()
        app.assert_text_visible("RECOMMENDED ITEMS")
        app.add_recommended_item_to_cart()
        app.assert_cart_has_items(min_count=1)

    @allure.title("TC23: Verify address details in checkout page")
    def test_23_verify_address_details_in_checkout(self, app):
        user = make_user("TC23 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.click_products()
            app.add_product_to_cart(product_id="1", view_cart=True)
            app.proceed_to_checkout()
            app.assert_checkout_page()
            app.assert_checkout_address_matches(user)
        finally:
            cleanup_account(app, user)

    @allure.title("TC24: Download Invoice after purchase order")
    def test_24_download_invoice_after_purchase(self, app):
        user = make_user("TC24 User")
        try:
            app.open_home()
            app.register_new_user(user)
            app.click_products()
            app.add_product_to_cart(product_id="1", view_cart=True)
            app.proceed_to_checkout()
            app.assert_checkout_page()
            app.place_order()
            app.pay_and_confirm_order()
            invoice = app.download_invoice(DOWNLOAD_DIR)
            assert invoice.exists() and invoice.stat().st_size > 0
        finally:
            cleanup_account(app, user)

    @allure.title("TC25: Verify Scroll Up using Arrow button and Scroll Down functionality")
    def test_25_scroll_up_using_arrow_button(self, app):
        app.open_home()
        app.scroll_to_bottom()
        app.assert_text_visible("SUBSCRIPTION")
        app.click_scroll_up_arrow()
        app.assert_top_banner_visible()

    @allure.title("TC26: Verify Scroll Up without Arrow button and Scroll Down functionality")
    def test_26_scroll_up_without_arrow_button(self, app):
        app.open_home()
        app.scroll_to_bottom()
        app.assert_text_visible("SUBSCRIPTION")
        app.scroll_to_top()
        app.assert_top_banner_visible()
