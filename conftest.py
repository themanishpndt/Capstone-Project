"""
Pytest Configuration and Fixtures
This file contains all pytest fixtures and configurations for the test suite
Enhanced with Allure reporting and screenshot capture on failure
"""

import pytest
import logging
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import platform

# Load environment variables
load_dotenv()

# Ensure reports directories exist
os.makedirs('reports/logs', exist_ok=True)
os.makedirs('reports/screenshots', exist_ok=True)
os.makedirs('reports/allure-results', exist_ok=True)

# Configure logging with more detailed format
logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.FileHandler('reports/logs/test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser", action="store", default=os.getenv("BROWSER", "chrome"),
        help="Browser to run tests on: chrome, brave, firefox, or edge"
    )
    parser.addoption(
        "--headless", action="store_true", default=False,
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--base_url", action="store", default=os.getenv("BASE_URL", "https://automationexercise.com"),
        help="Base URL for the application"
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Fixture to provide base URL"""
    configured_url = request.config.getoption("--base_url").rstrip("/")
    if configured_url.startswith("http://automationexercise.com"):
        return configured_url.replace("http://", "https://", 1)
    return configured_url


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to initialize and teardown WebDriver
    Creates a new browser instance for each test
    """
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    
    logger.info(f"Initializing {browser} WebDriver (headless={headless})")
    download_dir = os.path.abspath(os.getenv("DOWNLOAD_DIR", "reports/downloads"))
    os.makedirs(download_dir, exist_ok=True)
    
    if browser == "chrome":
        options = ChromeOptions()
        options.page_load_strategy = os.getenv("PAGE_LOAD_STRATEGY", "eager")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )
        
        if headless:
            options.add_argument("--headless=new")
        
        driver_instance = webdriver.Chrome(
            options=options
        )
    
    elif browser == "brave":
        # Brave browser configuration (uses Chromium-based options)
        options = ChromeOptions()
        # Set Brave executable path
        brave_path = os.getenv("BRAVE_PATH", "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
        options.binary_location = brave_path
        options.page_load_strategy = os.getenv("PAGE_LOAD_STRATEGY", "eager")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )
        
        if headless:
            options.add_argument("--headless=new")
        
        driver_instance = webdriver.Chrome(
            options=options
        )
    
    elif browser == "firefox":
        options = FirefoxOptions()
        options.page_load_strategy = os.getenv("PAGE_LOAD_STRATEGY", "eager")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", download_dir)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/octet-stream")
        
        if headless:
            options.add_argument("--headless")
        
        driver_instance = webdriver.Firefox(
            options=options
        )

    elif browser == "edge":
        options = EdgeOptions()
        options.page_load_strategy = os.getenv("PAGE_LOAD_STRATEGY", "eager")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )

        if headless:
            options.add_argument("--headless=new")

        driver_instance = webdriver.Edge(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    # Set implicit and explicit waits - increased for slower test execution
    implicit_wait = int(os.getenv("IMPLICIT_WAIT", 15))  # Increased from 10 to 15
    explicit_wait = int(os.getenv("EXPLICIT_WAIT", 25))  # Increased from 20 to 25
    page_load_timeout = int(os.getenv("PAGE_LOAD_TIMEOUT", 40))  # Increased from 30 to 40
    
    driver_instance.implicitly_wait(implicit_wait)
    driver_instance.set_page_load_timeout(page_load_timeout)
    
    # Add custom wait attribute
    driver_instance.wait = WebDriverWait(driver_instance, explicit_wait)
    
    logger.info(f"WebDriver initialized successfully")
    
    yield driver_instance
    
    # Teardown
    logger.info("Closing WebDriver")
    driver_instance.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """Fixture to provide WebDriverWait instance"""
    explicit_wait = int(os.getenv("EXPLICIT_WAIT", 20))
    return WebDriverWait(driver, explicit_wait)


@pytest.fixture(scope="function")
def action_delay():
    """
    Fixture to add delays between test actions
    Helps slow down test execution for better visibility (default 2.5 seconds)
    Usage: action_delay(2.5) in your test or page object methods
    """
    def delay(seconds=2.5):
        """Add delay between actions"""
        time.sleep(seconds)
        logger.debug(f"Action delay applied: {seconds} seconds")
    
    return delay


@pytest.fixture(scope="function")
def test_data():
    """Fixture to provide test data"""
    return {
        "valid_email": "test@example.com",
        "valid_password": "Password123!",
        "invalid_email": "invalid@test.com",
        "invalid_password": "wrong_password",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "+1234567890",
    }


@pytest.fixture(scope="function", autouse=True)
def auto_action_delay(request):
    """
    Auto-use fixture that adds automatic delays between actions
    This ensures a minimum 2.5 second delay for test visibility
    """
    action_delay_time = float(os.getenv("ACTION_DELAY", 0))
    
    # Add delay before test starts
    time.sleep(0.2)
    
    yield
    
    # Add delay after test completes
    time.sleep(action_delay_time)


@pytest.fixture(scope="session")
def log_test_start_end():
    """Fixture to log test start and end"""
    logger.info("=" * 80)
    logger.info("TEST SUITE STARTED")
    logger.info(f"Timestamp: {datetime.now()}")
    logger.info("=" * 80)
    
    yield
    
    logger.info("=" * 80)
    logger.info("TEST SUITE COMPLETED")
    logger.info(f"Timestamp: {datetime.now()}")
    logger.info("=" * 80)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure
    Enhanced with Allure attachment support
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Log test failure
        logger.error(f"Test FAILED: {item.name}")
        logger.error(f"Failure details: {rep.longrepr}")
        
        # Take screenshot if driver is available
        if "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
            if driver:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_filename = f"{item.name}_{timestamp}.png"
                screenshot_path = f"reports/screenshots/{screenshot_filename}"
                
                try:
                    # Create directory if it doesn't exist
                    os.makedirs('reports/screenshots', exist_ok=True)
                    
                    # Take screenshot
                    driver.save_screenshot(screenshot_path)
                    logger.info(f"Screenshot saved: {screenshot_path}")
                    
                    # Attach screenshot to Allure report
                    with open(screenshot_path, 'rb') as image:
                        allure.attach(
                            image.read(),
                            name=screenshot_filename,
                            attachment_type=allure.attachment_type.PNG
                        )
                    logger.info(f"Screenshot attached to Allure report")
                    
                except Exception as e:
                    logger.error(f"Failed to take/attach screenshot: {e}")
        
        # Attach browser logs to Allure
        try:
            if "driver" in item.fixturenames:
                driver = item.funcargs.get("driver")
                if driver:
                    logs = driver.get_log('browser')
                    if logs:
                        log_content = json.dumps(logs, indent=2)
                        allure.attach(
                            log_content,
                            name="browser_logs.json",
                            attachment_type=allure.attachment_type.JSON
                        )
        except Exception as e:
            logger.warning(f"Could not attach browser logs: {e}")
    
    elif rep.when == "call" and rep.passed:
        logger.info(f"Test PASSED: {item.name}")
        
        # Attach browser logs on success for debugging
        if "driver" in item.fixturenames:
            try:
                driver = item.funcargs.get("driver")
                if driver:
                    current_url = driver.current_url
                    allure.attach(
                        f"Final URL: {current_url}",
                        name="page_info",
                        attachment_type=allure.attachment_type.TEXT
                    )
            except Exception as e:
                logger.warning(f"Could not attach page info: {e}")


def pytest_configure(config):
    """Configure pytest with Allure options"""
    # Add custom markers
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "critical: mark test as critical"
    )
    
    # Set Allure environment variables
    allure_env_vars = {
        "BROWSER": os.getenv("BROWSER", "chrome").lower(),
        "HEADLESS": os.getenv("HEADLESS", "False"),
        "PLATFORM": platform.system(),
        "PYTHON_VERSION": f"{platform.python_version()}",
        "SELENIUM_VERSION": f"{webdriver.__version__}",
    }
    
    logger.info(f"Test Environment: {allure_env_vars}")
    
    # Create environment.properties file for Allure
    env_file = "reports/allure-results/environment.properties"
    os.makedirs(os.path.dirname(env_file), exist_ok=True)
    with open(env_file, 'w') as f:
        for key, value in allure_env_vars.items():
            f.write(f"{key}={value}\n")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers and Allure features"""
    for item in items:
        # Add default marker if none exists
        if not item.iter_markers():
            item.add_marker(pytest.mark.functional)
        
        # Add test ID from test name
        test_class_name = item.cls.__name__ if item.cls else ""
        test_method_name = item.name
        
        # Set Allure ID and label
        allure.dynamic.id(f"{test_class_name}::{test_method_name}")


@pytest.fixture(scope="session", autouse=True)
def setup_allure_environment():
    """Setup Allure environment information"""
    # allure-pytest 2.13.2 does not expose allure.environment().
    # Environment metadata is written to environment.properties in pytest_configure.
    return None
