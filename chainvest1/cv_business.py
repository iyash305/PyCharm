import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


   #-----setting up browser----
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options = options)
driver.maximize_window()
wait = WebDriverWait(driver,20)
   #---navigating to login page and logging in---
driver.get("http://192.168.0.3/Chainvest/BO/login")
time.sleep(1)


def login():
    phone_no = driver.find_element(By.ID,"PhoneNo")
    phone_no.send_keys("0922112211")
    password = driver.find_element(By.ID,"Password")
    password.send_keys("P@ssw0rd")
    sign_in = driver.find_element(By.XPATH,"//button[normalize-space()='Sign in']")
    sign_in.click()
    time.sleep(2)

def business_products():
    busi_prod = driver.find_element(By.XPATH,"//span[normalize-space()='Product']")
    busi_prod.click()
    time.sleep(1)
    business_prod = driver.find_element(By.XPATH,"//a[normalize-space()='Business Products']")
    business_prod.click()
    time.sleep(1)
    add_product = driver.find_element(By.XPATH,"//button[normalize-space()='Add Products']")
    add_product.click()
    time.sleep(1)
    sel_category = driver.find_element(By.XPATH,"//select[@formcontrolname='productCategoryID']")
    sel_category = Select(sel_category)
    sel_category.select_by_visible_text("Electronics")

    sel_sub_category = driver.find_element(By.XPATH,"//select[@formcontrolname='productSubCategoryID']")
    sel_sub_category = Select(sel_sub_category)
    sel_sub_category.select_by_visible_text("Laptops")

    search_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Search')]")
    search_btn.click()

    prod = wait.until(EC.presence_of_element_located((By.XPATH,"//button[.//div[contains(text(),'ProBook Laptop')]]")))
    prod.click()

    discount_type = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@formcontrolname='DiscountType']")))
    select_discount_type = Select(discount_type)
    select_discount_type.select_by_visible_text("Fixed")

    discount_price = wait.until(EC.presence_of_element_located((By.XPATH,"//label[normalize-space()='Discount Price']")))
    discount_price.send_keys("250")

    current_stock = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@formcontrolname='CurrentStock']")))
    current_stock.send_keys("20")

    reorder_quantity = driver.find_element(By.XPATH,"//input[@formcontrolname='ReorderLevelQty']")
    reorder_quantity.send_keys("5")

    add_busi_product = driver.find_element(By.XPATH,"//button[contains(text(),'Add Product')]")
    add_busi_product.click()
    time.sleep(2)






login()
business_products()
time.sleep(2)