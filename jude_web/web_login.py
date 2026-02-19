import pytest
from selenium import webdriver
from selenium.common import TimeoutException
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

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Sign In ']"))).click()
    time.sleep(0.5)

    # Open Shops
    wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='#/Shops']"))).click()
    driver.execute_script("window.scrollBy(0, 1200);")
    time.sleep(0.5)

    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AAM Fresh fruite Distributer']"))).click()

    # First Add
    add1 = "(//a[contains(@class,'btn') and contains(., 'Add')])[1]"
    element = wait.until(EC.presence_of_element_located((By.XPATH, add1)))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.3)

    wait.until(EC.element_to_be_clickable((By.XPATH, add1))).click()

    # Popup appears → click Yes
    yes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']")))
    yes_btn.click()

    # Second Add
    add2 = "(//a[contains(@class,'btn') and contains(., 'Add')])[2]"
    element2 = wait.until(EC.presence_of_element_located((By.XPATH, add2)))

    # Scroll second add button into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element2)
    time.sleep(0.3)

    wait.until(EC.element_to_be_clickable((By.XPATH, add2))).click()

    # If popup appears after second Add, click Yes
    try:
        yes_btn = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Yes']"))
        )
        yes_btn.click()
    except TimeoutException:
        # Popup did not appear, continue
        pass

    # Scroll to top and click checkout
    driver.execute_script("window.scrollTo(0, 0);")
    cart_button_xpath = "//button[contains(., 'Go to Checkout')]"
    cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, cart_button_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_button)
    cart_button = wait.until(EC.presence_of_element_located((By.XPATH,"//svg[contains(@class,'feather-shopping-bag')]")))
    cart_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Go to Checkout' or contains(., 'Go to Checkout')]"))).click()