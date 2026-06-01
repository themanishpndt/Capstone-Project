"""
Page object for the official AutomationExercise capstone test cases.
"""

import os
import re
import time
from pathlib import Path

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoAlertPresentException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from src.pages.base_page import BasePage


class AutomationExercisePage(BasePage):
    """High-level page object for the public AutomationExercise site."""

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url.rstrip("/")
        explicit_wait = int(os.getenv("EXPLICIT_WAIT", 25))
        self.wait = WebDriverWait(driver, explicit_wait)
        self.short_wait = WebDriverWait(driver, 5)

    def _url(self, path):
        path = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url}{path}"

    @staticmethod
    def _xpath_literal(value):
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ', "\'", '.join(f"'{part}'" for part in parts) + ")"

    def _text_locator(self, text):
        normalized = "translate(normalize-space(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
        return (By.XPATH, f"//*[contains({normalized}, {self._xpath_literal(text.lower())})]")

    def _hide_ad_frames(self):
        try:
            self.driver.execute_script(
                """
                for (const el of document.querySelectorAll(
                    "iframe[id^='aswift'], iframe[name^='aswift'], ins.adsbygoogle, [id^='google_vignette']"
                )) {
                    el.style.pointerEvents = 'none';
                    el.style.display = 'none';
                }
                """
            )
        except WebDriverException:
            pass

    def _elements(self, locator, timeout=0):
        implicit_wait = int(os.getenv("IMPLICIT_WAIT", 15))
        self.driver.implicitly_wait(0)
        try:
            if timeout:
                WebDriverWait(self.driver, timeout).until(
                    lambda driver: driver.find_elements(*locator)
                )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []
        finally:
            self.driver.implicitly_wait(implicit_wait)

    def _click(self, locator, timeout=None):
        self._hide_ad_frames()
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except (ElementClickInterceptedException, WebDriverException):
            self.driver.execute_script("arguments[0].click();", element)
        return element

    def _click_element(self, element):
        self._hide_ad_frames()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except (ElementClickInterceptedException, WebDriverException):
            self.driver.execute_script("arguments[0].click();", element)

    def _type(self, locator, value):
        self._hide_ad_frames()
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.clear()
        element.send_keys(value)
        return element

    def _select_by_text(self, locator, text):
        Select(self.wait.until(EC.visibility_of_element_located(locator))).select_by_visible_text(text)

    def _set_checkbox(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        if not element.is_selected():
            self.driver.execute_script("arguments[0].click();", element)

    def _accept_alert_if_present(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except (NoAlertPresentException, TimeoutException):
            pass

    def assert_text_visible(self, text, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(self._text_locator(text)))

    def open_home(self):
        self.navigate_to(self._url("/"))
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.assert_home_visible()

    def assert_home_visible(self):
        self.assert_text_visible("Full-Fledged practice website for Automation Engineers")

    def open_login(self):
        self.navigate_to(self._url("/login"))
        self.assert_text_visible("Login to your account")

    def open_products(self):
        self.navigate_to(self._url("/products"))
        self.assert_all_products_page()

    def open_cart(self):
        self.navigate_to(self._url("/view_cart"))
        self.wait.until(EC.url_contains("view_cart"))

    def open_product_details(self, product_id=1):
        self.navigate_to(self._url(f"/product_details/{product_id}"))
        self.wait.until(EC.url_contains("/product_details/"))

    def click_signup_login(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Signup / Login')]"))
        self.assert_text_visible("New User Signup!")

    def click_products(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Products')]"))
        self.assert_all_products_page()

    def click_cart(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Cart')]"))
        self.wait.until(EC.url_contains("view_cart"))

    def click_contact_us(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Contact us')]"))
        self.wait.until(EC.url_contains("contact_us"))

    def click_test_cases(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Test Cases')]"))
        self.wait.until(EC.url_contains("test_cases"))

    def click_home_button(self):
        self._click((By.XPATH, "//a[contains(@class, 'btn') and normalize-space()='Home']"))
        self.assert_home_visible()

    def signup_new_user(self, user):
        self.assert_text_visible("New User Signup!")
        self._type((By.CSS_SELECTOR, "[data-qa='signup-name']"), user["name"])
        self._type((By.CSS_SELECTOR, "[data-qa='signup-email']"), user["email"])
        self._click((By.CSS_SELECTOR, "[data-qa='signup-button']"))
        self.assert_text_visible("ENTER ACCOUNT INFORMATION")

    def fill_account_information(self, user):
        gender_id = "id_gender1" if user.get("title", "Mr") == "Mr" else "id_gender2"
        self._click((By.ID, gender_id))
        self._type((By.CSS_SELECTOR, "[data-qa='password']"), user["password"])
        self._select_by_text((By.ID, "days"), user.get("day", "10"))
        self._select_by_text((By.ID, "months"), user.get("month", "May"))
        self._select_by_text((By.ID, "years"), user.get("year", "1995"))
        self._set_checkbox((By.ID, "newsletter"))
        self._set_checkbox((By.ID, "optin"))
        self._type((By.CSS_SELECTOR, "[data-qa='first_name']"), user["first_name"])
        self._type((By.CSS_SELECTOR, "[data-qa='last_name']"), user["last_name"])
        self._type((By.CSS_SELECTOR, "[data-qa='company']"), user["company"])
        self._type((By.CSS_SELECTOR, "[data-qa='address']"), user["address1"])
        self._type((By.CSS_SELECTOR, "[data-qa='address2']"), user["address2"])
        self._select_by_text((By.CSS_SELECTOR, "[data-qa='country']"), user["country"])
        self._type((By.CSS_SELECTOR, "[data-qa='state']"), user["state"])
        self._type((By.CSS_SELECTOR, "[data-qa='city']"), user["city"])
        self._type((By.CSS_SELECTOR, "[data-qa='zipcode']"), user["zipcode"])
        self._type((By.CSS_SELECTOR, "[data-qa='mobile_number']"), user["mobile"])
        self._click((By.CSS_SELECTOR, "[data-qa='create-account']"))

    def complete_account_creation(self):
        self.assert_text_visible("ACCOUNT CREATED!")
        self._click((By.CSS_SELECTOR, "[data-qa='continue-button']"))

    def register_new_user(self, user):
        self.click_signup_login()
        self.signup_new_user(user)
        self.fill_account_information(user)
        self.complete_account_creation()
        self.assert_logged_in_as(user["name"])

    def login_user(self, email, password, expect_success=True):
        if not self._elements((By.CSS_SELECTOR, "[data-qa='login-email']"), timeout=2):
            self.open_login()
        self._type((By.CSS_SELECTOR, "[data-qa='login-email']"), email)
        self._type((By.CSS_SELECTOR, "[data-qa='login-password']"), password)
        self._click((By.CSS_SELECTOR, "[data-qa='login-button']"))
        if expect_success:
            self.assert_text_visible("Logged in as")

    def logout(self):
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Logout')]"))
        self.wait.until(EC.url_contains("login"))

    def is_logged_in(self):
        return bool(self._elements((By.XPATH, "//a[contains(normalize-space(), 'Logged in as')]"), timeout=1))

    def assert_logged_in_as(self, name):
        self.assert_text_visible(f"Logged in as {name}")

    def assert_login_error(self):
        self.assert_text_visible("Your email or password is incorrect!")

    def assert_existing_email_error(self):
        self.assert_text_visible("Email Address already exist!")

    def delete_account_if_logged_in(self):
        if not self.is_logged_in():
            return False
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Delete Account')]"))
        self.assert_text_visible("ACCOUNT DELETED!")
        self._click((By.CSS_SELECTOR, "[data-qa='continue-button']"))
        return True

    def submit_contact_form(self, name, email, subject, message, upload_path=None):
        self.assert_text_visible("GET IN TOUCH")
        self._type((By.CSS_SELECTOR, "[data-qa='name']"), name)
        self._type((By.CSS_SELECTOR, "[data-qa='email']"), email)
        self._type((By.CSS_SELECTOR, "[data-qa='subject']"), subject)
        self._type((By.CSS_SELECTOR, "[data-qa='message']"), message)
        if upload_path:
            self.wait.until(EC.presence_of_element_located((By.NAME, "upload_file"))).send_keys(
                str(upload_path)
            )
        self._click((By.CSS_SELECTOR, "[data-qa='submit-button']"))
        self._accept_alert_if_present()
        self.assert_text_visible("Success! Your details have been submitted successfully.")

    def assert_test_cases_page(self):
        self.assert_text_visible("TEST CASES")
        assert "test_cases" in self.driver.current_url

    def assert_all_products_page(self):
        self.wait.until(EC.url_contains("/products"))
        self.assert_text_visible("ALL PRODUCTS")
        assert self.product_count() > 0, "No products are visible on products page"

    def product_count(self):
        return len(self._elements((By.CSS_SELECTOR, ".features_items .product-image-wrapper"), timeout=10))

    def view_first_product(self):
        links = self._elements((By.CSS_SELECTOR, ".features_items a[href*='/product_details/']"), timeout=10)
        if not links:
            raise AssertionError("No product detail links found")
        product_url = links[0].get_attribute("href")
        if not product_url:
            raise AssertionError("First product detail link does not have an href")
        self.navigate_to(product_url)
        self.wait.until(EC.url_contains("/product_details/"))

    def assert_product_details_visible(self):
        product_info = (By.CSS_SELECTOR, ".product-information")
        self.wait.until(EC.visibility_of_element_located(product_info))
        required = [
            (By.CSS_SELECTOR, ".product-information h2"),
            (By.XPATH, "//div[contains(@class, 'product-information')]//p[contains(., 'Category')]"),
            (By.XPATH, "//div[contains(@class, 'product-information')]//*[contains(., 'Rs.')]"),
            (By.XPATH, "//div[contains(@class, 'product-information')]//b[contains(., 'Availability')]"),
            (By.XPATH, "//div[contains(@class, 'product-information')]//b[contains(., 'Condition')]"),
            (By.XPATH, "//div[contains(@class, 'product-information')]//b[contains(., 'Brand')]"),
        ]
        missing = [locator for locator in required if not self._elements(locator, timeout=5)]
        assert not missing, f"Product details missing expected fields: {missing}"

    def search_product(self, term):
        self._type((By.ID, "search_product"), term)
        self._click((By.ID, "submit_search"))
        self.assert_text_visible("SEARCHED PRODUCTS")
        assert self.product_count() > 0, f"No search results found for {term}"

    def visible_product_ids(self, limit=None):
        buttons = self._elements((By.CSS_SELECTOR, ".features_items .productinfo a.add-to-cart"), timeout=10)
        product_ids = []
        for button in buttons:
            product_id = button.get_attribute("data-product-id")
            if product_id and product_id not in product_ids:
                product_ids.append(product_id)
            if limit and len(product_ids) >= limit:
                break
        return product_ids

    def add_product_to_cart(self, product_id=None, view_cart=False):
        selector = ".features_items .productinfo a.add-to-cart"
        if product_id:
            selector = f".features_items .productinfo a.add-to-cart[data-product-id='{product_id}']"
        buttons = self._elements((By.CSS_SELECTOR, selector), timeout=10)
        if not buttons:
            raise AssertionError(f"No add-to-cart button found for product {product_id or 'first visible'}")
        self._click_element(buttons[0])
        self._handle_cart_modal(view_cart=view_cart)

    def _handle_cart_modal(self, view_cart=False):
        self.wait.until(EC.visibility_of_element_located((By.ID, "cartModal")))
        if view_cart:
            self._click((By.XPATH, "//div[@id='cartModal']//u[normalize-space()='View Cart']/ancestor::a"))
            self.wait.until(EC.url_contains("view_cart"))
        else:
            self._click((By.XPATH, "//div[@id='cartModal']//button[contains(., 'Continue Shopping')]"))

    def add_recommended_item_to_cart(self):
        buttons = self._elements((By.CSS_SELECTOR, ".recommended_items a.add-to-cart"), timeout=10)
        visible_buttons = [button for button in buttons if button.is_displayed()]
        target = visible_buttons[0] if visible_buttons else buttons[0]
        self._click_element(target)
        self._handle_cart_modal(view_cart=True)

    def cart_rows(self):
        return self._elements((By.CSS_SELECTOR, "#cart_info_table tbody tr[id^='product-']"), timeout=5)

    def assert_cart_has_items(self, min_count=1):
        self.wait.until(lambda _driver: len(self.cart_rows()) >= min_count)

    def assert_cart_contains_product_ids(self, product_ids):
        self.assert_cart_has_items(len(product_ids))
        row_ids = {row.get_attribute("id").replace("product-", "") for row in self.cart_rows()}
        missing = [product_id for product_id in product_ids if str(product_id) not in row_ids]
        assert not missing, f"Missing product ids in cart: {missing}"

    @staticmethod
    def _money_to_int(value):
        digits = re.sub(r"\D", "", value)
        return int(digits) if digits else 0

    def assert_cart_item_calculations(self):
        for row in self.cart_rows():
            price = self._money_to_int(row.find_element(By.CSS_SELECTOR, ".cart_price").text)
            quantity = int(row.find_element(By.CSS_SELECTOR, ".cart_quantity button").text)
            total = self._money_to_int(row.find_element(By.CSS_SELECTOR, ".cart_total").text)
            assert price * quantity == total, (
                f"Cart total mismatch for {row.get_attribute('id')}: {price} * {quantity} != {total}"
            )

    def set_product_quantity_and_add_to_cart(self, quantity):
        self.assert_product_details_visible()
        self._type((By.ID, "quantity"), str(quantity))
        self._click((By.CSS_SELECTOR, "button.cart"))
        self._handle_cart_modal(view_cart=True)

    def cart_quantity_for_product(self, product_id):
        locator = (By.CSS_SELECTOR, f"#product-{product_id} .cart_quantity button")
        return int(self.wait.until(EC.visibility_of_element_located(locator)).text)

    def remove_cart_item(self, product_id):
        self._click((By.CSS_SELECTOR, f"#product-{product_id} .cart_quantity_delete"))
        self.wait.until(lambda _driver: not self._elements((By.ID, f"product-{product_id}"), timeout=1))

    def remove_all_cart_items(self):
        for _ in range(10):
            buttons = self._elements((By.CSS_SELECTOR, ".cart_quantity_delete"), timeout=1)
            if not buttons:
                return
            self._click_element(buttons[0])
            time.sleep(0.5)

    def assert_cart_empty(self):
        self.assert_text_visible("Cart is empty!")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.wait.until(lambda driver: driver.execute_script("return window.pageYOffset;") == 0)

    def assert_subscription_visible(self):
        self.scroll_to_bottom()
        self.assert_text_visible("SUBSCRIPTION")

    def subscribe(self, email):
        self._type((By.ID, "susbscribe_email"), email)
        self._click((By.ID, "subscribe"))
        self.assert_text_visible("You have been successfully subscribed!")

    def proceed_to_checkout(self):
        self._click(
            (
                By.XPATH,
                "//a[contains(@class, 'check_out') and contains(normalize-space(), 'Proceed To Checkout')]",
            )
        )

    def click_register_login_from_checkout_modal(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "checkoutModal")))
        self._click((By.XPATH, "//div[@id='checkoutModal']//u[normalize-space()='Register / Login']/ancestor::a"))
        self.assert_text_visible("New User Signup!")

    def assert_checkout_page(self):
        self.wait.until(EC.url_contains("/checkout"))
        self.assert_text_visible("Address Details")
        self.assert_text_visible("Review Your Order")

    def assert_checkout_address_matches(self, user):
        delivery = self.wait.until(EC.visibility_of_element_located((By.ID, "address_delivery"))).text
        billing = self.wait.until(EC.visibility_of_element_located((By.ID, "address_invoice"))).text
        expected_parts = [
            user["first_name"],
            user["last_name"],
            user["address1"],
            user["city"],
            user["state"],
            user["zipcode"],
            user["mobile"],
        ]
        for address_text in (delivery, billing):
            missing = [part for part in expected_parts if part not in address_text]
            assert not missing, f"Checkout address missing values {missing}. Address was: {address_text}"

    def place_order(self, comment="Please deliver during business hours."):
        self._type((By.NAME, "message"), comment)
        self._click((By.XPATH, "//a[contains(@class, 'check_out') and contains(normalize-space(), 'Place Order')]"))
        self.wait.until(EC.url_contains("/payment"))

    def pay_and_confirm_order(self):
        self._type((By.CSS_SELECTOR, "[data-qa='name-on-card']"), "Capstone Tester")
        self._type((By.CSS_SELECTOR, "[data-qa='card-number']"), "4111111111111111")
        self._type((By.CSS_SELECTOR, "[data-qa='cvc']"), "123")
        self._type((By.CSS_SELECTOR, "[data-qa='expiry-month']"), "12")
        self._type((By.CSS_SELECTOR, "[data-qa='expiry-year']"), "2030")
        self._click((By.CSS_SELECTOR, "[data-qa='pay-button']"))
        self.assert_order_confirmed()

    def assert_order_confirmed(self):
        self.assert_text_visible("ORDER PLACED!")
        self.assert_text_visible("Congratulations! Your order has been confirmed!")

    def download_invoice(self, download_dir):
        download_dir = Path(download_dir)
        download_dir.mkdir(parents=True, exist_ok=True)
        before = {
            path.name: path.stat().st_mtime_ns
            for path in download_dir.glob("*")
            if path.is_file()
        }
        self._click((By.XPATH, "//a[contains(normalize-space(), 'Download Invoice')]"))
        deadline = time.time() + 20
        while time.time() < deadline:
            for path in download_dir.glob("*"):
                if path.suffix == ".crdownload" or not path.is_file():
                    continue
                if path.name not in before or path.stat().st_mtime_ns != before[path.name]:
                    return path
            time.sleep(0.5)
        raise AssertionError(f"Invoice was not downloaded to {download_dir}")

    def assert_categories_visible(self):
        self.assert_text_visible("CATEGORY")

    def view_category_products(self):
        self.assert_categories_visible()
        self._click((By.CSS_SELECTOR, "a[href='#Women']"))
        self._click((By.CSS_SELECTOR, "#Women a[href='/category_products/1']"))
        self.assert_text_visible("WOMEN - DRESS PRODUCTS")
        self._click((By.CSS_SELECTOR, "a[href='#Men']"))
        self._click((By.CSS_SELECTOR, "#Men a[href='/category_products/3']"))
        self.assert_text_visible("MEN - TSHIRTS PRODUCTS")

    def assert_brands_visible(self):
        self.assert_text_visible("BRANDS")

    def click_brand(self, brand_name):
        self._click(
            (
                By.XPATH,
                "//div[contains(@class, 'brands_products')]"
                f"//a[contains(normalize-space(), {self._xpath_literal(brand_name)})]",
            )
        )
        self.wait.until(EC.url_contains("brand_products"))

    def assert_brand_page(self, brand_name):
        self.assert_text_visible(f"BRAND - {brand_name.upper()} PRODUCTS")
        assert self.product_count() > 0, f"No products visible for brand {brand_name}"

    def assert_write_review_visible(self):
        self.assert_text_visible("WRITE YOUR REVIEW")

    def submit_product_review(self, name, email, review):
        self.assert_write_review_visible()
        self._type((By.ID, "name"), name)
        self._type((By.ID, "email"), email)
        self._type((By.ID, "review"), review)
        self._click((By.ID, "button-review"))
        self.assert_text_visible("Thank you for your review.")

    def click_scroll_up_arrow(self):
        self._click((By.ID, "scrollUp"))
        self.wait.until(lambda driver: driver.execute_script("return window.pageYOffset;") == 0)

    def assert_top_banner_visible(self):
        self.assert_text_visible("Full-Fledged practice website for Automation Engineers")
