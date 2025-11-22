import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------
# FIXTURE: creates fresh driver
# -----------------------------
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    yield driver, wait

    driver.quit()


def signin(driver, wait):
    sign_in_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign In']"))
    )
    sign_in_button.click()

'''
def test_valid_login(driver):
    driver, wait = driver

    driver.get("https://automate.we-innovate.co/jude/web/#/")
    signin(driver, wait)

    wait.until(EC.presence_of_element_located((By.ID, "formSigninEmail"))).send_keys("yashjr17@gmail.com")
    wait.until(EC.presence_of_element_located((By.ID, "formSigninPassword"))).send_keys("P@ssw0rd")

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Sign In ']"))
    ).click()

    assert "Home" in driver.page_source

def test_invalid_email_format(driver):
    driver, wait = driver

    driver.get("https://automate.we-innovate.co/jude/web/#/")
    signin(driver, wait)

    wait.until(EC.presence_of_element_located((By.ID, "formSigninEmail"))).send_keys("yash")  # invalid
    wait.until(EC.presence_of_element_located((By.ID, "formSigninPassword"))).send_keys("P@ssw0rd")

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Sign In ']"))
    ).click()

    assert "Invalid email format" in driver.page_source

def test_blank_fields(driver):
    driver, wait = driver
    driver.get("https://automate.we-innovate.co/jude/web/#/")
    signin(driver, wait)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign In')]"))).click()
    assert "Please enter email address" in driver.page_source
    assert "Password required" in driver.page_source
'''
def test_flow(driver):
    driver, wait = driver

    driver.get("https://automate.we-innovate.co/jude/web/#/")
    signin(driver, wait)

    wait.until(EC.presence_of_element_located((By.ID, "formSigninEmail"))).send_keys("yashjr17@gmail.com")
    wait.until(EC.presence_of_element_located((By.ID, "formSigninPassword"))).send_keys("P@ssw0rd")

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Sign In ']"))
    ).click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='#/Shops']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='AAM Fresh fruite Distributer']"))).click()
    add_btn_xpath = "(//a[contains(@class,'btn') and contains(., 'Add')])[1]"

    element = wait.until(
        EC.presence_of_element_located((By.XPATH, add_btn_xpath))
    )

    # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    wait.until(EC.element_to_be_clickable((By.XPATH, add_btn_xpath))).click()
    add_btn_xpath_2 = "(//a[contains(@class,'btn') and contains(., 'Add')])[2]"

    element2 = wait.until(
        EC.presence_of_element_located((By.XPATH, add_btn_xpath_2))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element2)

    wait.until(EC.element_to_be_clickable((By.XPATH, add_btn_xpath_2))).click()

    time.sleep(2)



