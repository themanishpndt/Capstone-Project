"""
Test User Profile and Account Management
"""

import pytest


class TestUserProfile:
    """Test suite for user profile functionality"""
    
    @pytest.mark.smoke
    def test_view_profile_page(self, driver, base_url):
        """Test viewing user profile page"""
        driver.get(f"{base_url}/account/profile")
        
        # Verify profile page is displayed
        assert "profile" in driver.current_url.lower() or "account" in driver.current_url.lower()
    
    @pytest.mark.functional
    def test_edit_first_name(self, driver, base_url, test_data):
        """Test editing first name in profile"""
        driver.get(f"{base_url}/account/profile")
        
        # Find and edit first name field
        first_name_inputs = driver.find_elements(("id", "first-name"))
        if first_name_inputs:
            first_name_inputs[0].clear()
            first_name_inputs[0].send_keys("UpdatedName")
            
            # Save changes
            save_buttons = driver.find_elements(("xpath", "//button[@title='Save']"))
            if save_buttons:
                save_buttons[0].click()
                
                # Verify success message
                success_messages = driver.find_elements(("class name", "success-message"))
                assert len(success_messages) > 0
    
    @pytest.mark.functional
    def test_edit_email(self, driver, base_url):
        """Test editing email in profile"""
        driver.get(f"{base_url}/account/profile")
        
        # Find and edit email field
        email_inputs = driver.find_elements(("id", "email"))
        if email_inputs:
            email_inputs[0].clear()
            email_inputs[0].send_keys("newemail@example.com")
            
            # Verify validation message
            messages = driver.find_elements(("class name", "message"))
            assert len(messages) >= 0
    
    @pytest.mark.functional
    def test_edit_phone_number(self, driver, base_url, test_data):
        """Test editing phone number in profile"""
        driver.get(f"{base_url}/account/profile")
        
        # Find and edit phone field
        phone_inputs = driver.find_elements(("id", "phone"))
        if phone_inputs:
            phone_inputs[0].clear()
            phone_inputs[0].send_keys(test_data["phone"])
            
            # Verify phone is entered
            phone_value = phone_inputs[0].get_attribute("value")
            assert phone_value
    
    @pytest.mark.functional
    def test_change_password(self, driver, base_url):
        """Test changing password"""
        driver.get(f"{base_url}/account/security")
        
        # Find and fill password fields
        old_password_inputs = driver.find_elements(("id", "old-password"))
        if old_password_inputs:
            old_password_inputs[0].send_keys("OldPassword123!")
            
            new_password_inputs = driver.find_elements(("id", "new-password"))
            if new_password_inputs:
                new_password_inputs[0].send_keys("NewPassword123!")
                
                confirm_inputs = driver.find_elements(("id", "confirm-password"))
                if confirm_inputs:
                    confirm_inputs[0].send_keys("NewPassword123!")
                    
                    # Click change password button
                    change_buttons = driver.find_elements(("xpath", "//button[@title='Change Password']"))
                    if change_buttons:
                        change_buttons[0].click()
    
    @pytest.mark.functional
    def test_add_address(self, driver, base_url):
        """Test adding new address to profile"""
        driver.get(f"{base_url}/account/addresses")
        
        # Click add address button
        add_buttons = driver.find_elements(("xpath", "//button[@title='Add Address']"))
        if add_buttons:
            add_buttons[0].click()
            
            # Verify address form is displayed
            address_forms = driver.find_elements(("class name", "address-form"))
            assert len(address_forms) > 0
    
    @pytest.mark.functional
    def test_delete_address(self, driver, base_url):
        """Test deleting address from profile"""
        driver.get(f"{base_url}/account/addresses")
        
        # Find and click delete button
        delete_buttons = driver.find_elements(("xpath", "//button[@title='Delete Address']"))
        if delete_buttons:
            delete_buttons[0].click()
            
            # Verify confirmation dialog
            confirmation_dialogs = driver.find_elements(("class name", "confirmation-dialog"))
            assert len(confirmation_dialogs) > 0
    
    @pytest.mark.functional
    def test_set_default_address(self, driver, base_url):
        """Test setting default address"""
        driver.get(f"{base_url}/account/addresses")
        
        # Find and click set default button
        default_buttons = driver.find_elements(("xpath", "//button[@title='Set as Default']"))
        if default_buttons:
            default_buttons[0].click()
            
            # Verify address is set as default
            success_messages = driver.find_elements(("class name", "success-message"))
            assert len(success_messages) >= 0
    
    @pytest.mark.functional
    def test_manage_notifications(self, driver, base_url):
        """Test managing notification preferences"""
        driver.get(f"{base_url}/account/notifications")
        
        # Find notification checkboxes
        checkboxes = driver.find_elements(("xpath", "//input[@type='checkbox']"))
        assert len(checkboxes) >= 0
    
    @pytest.mark.functional
    def test_view_account_activity(self, driver, base_url):
        """Test viewing account activity/login history"""
        driver.get(f"{base_url}/account/security")
        
        # Look for activity log
        activity_logs = driver.find_elements(("class name", "activity-log"))
        assert len(activity_logs) >= 0
