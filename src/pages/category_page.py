"""
Category Page class - Page Object Model
"""

from src.pages.base_page import BasePage
from src.locators.category_locators import CategoryLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()

    def is_category_section_visible(self):
        return self.is_element_visible(
            self.locators.CATEGORY_SECTION
        )

    def click_women_category(self):
        self.click_element(
            self.locators.WOMEN_CATEGORY
        )

    def _open_subcategory(self, locator):
        try:
            self.click_element(locator)
        except TimeoutException:
            subcategory = self.wait.until(EC.presence_of_element_located(locator))
            href = subcategory.get_attribute("href")
            if href:
                self.navigate_to(href)
            else:
                self.driver.execute_script("arguments[0].click();", subcategory)
        self.wait_for_url_contains("/category_products/")

    def wait_for_category_title_contains(self, expected_text):
        self.wait.until(
            lambda driver: expected_text.upper() in self.get_category_title().upper()
        )

    def click_women_dress_subcategory(self):
        self._open_subcategory(self.locators.WOMEN_DRESS_SUBCATEGORY)

    def click_men_category(self):
        self.click_element(
            self.locators.MEN_CATEGORY
        )

    def click_men_tshirts_subcategory(self):
        self._open_subcategory(self.locators.MEN_TSHIRTS_SUBCATEGORY)

    def get_category_title(self):
        return self.get_text(
            self.locators.CATEGORY_TITLE
        )

    def get_product_count(self):
        return len(
            self.find_elements(
                self.locators.PRODUCT_ITEMS
            )
        )

    def verify_category_page_loaded(self):
        return self.get_product_count() > 0
