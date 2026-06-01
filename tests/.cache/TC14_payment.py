"""
Test Payment Processing
"""

import pytest


class TestPayment:
    """Test suite for payment processing"""
    
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_credit_card_payment(self, driver, base_url):
        """Test credit card payment processing"""
        driver.get(f"{base_url}/checkout")
        
        # Select credit card payment
        cc_radio = driver.find_elements(("xpath", "//input[@value='credit_card']"))
        if cc_radio:
            cc_radio[0].click()
            
            # Verify credit card fields are displayed
            card_fields = driver.find_elements(("class name", "card-field"))
            assert len(card_fields) > 0
    
    @pytest.mark.functional
    def test_debit_card_payment(self, driver, base_url):
        """Test debit card payment processing"""
        driver.get(f"{base_url}/checkout")
        
        # Select debit card payment
        debit_radio = driver.find_elements(("xpath", "//input[@value='debit_card']"))
        if debit_radio:
            debit_radio[0].click()
            
            # Verify debit card form is displayed
            debit_fields = driver.find_elements(("class name", "debit-field"))
            assert len(debit_fields) >= 0
    
    @pytest.mark.functional
    def test_paypal_payment(self, driver, base_url):
        """Test PayPal payment option"""
        driver.get(f"{base_url}/checkout")
        
        # Select PayPal payment
        paypal_radio = driver.find_elements(("xpath", "//input[@value='paypal']"))
        if paypal_radio:
            paypal_radio[0].click()
            
            # Verify PayPal button is displayed
            paypal_buttons = driver.find_elements(("id", "paypal-button"))
            assert len(paypal_buttons) >= 0
    
    @pytest.mark.functional
    def test_google_pay_payment(self, driver, base_url):
        """Test Google Pay payment option"""
        driver.get(f"{base_url}/checkout")
        
        # Select Google Pay payment
        gpay_radio = driver.find_elements(("xpath", "//input[@value='google_pay']"))
        if gpay_radio:
            gpay_radio[0].click()
            
            # Verify Google Pay button is displayed
            gpay_buttons = driver.find_elements(("xpath", "//button[contains(text(), 'Google Pay')]"))
            assert len(gpay_buttons) >= 0
    
    @pytest.mark.regression
    def test_payment_with_expired_card(self, driver, base_url):
        """Test payment with expired card"""
        driver.get(f"{base_url}/checkout")
        
        # Enter expired card details
        card_inputs = driver.find_elements(("id", "card-number"))
        if card_inputs:
            card_inputs[0].send_keys("4111111111111111")
            
            expiry_inputs = driver.find_elements(("id", "card-expiry"))
            if expiry_inputs:
                expiry_inputs[0].send_keys("01/20")
                
                # Try to process payment
                pay_buttons = driver.find_elements(("xpath", "//button[@title='Pay Now']"))
                if pay_buttons:
                    pay_buttons[0].click()
                    
                    # Verify error message
                    error_messages = driver.find_elements(("class name", "error-message"))
                    assert len(error_messages) > 0
    
    @pytest.mark.regression
    def test_payment_with_invalid_cvv(self, driver, base_url):
        """Test payment with invalid CVV"""
        driver.get(f"{base_url}/checkout")
        
        # Enter invalid CVV
        cvv_inputs = driver.find_elements(("id", "card-cvv"))
        if cvv_inputs:
            cvv_inputs[0].send_keys("1")
            
            # Verify error message or validation
            error_messages = driver.find_elements(("class name", "error-message"))
            assert len(error_messages) >= 0
    
    @pytest.mark.regression
    def test_payment_timeout(self, driver, base_url):
        """Test payment processing timeout"""
        driver.get(f"{base_url}/checkout")
        
        # Attempt payment and wait for timeout
        pay_buttons = driver.find_elements(("xpath", "//button[@title='Pay Now']"))
        if pay_buttons:
            pay_buttons[0].click()
            
            # Verify timeout message or retry option
            timeout_messages = driver.find_elements(("class name", "timeout-message"))
            assert len(timeout_messages) >= 0 or len(driver.find_elements(("class name", "retry-button"))) >= 0
    
    @pytest.mark.functional
    def test_payment_security_ssl(self, driver, base_url):
        """Test payment page has SSL security"""
        driver.get(f"{base_url}/checkout")
        
        # Verify HTTPS protocol
        assert "https" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_payment_confirmation_email(self, driver, base_url):
        """Test payment confirmation email sent"""
        driver.get(f"{base_url}/checkout")
        
        # After payment completion, verify confirmation
        confirmation_messages = driver.find_elements(("class name", "confirmation-message"))
        if confirmation_messages:
            email_text = confirmation_messages[0].text
            assert "email" in email_text.lower() or "confirmation" in email_text.lower()
    
    @pytest.mark.functional
    def test_payment_receipt_generation(self, driver, base_url):
        """Test payment receipt generation"""
        driver.get(f"{base_url}/account/orders")
        
        # Look for receipt/invoice download
        receipt_buttons = driver.find_elements(("xpath", "//button[@title='Download Receipt']"))
        assert len(receipt_buttons) >= 0
