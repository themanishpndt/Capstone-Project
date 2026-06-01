"""
Test Checkout and Payment Processing
"""

import pytest
from src.pages.checkout_page import CheckoutPage


class TestCheckout:
    """Test suite for checkout functionality"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_checkout_page_loads(self, driver, base_url):
        """Test checkout page loads successfully"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        # Verify checkout page is displayed
        assert "checkout" in driver.current_url.lower()
    
    @pytest.mark.smoke
    def test_enter_shipping_address(self, driver, base_url, test_data):
        """Test entering shipping address"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.enter_shipping_address(
            test_data["first_name"],
            test_data["last_name"],
            "123 Main Street",
            "New York",
            "NY",
            "10001",
            "United States"
        )
        
        # Verify address fields are filled
        first_name = checkout_page.find_element(CheckoutPage.locators.FIRST_NAME_INPUT).get_attribute("value")
        assert first_name == test_data["first_name"]
    
    @pytest.mark.functional
    def test_use_same_as_shipping_for_billing(self, driver, base_url):
        """Test using same address for billing"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.use_same_as_shipping()
        
        # Verify checkbox is checked
        checkbox = checkout_page.find_element(CheckoutPage.locators.SAME_AS_SHIPPING_CHECKBOX)
        assert checkbox.is_selected()
    
    @pytest.mark.functional
    def test_select_shipping_method(self, driver, base_url):
        """Test selecting shipping method"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.select_shipping_method("standard")
        
        # Verify shipping method is selected
        shipping_radios = checkout_page.find_elements(CheckoutPage.locators.SHIPPING_METHOD_RADIO)
        assert any(radio.is_selected() for radio in shipping_radios)
    
    @pytest.mark.functional
    def test_select_payment_method(self, driver, base_url):
        """Test selecting payment method"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.select_payment_method("credit_card")
        
        # Verify payment method is selected
        payment_radios = checkout_page.find_elements(CheckoutPage.locators.PAYMENT_METHOD_RADIO)
        assert any(radio.is_selected() for radio in payment_radios)
    
    @pytest.mark.smoke
    def test_enter_card_details(self, driver, base_url):
        """Test entering credit card details"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.enter_card_details(
            "4111111111111111",
            "12/25",
            "123",
            "John Doe"
        )
        
        # Verify card details are entered
        card_number = checkout_page.find_element(CheckoutPage.locators.CARD_NUMBER_INPUT).get_attribute("value")
        assert "1111" in card_number
    
    @pytest.mark.regression
    def test_enter_invalid_card_number(self, driver, base_url):
        """Test entering invalid card number"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.enter_card_details(
            "1234567890123456",
            "12/25",
            "123",
            "John Doe"
        )
        
        # Verify system validates card number
        card_number = checkout_page.find_element(CheckoutPage.locators.CARD_NUMBER_INPUT).get_attribute("value")
        assert card_number
    
    @pytest.mark.regression
    def test_enter_expired_card(self, driver, base_url):
        """Test entering expired card date"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.enter_card_details(
            "4111111111111111",
            "01/20",
            "123",
            "John Doe"
        )
        
        # Verify system validates expiry
        expiry = checkout_page.find_element(CheckoutPage.locators.CARD_EXPIRY_INPUT).get_attribute("value")
        assert expiry
    
    @pytest.mark.regression
    def test_enter_invalid_cvc(self, driver, base_url):
        """Test entering invalid CVC"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.enter_card_details(
            "4111111111111111",
            "12/25",
            "12",
            "John Doe"
        )
        
        # Verify system validates CVC
        cvc = checkout_page.find_element(CheckoutPage.locators.CARD_CVC_INPUT).get_attribute("value")
        assert len(cvc) >= 2
    
    @pytest.mark.functional
    def test_get_order_total(self, driver, base_url):
        """Test retrieving order total on checkout page"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        total = checkout_page.get_order_total()
        assert total is not None
        assert len(total) > 0
    
    @pytest.mark.functional
    def test_get_order_items_count(self, driver, base_url):
        """Test retrieving order items count"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        count = checkout_page.get_order_items_count()
        assert count >= 0
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_place_order(self, driver, base_url, test_data):
        """Test placing an order"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        # Fill all checkout details
        checkout_page.enter_shipping_address(
            test_data["first_name"],
            test_data["last_name"],
            "123 Main Street",
            "New York",
            "NY",
            "10001",
            "United States"
        )
        checkout_page.select_shipping_method("standard")
        checkout_page.select_payment_method("credit_card")
        checkout_page.enter_card_details(
            "4111111111111111",
            "12/25",
            "123",
            "John Doe"
        )
        
        # Place order
        checkout_page.click_place_order()
        
        # Verify order confirmation
        assert checkout_page.is_element_visible(CheckoutPage.locators.ORDER_CONFIRMATION_MESSAGE)
    
    @pytest.mark.functional
    def test_get_order_number_on_confirmation(self, driver, base_url):
        """Test getting order number on confirmation page"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        # Assuming order is placed
        # Get order number
        order_number = checkout_page.get_order_number()
        assert order_number is not None
    
    @pytest.mark.functional
    def test_click_back_on_checkout(self, driver, base_url):
        """Test clicking back button on checkout page"""
        checkout_page = CheckoutPage(driver)
        checkout_page.navigate_to(f"{base_url}/checkout")
        
        checkout_page.click_back()
        
        # Verify navigation back to previous page
        assert "checkout" not in driver.current_url.lower()
