"""
Test Case 10: Verify Subscription in Home Page
Verify subscription functionality on the home page
"""

import pytest
import allure
import logging
from src.pages.home_page import HomePage
from src.pages.subscription_page import SubscriptionPage

logger = logging.getLogger(__name__)


class TestHomeSubscription:
    """Test suite for Home page subscription"""
    
    @pytest.mark.smoke
    @pytest.mark.functional
    @allure.title("TC10: Verify Subscription in Home Page")
    @allure.description("Verify that user can subscribe via email in home page section")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_page_subscription(self, driver, base_url):
        """Test subscription in home page"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Subscribe with valid email"):
            subscription_page = SubscriptionPage(driver)
            subscription_page.subscribe_home_page("testuser@example.com")
        
        with allure.step("Verify subscription success"):
            assert subscription_page.is_home_subscription_success_visible(), \
                "Subscription success message not displayed"
            logger.info("Home page subscription successful")
    
    @pytest.mark.regression
    @allure.title("TC10: Home Subscription with Multiple Emails")
    @allure.description("Verify subscription works with different email formats")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("email", [
        "user1@test.com",
        "user2@example.org",
        "user3@domain.co.uk"
    ])
    def test_home_subscription_multiple_emails(self, driver, base_url, email):
        """Test subscription with multiple email formats"""
        with allure.step(f"Subscribe with email: {email}"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
            
            subscription_page = SubscriptionPage(driver)
            subscription_page.subscribe_home_page(email)
        
        with allure.step("Verify success"):
            assert subscription_page.is_home_subscription_success_visible(), \
                f"Subscription failed for {email}"
            logger.info(f"Subscription successful for {email}")
    
    @pytest.mark.regression
    @allure.title("TC10: Verify Subscription Section Visibility")
    @allure.description("Verify subscription section is visible on home page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_subscription_section_visibility(self, driver, base_url):
        """Test subscription section visibility"""
        with allure.step("Navigate to home page"):
            home_page = HomePage(driver)
            home_page.navigate_to_home()
        
        with allure.step("Scroll to subscription section"):
            home_page.scroll_to_footer()
        
        with allure.step("Verify footer subscription section"):
            subscription_page = SubscriptionPage(driver)
            is_visible = subscription_page.is_element_visible(
                subscription_page.locators.FOOTER_SUBSCRIPTION_EMAIL
            )
            assert is_visible, "Footer subscription section not visible"
            logger.info("Subscription section is visible on home page")
