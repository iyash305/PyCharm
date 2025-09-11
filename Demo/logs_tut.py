from stat import filemode

from selenium import webdriver
import logging
import time

from selenium.webdriver.common.by import By



logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename = "test_logs.logs",
    filemode = "w"
)
logger = logging.getLogger()

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="selenium_test.log",
    filemode="w"
)
logger = logging.getLogger()

# Define log_step here 👇
def log_step(description, action):
    """
    Logs success or failure of a Selenium action.
    """
    try:
        logger.info("➡️ %s", description)
        action()
        logger.info("✅ %s - SUCCESS", description)
    except Exception as e:
        logger.error("❌ %s - FAILED: %s", description, e)


#launching chrome
driver = webdriver.Chrome
log_step("Open Google homepage", lambda: driver.get("https://www.google.com/"))
log_step("Find search box", lambda: driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("Selenium logging wrapper"))
log_step("Submit search", lambda: driver.find_element(By.XPATH, "//input[@name='btnK']").submit())

