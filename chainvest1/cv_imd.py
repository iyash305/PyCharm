import time
from itertools import count
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from datetime import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


# A simple class for logging to an Excel file
class ExcelLogger:
    def __init__(self, filename="automation_logs.xlsx"):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Automation Log"
        self.log_row = 1
        self.setup_headers()

    def setup_headers(self):
        headers = ["Timestamp", "Action", "Log Message"]
        self.sheet.append(headers)

        # Apply formatting to headers
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")

        for cell in self.sheet[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Set column widths for better readability
        self.sheet.column_dimensions['A'].width = 25
        self.sheet.column_dimensions['B'].width = 30
        self.sheet.column_dimensions['C'].width = 80
        self.log_row += 1

    def log(self, action, message, color=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sheet.append([timestamp, action, message])

        # Apply color coding if specified
        if color:
            fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            for cell in self.sheet[self.log_row]:
                cell.fill = fill

        self.log_row += 1

    def save(self):
        self.workbook.save(self.filename)


# Create a folder for screenshots if it doesn't exist
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Initialize the logger with a specific file path
# CHANGE THIS PATH to your desired folder location
log_path = r"C:\Users\manoj\Documents\MyAutomationLogs\automation_logs.xlsx"
logger = ExcelLogger(filename=log_path)

# -----setting up browser----
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)


def take_screenshot(test_case_name):
    """Saves a screenshot with a unique timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"screenshots/{test_case_name}_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    return screenshot_name


# --- Test Case 1: Login ---
try:
    logger.log("Navigation", "Navigating to login page.")
    driver.get("http://code-server-app/Chainvest/BO/login")

    logger.log("Login", "Entering credentials and logging in.")
    email = wait.until(EC.presence_of_element_located((By.ID, "Email")))
    email.send_keys("admin@chainvest.com")
    password = driver.find_element(By.ID, "Password")
    password.send_keys("P@ssw0rd")
    sign_in = driver.find_element(By.XPATH, "//button[normalize-space(text())='Sign in']")
    sign_in.click()

    # Assertion: Verify successful login by checking for a known element on the dashboard
    dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Dashboard']")))
    assert dashboard_element.is_displayed(), "Dashboard element not found after login."
    logger.log("Login", "Login successful!", color="C6EFCE")
except Exception as e:
    screenshot = take_screenshot("login_failure")
    logger.log("Login Failed", f"Login test case failed. Error: {e}. Screenshot: {screenshot}", color="FFC7CE")

# --- Test Case 2: Adding a New Business ---
try:
    logger.log("Add Business", "Starting 'Add Business' test case.")
    business_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Business']")))
    business_menu.click()

    add_busi = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Business')]")))
    add_busi.click()

    logger.log("Fill Business Details", "Filling in business information.")
    wait.until(EC.presence_of_element_located((By.ID, "Name"))).send_keys("DMart")
    business_type = driver.find_element(By.XPATH, "//select[@id='BusinessTypeID']")
    Select(business_type).select_by_visible_text("Retailer")
    business_category = driver.find_element(By.XPATH, "//input[@role='combobox']")
    business_category.send_keys("Retail")
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Retail']")))
    option.click()
    driver.find_element(By.ID, "ContactPersonName").send_keys("DMart Admin")
    driver.find_element(By.ID, "EmailID").send_keys("dmart@sample.com")
    driver.find_element(By.ID, "MobileNo1").send_keys("99911212111")
    driver.find_element(By.ID, "Description").send_keys("Test description")
    driver.find_element(By.XPATH, "//span[normalize-space()='Save & Next']").click()

    # New code to handle the image upload step
    logger.log("Upload Document", "Uploading business document.")
    doc1_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file' and @formcontrolname='DocumentPath']")))
    doc1_input.send_keys(r"C:\Users\manoj\Desktop\SampleImages\dmart.png")  # Using relative path for portability
    doc_save = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[normalize-space()='Save & Next']]")))
    doc_save.click()

    # Assertion: Check if address details page is loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Address Details']")))

    logger.log("Address Details", "Entering address information.")
    address1 = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @formcontrolname='Address1']")))
    address1.send_keys("Bangur Nagar")
    country = driver.find_element(By.XPATH, "//select[@formcontrolname='CountryID']")
    Select(country).select_by_visible_text("Ethiopia")
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//select[@formcontrolname='StateID']/option[normalize-space()='Addis Ababa']")))
    state = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='StateID']")))
    Select(state).select_by_visible_text("Addis Ababa")
    city_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='CityID']")))
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//select[@formcontrolname='CityID']/option[normalize-space()='Addis Ababa']")))
    Select(city_dropdown).select_by_visible_text("Addis Ababa")
    driver.find_element(By.XPATH, "//span[normalize-space()='Save & Next']").click()

    # Assertion: Check if bank details page is loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Bank Details']")))

    logger.log("Bank Details", "Entering bank information.")
    bank_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='BankName']")))
    bank_name.send_keys("HDFC")
    finish = driver.find_element(By.XPATH, "//span[normalize-space()='Save & Complete']")
    finish.click()

    # Assertion: Check for a success message after completing the form
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Business details saved successfully!')]")))
    logger.log("Business", "Business details added successfully!", color="C6EFCE")
except Exception as e:
    screenshot = take_screenshot("add_business_failure")
    logger.log("Add Business Failed", f"Add Business test case failed. Error: {e}. Screenshot: {screenshot}",
               color="FFC7CE")

# --- Test Case 3: Add Master Data - Business Type ---
try:
    logger.log("Master Data", "Starting 'Add Business Type' test case.")
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space() = 'Master']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/Chainvest/BO/business-type']"))).click()

    add_bus_type = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()= 'Add Business Type']")))
    add_bus_type.click()

    busi_type = driver.find_element(By.XPATH, "//input[@formcontrolname='BusinessTypeName']")
    busi_type.send_keys("Agent")
    driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']").click()

    # Assertion: Check for success or list with new item
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[normalize-space()='Agent']")))
    logger.log("Master", "Business Type 'Agent' added successfully.", color="C6EFCE")
except Exception as e:
    screenshot = take_screenshot("add_business_type_failure")
    logger.log("Master Data Failed", f"Adding Business Type failed. Error: {e}. Screenshot: {screenshot}",
               color="FFC7CE")

# --- Test Case 4: Add Product Category ---
try:
    logger.log("Product Category", "Starting 'Add Product Category' test case.")
    product_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Product']")))
    product_menu.click()
    product_category_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/Chainvest/BO/product-category']")))
    product_category_link.click()

    add_product_category_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add Product Category']")))
    add_product_category_btn.click()

    thumb_img = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
    thumb_img.send_keys(r"test_data/earbuds.jpeg")

    languages = [("French", "Earbuds", "Earbuds"), ("English", "Earbuds", "Earbuds")]
    for lang_name, short_name, desc in languages:
        name_xpath = f"//tr[td[normalize-space()='{lang_name}']]//input[@formcontrolname='ProductCategoryShortName']"
        desc_xpath = f"//tr[td[normalize-space()='{lang_name}']]//input[@placeholder='Enter Description']"

        name_field = wait.until(EC.presence_of_element_located((By.XPATH, name_xpath)))
        name_field.send_keys(short_name)
        desc_field = driver.find_element(By.XPATH, desc_xpath)
        desc_field.send_keys(desc)

    add_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    add_btn.click()

    # Assertion: Check if the new category appears in the list
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[normalize-space()='Earbuds']")))
    logger.log("Product", "Product Category added successfully.", color="C6EFCE")
except Exception as e:
    screenshot = take_screenshot("add_product_category_failure")
    logger.log("Product Category Failed", f"Adding Product Category failed. Error: {e}. Screenshot: {screenshot}",
               color="FFC7CE")

# --- Test Case 5: Add a new User ---
try:
    logger.log("Users", "Starting 'Add User' test case.")
    user_module = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space(text())='Users']")))
    user_module.click()
    new_user_add_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='Add User']")))
    new_user_add_btn.click()

    company_dropdown = wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname = 'CompanyID']")))
    Select(company_dropdown).select_by_visible_text("Digital Automation Enterprises")
    driver.find_element(By.XPATH, "//input[@formcontrolname = 'Email']").send_keys("admin@dae.com")
    driver.find_element(By.XPATH, "//input[@formcontrolname = 'PasswordHash']").send_keys("P@ssw0rd")
    user_country_dropdown = driver.find_element(By.XPATH, "//select[@formcontrolname = 'CountryID']")
    Select(user_country_dropdown).select_by_visible_text("Ethiopia")
    driver.find_element(By.XPATH, "//input[@formcontrolname = 'Phone']").send_keys("9874615860")
    role_dropdown = driver.find_element(By.XPATH, "//select[@formcontrolname = 'RoleID']")
    Select(role_dropdown).select_by_visible_text("Admin")
    add_user = driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']")
    add_user.click()

    # Assertion: Check for a success message or that the new user appears in the list
    wait.until(EC.presence_of_element_located((By.XPATH, "//td[normalize-space()='admin@dae.com']")))
    logger.log("Users", "New user added successfully.", color="C6EFCE")
except Exception as e:
    screenshot = take_screenshot("add_user_failure")
    logger.log("Add User Failed", f"Adding a new user failed. Error: {e}. Screenshot: {screenshot}", color="FFC7CE")

# --- Final Actions ---
# Save the log file before closing the browser
logger.save()

# Close the browser at the end
driver.quit()