from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("http://192.168.0.3/PedalPay/BO/login")


def login():
    email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
    email_field.send_keys("berlinbites@gmail.com")

    password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
    password_field.send_keys("P@ssw0rd")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign in')]"))).click()

def rewards():
    shop_module = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()=' Shop Management ']")))
    shop_module.click()
    time.sleep(1)
    # reward_category_module = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Reward Category']")))
    # reward_category_module.click()

    rewards_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Rewards']")))
    rewards_module.click()

    add_reward = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='Add Reward']")))
    add_reward.click()

    upload_input = wait.until(EC.presence_of_element_located((By.ID, "icon-upload")))
    upload_input.send_keys(r"/Users/mac/Desktop/DAE Work/box.png")

    # 2. Reward Category (dropdown)
    reward_category = wait.until(EC.element_to_be_clickable((By.ID, "rewardsCategory_Id")))
    Select(reward_category).select_by_visible_text("Shopping Offers")

    # 3. Shop (dropdown)
    # shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='shop_id']")))
    # Select(shop).select_by_visible_text("Bonanza Coffee Roasters")

    # 4. Reward Title
    reward_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Reward Title']")))
    reward_title.send_keys("Cashback")

    description = wait.until(EC.visibility_of_element_located((By.ID, "description")))

    description.send_keys("Get one free cappuccino with any order above ₹200")

    credit_coins = wait.until(EC.presence_of_element_located((By.ID, "credit_coins")))
    credit_coins.send_keys("50")

    min_spend = wait.until(EC.presence_of_element_located((By.ID, "minimum_spend")))
    min_spend.send_keys("100")

    valid_from = wait.until(EC.presence_of_element_located((By.ID, "valid_from")))
    valid_from.send_keys("25-08-2025")

    valid_to = wait.until(EC.presence_of_element_located((By.ID, "valid_to")))
    valid_to.send_keys("30-08-2025")

    discount_type = wait.until(EC.presence_of_element_located((By.ID, "discount_type")))
    discount_type.send_keys("Percentage")

    discount_value = wait.until(EC.presence_of_element_located((By.ID, "discount")))
    discount_value.send_keys("10")

    limit_type = wait.until(EC.presence_of_element_located((By.ID, "redemption_limit_type")))
    limit_type.send_keys("PerUser")

    limit_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='redemption_limit']")))
    limit_value.send_keys("1")

    valid_on = wait.until(EC.presence_of_element_located((By.ID, "valid_on")))
    valid_on.send_keys("Weekdays")

    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add']")))
    add_btn.click()

    # latest_reward_edit_btn = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]")))
    # latest_reward_edit_btn.click()
    # reward_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Reward Title']")))
    # reward_title.clear()
    # reward_title.send_keys("Free Espresso")
    # reward_update = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='Update']")))
    # reward_update.click()



login()
rewards()
time.sleep(2)