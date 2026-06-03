import time


def build_user(prefix="testuser"):
    """Build unique user data for independent account tests."""
    return {
        "name": "Test User",
        "email": f"{prefix}_{int(time.time() * 1000)}@example.com",
        "password": "TestPass123!",
        "first_name": "Test",
        "last_name": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "address2": "Apt 101",
        "country": "United States",
        "state": "Texas",
        "city": "Houston",
        "zipcode": "77001",
        "mobile": "1234567890",
    }


def create_account_from_signup_page(login_page, action_delay, user):
    """Create a user from the login/signup page and leave the user logged in."""
    login_page.enter_signup_name(user["name"])
    login_page.enter_signup_email(user["email"])
    login_page.click_signup_button()
    action_delay(2)

    assert login_page.is_account_info_visible()
    login_page.select_title_mr()
    login_page.enter_reg_password(user["password"])
    login_page.select_date_of_birth("15", "5", "1990")
    login_page.check_newsletter()
    login_page.check_special_offers()
    login_page.enter_first_name(user["first_name"])
    login_page.enter_last_name(user["last_name"])
    login_page.enter_company(user["company"])
    login_page.enter_address(user["address1"])
    login_page.enter_address2(user["address2"])
    login_page.select_country(user["country"])
    login_page.enter_state(user["state"])
    login_page.enter_city(user["city"])
    login_page.enter_zipcode(user["zipcode"])
    login_page.enter_mobile_number(user["mobile"])
    login_page.click_create_account()
    action_delay(3)

    assert login_page.is_account_created_visible()
    login_page.click_continue()
    action_delay(3)
    assert login_page.is_logged_in_visible()


def login_existing_user(login_page, email, password, action_delay):
    """Login with credentials from the current signup/login page."""
    login_page.enter_login_email(email)
    action_delay(0.5)
    login_page.enter_login_password(password)
    action_delay(0.5)
    login_page.click_login_button()
    action_delay(3)
    assert login_page.is_logged_in_visible()
