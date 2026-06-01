"""
Utility Functions for Screenshots
"""

import os
from datetime import datetime


def take_screenshot(driver, filename=None, directory='reports/screenshots'):
    """Take screenshot and save to file"""
    
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"screenshot_{timestamp}.png"
    
    # Full path for screenshot
    filepath = os.path.join(directory, filename)
    
    # Take screenshot
    driver.save_screenshot(filepath)
    
    return filepath


def take_screenshot_on_failure(driver, test_name):
    """Take screenshot with test name"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{test_name}_{timestamp}.png"
    return take_screenshot(driver, filename)
