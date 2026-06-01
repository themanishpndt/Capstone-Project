"""
Utility Functions for Wait Conditions
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def wait_for_element_visibility(driver, locator, timeout=20):
    """Wait for element to be visible"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_element_clickable(driver, locator, timeout=20):
    """Wait for element to be clickable"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_element_presence(driver, locator, timeout=20):
    """Wait for element to be present in DOM"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False


def wait_for_url_to_contain(driver, url_fragment, timeout=20):
    """Wait for URL to contain specific fragment"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.url_contains(url_fragment)
        )
        return True
    except TimeoutException:
        return False


def wait_for_text_in_element(driver, locator, text, timeout=20):
    """Wait for element to contain specific text"""
    try:
        WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
        return True
    except TimeoutException:
        return False
