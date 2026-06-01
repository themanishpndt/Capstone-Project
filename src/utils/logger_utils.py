"""
Utility Functions for Logging
"""

import logging
import os
from datetime import datetime


def setup_logger(name, log_file='reports/logs/test.log', level=logging.INFO):
    """Setup logger with file and console handlers"""
    
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


def log_test_start(logger, test_name):
    """Log test start"""
    logger.info("=" * 80)
    logger.info(f"TEST START: {test_name}")
    logger.info(f"Timestamp: {datetime.now()}")
    logger.info("=" * 80)


def log_test_end(logger, test_name, status):
    """Log test end"""
    logger.info("=" * 80)
    logger.info(f"TEST END: {test_name} - {status}")
    logger.info(f"Timestamp: {datetime.now()}")
    logger.info("=" * 80)
