import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="module")
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
def test_valid_login(setup_browser):
    driver = setup_browser
    username = driver.find_element(By.NAME,"username")
    username.send_keys("Admin")
    password = driver.find_element(By.NAME,"password")
    password.send_keys("admin123")
    login = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    login.click()
