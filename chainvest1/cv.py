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
wait = WebDriverWait(driver,10)
   #---navigating to login page and logging in---
driver.get("http://code-server-app/Chainvest/BO/login")

def login():
    email = driver.find_element(By.ID,"Email").send_keys("admin@chainvest.com")
    password = driver.find_element(By.ID,"Password").send_keys("P@ssw0rd")
    sigm_in= driver.find_element(By.XPATH,"//button[normalize-space(text())='Sign in']").click()


def business():

    business_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Business']")))
    business_menu.click()

#business_link = wait.until(
   # EC.element_to_be_clickable((By.XPATH, "//a[@href='/Chainvest/BO/company' and normalize-space(text())='Business']"))
#)
#business_link.click()

    add_busi = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add Business')]")))
    add_busi.click()
    driver.find_element(By.ID,"Name").send_keys("DMart")
    business_type = driver.find_element(By.XPATH,"//select[@id='BusinessTypeID']")
    select = Select(business_type)
    select.select_by_visible_text("Retailer")
    business_category = driver.find_element(By.XPATH,"//input[@role='combobox']")
    business_category.send_keys("Retail")
    time.sleep(0.2)
    option = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Retail']")))
    option.click()
    media = driver.find_element(By.XPATH,"//input[@id='Logo']")
    media.send_keys(r"C:\Users\manoj\Desktop\SampleImages\dmart.png")
    cont_person_name = driver.find_element(By.ID,"ContactPersonName").send_keys("DMart Admin")
    bus_email = driver.find_element(By.ID,"EmailID").send_keys("dmart@sample.com")
    mob_num1 = driver.find_element(By.ID,"MobileNo1").send_keys("99911212111")
    mob_num2 = driver.find_element(By.ID,"MobileNo2").send_keys("9786411087")
    website = driver.find_element(By.ID,"WebsiteURL").send_keys("https://www.dmartindia.com/")
    license_num = driver.find_element(By.ID,"BusinessLicenseNo").send_keys("A12345")
    vat_num = driver.find_element(By.ID,"VAT").send_keys("IE1234567T")
    description = driver.find_element(By.ID,"Description").send_keys("Test description")
    save = driver.find_element(By.XPATH,"//span[normalize-space()='Save & Next']").click()
    time.sleep(0.5)
    doc1_input = wait.until(EC.presence_of_element_located((
    By.XPATH, "//button[normalize-space(text())='Upload Document']")))
    doc1_input.send_keys(r"C:\Users\manoj\Desktop\dmart_sample.jpg")
    doc_save = driver.find_element(By.XPATH,"//button[span[normalize-space()='Save & Next']]").click()
    time.sleep(0.25)
    address1 = driver.find_element(By.XPATH, "//input[@type='text' and @formcontrolname='Address1']")
    address1.send_keys("Bangur Nagar")
    address2 = driver.find_element(By.XPATH,"//input[@type='text' and @formcontrolname='Address2']")
    address2.send_keys("Goregaon West")
    # Select the country
    country = driver.find_element(By.XPATH, "//select[@formcontrolname='CountryID']")
    select_country = Select(country)
    select_country.select_by_visible_text("Ethiopia")

# Now, wait for the 'Addis Ababa' option to be visible in the State dropdown.
# This ensures the option has been loaded after the country selection.
    wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@formcontrolname='StateID']/option[text()='Addis Ababa']")))

# Locate the State dropdown and select the option.
    state = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='StateID']")))
    select_state = Select(state)
    select_state.select_by_visible_text("Addis Ababa")


# Wait for the City dropdown to become clickable after the State selection.
    city_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='CityID']")))
    select_city = Select(city_dropdown)

# Explicitly wait for the "Addis Ababa" option to be present and visible
# within the City dropdown before selecting it.
    wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@formcontrolname='CityID']/option[normalize-space()='Addis Ababa']")))

# Now, select the city.
    select_city.select_by_visible_text("Addis Ababa")
    zip_code = driver.find_element(By.XPATH,"//input[@formcontrolname='Zip']").send_keys("400123")
    land_mark = driver.find_element(By.XPATH,"//input[@formcontrolname='Landmark']").send_keys("Addis")
    lat = driver.find_element(By.XPATH,"//input[@formcontrolname='Latitude']").send_keys("40.12")
    longitude = driver.find_element(By.XPATH,"//input[@formcontrolname='Longitude']").send_keys("35.98")
    save1 = driver.find_element(By.XPATH,"//span[normalize-space()='Save & Next']").click()
    bank_name = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@formcontrolname='BankName']")))
    bank_name.send_keys("HDFC")
    acc_holder = driver.find_element(By.XPATH,"//input[@formcontrolname='AccountHolderName']")
    acc_holder.send_keys("DMart")
    acc_num = driver.find_element(By.XPATH,"//input[@formcontrolname= 'AccountNumber']")
    acc_num.send_keys("2874271980167")
    ifsc = driver.find_element(By.XPATH,"//input[@formcontrolname= 'IFSC']")
    ifsc.send_keys("HDFC00000504")
    branch_name = driver.find_element(By.XPATH,"//input[@formcontrolname= 'BankBranchName']")
    branch_name.send_keys("HDFC Addis")
    finish = driver.find_element(By.XPATH,"//span[normalize-space()='Save & Complete']")
    finish.click()
    time.sleep(1)

def master():
    master = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space() = 'Master']"))).click()
    bus_type = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/Chainvest/BO/business-type']"))).click()
    add_bus_type = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()= 'Add Business Type']"))).click()
    busi_type = driver.find_element(By.XPATH,"//input[@formcontrolname='BusinessTypeName']")
    busi_type.send_keys("Agent")
    busi_desc = driver.find_element(By.XPATH,"//textarea[@formcontrolname='Description']")
    busi_desc.send_keys("Acts on behalf of a company to sell or promote products/services, usually earning a commission.")
    add1 = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()

#lang = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/language']").click()
#ent_lang = driver.find_element(By.ID,"name")
#ent_lang.send_keys("French")
#lang_desc = driver.find_element(By.XPATH,"//textarea[@id='description']")
#lang_desc.send_keys("Français")
#lang_code = driver.find_element(By.XPATH,"//input[@formcontrolname='Languagecode']")
#lang_code.send_keys("FR")
#lc_id = driver.find_element(By.XPATH,"//input[@formcontrolname='LCID']")
#lc_id.send_keys("33")
#add_lang = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()

     #---Roles---

    time.sleep(2)
    role = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/roles']").click()
    role_add = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add Role']").click()
    select_role = driver.find_element(By.XPATH,"//select[@formcontrolname='PrimaryRoleID']")
    select = Select(select_role)
    select.select_by_visible_text("EndUser")
    role1 = driver.find_element(By.XPATH, "//input[@formcontrolname='Name']")
    role1.send_keys("End User")
    role_desc = driver.find_element(By.XPATH,"//textarea[@formcontrolname='Description']")
    role_desc.send_keys("Application User")
    add_role = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()



    payment_type = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/paymentType']").click()
    add_pymnt_type = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add Payment Type']").click()
    pymnt_type = driver.find_element(By.XPATH,"//input[@formcontrolname='PaymentTypeName']")
    pymnt_type.send_keys("QR Code")
    pymnt_desc = driver.find_element(By.XPATH,"//textarea[@formcontrolname='PaymentTypeDescription']")
    pymnt_desc.send_keys("Scan an QR code for faster payment")
    add_pymnt = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()
         #---Payment Status
    payment_status = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/paymentStatus']").click()
    payment_status_button = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add Payment Status']").click()
    enter_payment_status = driver.find_element(By.XPATH,"//input[@formcontrolname='StatusName']")
    enter_payment_status.send_keys("Initiated")
    add_pymnt_button = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()


   #---Order Status---#

    order_status = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/order-status']").click()
    add_order_status = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add Order Status']")
    add_order_status.click()
    enter_order_status = driver.find_element(By.ID,"OrderStatusName")
    enter_order_status.send_keys("Pending")
    enter_order_desc = driver.find_element(By.ID,"OrderStatusDescription")
    enter_order_desc.send_keys("Order has been placed but not yet processed.")
    add_status = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']").click()

def loan():
    loan_module = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Loan Setting']")))
    loan_module.click()

    loan_purpose_module = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/loan-purpose']").click()

    add_loan_purpose_btn = driver.find_element(
        By.XPATH, "//button[normalize-space(text())='Add Loan Purpose']"
    )
    add_loan_purpose_btn.click()
    enter_loan_purpose = driver.find_element(By.ID,"LoanPurposeName")
    enter_loan_purpose.send_keys("Logistics")
    enter_loan_desc = driver.find_element(By.ID,"LoanPurposeDescription")
    enter_loan_desc.send_keys("Fleet expansion or delivery service payments")
    int_from = driver.find_element(By.XPATH,"//input[@formcontrolname='InterestFrom']")
    int_from.send_keys("8")
    int_to = driver.find_element(By.XPATH,"//input[@formcontrolname='InterestTO']")
    int_to.send_keys("20")
    loan_amount_from = driver.find_element(By.ID,"name")
    loan_amount_from.send_keys("200000")
    loan_amount_to = driver.find_element(By.ID,"LoanAmountTO")
    loan_amount_to.send_keys("800000")
    add_loan_purpose = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']")
    add_loan_purpose.click()

    loan_status_module = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/loan-status']").click()
    add_loan_status_btn = driver.find_element(By.XPATH, "//button[normalize-space(text())='Add Loan Status']")
    add_loan_status_btn.click()
    add_loan_status = driver.find_element(By.ID,"LoanStatusName")
    add_loan_status.send_keys("Overdue")
    loan_status_desc = driver.find_element(By.ID,"LoanStatusDescription")
    loan_status_desc.send_keys("Payment is delayed beyond the due date.")
    add_btn = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']")
    add_btn.click()

    #--Credit Score--#
def credit_score():
    credit_score = driver.find_element(By.XPATH, "//span[normalize-space(text())='Credit Score']")
    credit_score.click()
    view_rule = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/credit-score']").click()

    scrollable_module = driver.find_element(By.CLASS_NAME, "overflow-y-scroll")

    time.sleep(2)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_module)
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollTop = 0;", scrollable_module)

    add_rule_button = driver.find_element(By.XPATH,"//button[text()=' Add Rule ']")

    add_rule_button.click()
    time.sleep(2)
    rule_name = driver.find_element(By.XPATH,"//input[@id='RuleName']")
    rule_name.send_keys("Credit Utilization")
    rule_desc = driver.find_element(By.XPATH,"//textarea[@id='Description']")
    rule_desc.send_keys("Credit utilization ratio between 10% and 30%")
    score = driver.find_element(By.ID,"ScoreImpact")
    score.send_keys("10")
    prio = driver.find_element(By.ID,"Priority")
    prio.clear()
    prio.send_keys("4")
    add_rule = driver.find_element(By.XPATH,"//button[normalize-space(text())='Create Rule']")
    add_rule.click()

    view_score = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/Chainvest/BO/credit-scorescreen']"))).click()
    view_score_company = wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()=' InnovatePro Fabrications ']")))
    view_score_company.click()

def view_loan():
    loan = driver.find_element(By.XPATH,"//span[normalize-space(text())='Loan']")
    loan.click()
    view = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='View']")))

    view.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)

def product():
    product = driver.find_element(By.XPATH,"//span[normalize-space()='Product']")
    product.click()
    bulk_upload_click = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/bulk-upload']").click()
    file_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fileInput")))
    file_input.send_keys(r"C:\Users\manoj\Downloads\chainvestupload.xlsx")
    fileupload = driver.find_element(By.XPATH,"//button[normalize-space()='Upload File']")
    fileupload.click()
    product_category = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/product-category']").click()
    add_product_category_btn = driver.find_element(By.XPATH, "//button[normalize-space(text())='Add Product Category']")
    add_product_category_btn.click()
    thumb_img =wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
    thumb_img.send_keys(r"C:\Users\manoj\Downloads\earbuds.jpeg")
    large_input = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
    large_input.send_keys(r"C:\Users\manoj\Downloads\earbuds.jpeg")

    #french1_name = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='product-category-form']//tr[td[text()='French']]//input[@formcontrolname='ProductCategoryShortName']")))

    #french1_name.send_keys("Earbuds")
    #french_desc_1 = driver.find_element(
    #    By.XPATH, "(//tr[td[text()='French']]//input[@placeholder='Enter Description'])[1]"
    #)
    #french_desc_1.send_keys("Earbuds")
    #french2_name = driver.find_element(By.XPATH,"(//tr[td[text()='French']]//input[@formcontrolname='ProductCategoryShortName'])[2]")
    #french2_name.send_keys("Wireless earbuds")

    #french_desc_2 = driver.find_element(
    #    By.XPATH, "(//tr[td[text()='French']]//input[@placeholder='Enter Description'])[2]")
    #french_desc_2.send_keys("Wireless earbuds")

    hindi_name =  driver.find_element(By.XPATH,"//tr[td[text()='Hindi']]//input[@formcontrolname='ProductCategoryShortName']")
    hindi_name.send_keys("Earbuds")

    hindi_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Hindi']]//input[@placeholder='Enter Description']"
    )
    hindi_desc.send_keys("Earbuds")

    afan_name = driver.find_element(
        By.XPATH, "//tr[td[text()='Afan Oromo']]//input[@formcontrolname='ProductCategoryShortName']")
    afan_name.send_keys("Earbuds")
    afan_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Afan Oromo']]//input[@placeholder='Enter Description']"
    )
    afan_desc.send_keys("Earbuds")
    amharic_name = driver.find_element(
        By.XPATH, "//tr[td[text()='Amharic']]//input[@formcontrolname='ProductCategoryShortName']")
    amharic_name.send_keys("Earbuds")
    amharic_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Amharic']]//input[@placeholder='Enter Description']"
    )
    amharic_desc.send_keys("Earbuds")

    #eng_name
    eng_name = driver.find_element(
        By.XPATH, "//tr[td[text()='English']]//input[@formcontrolname='ProductCategoryShortName']")
    eng_name.send_keys("Earbuds")
    eng_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='English']]//input[@placeholder='Enter Description']")
    eng_desc.send_keys("Earbuds")
    #eng_desc
    add = driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

    sub_category = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/Chainvest/BO/product-subcategory']")))
    sub_category.click()

    sub_category_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Add Product SubCategory']")))
    sub_category_btn.click()

    sub_category_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@formcontrolname='ProductCategoryID']")))
    select_sub_category= Select(sub_category_dropdown)
    select_sub_category.select_by_visible_text("Earbuds")
    sub_category_upload = driver.find_element(By.XPATH, "(//input[@type='file'])[1]")
    sub_category_upload.send_keys(r"C:\Users\manoj\Downloads\earbuds.jpeg")

    sub_category_upload1 = driver.find_element(By.XPATH, "(//input[@type='file'])[2]")
    sub_category_upload1.send_keys(r"C:\Users\manoj\Downloads\earbuds.jpeg")
    #french1_name = driver.find_element(By.XPATH,"(//tr[td[text()='French']]//input[@formcontrolname='ProductCategoryShortName'])")
    #french1_name.send_keys(" Wireless Earbuds")
    #french_desc_1 = driver.find_element(
    #    By.XPATH, "(//tr[td[text()='French']]//input[@placeholder='Enter Description'])"
    #)
    #french_desc_1.send_keys("Wireless Earbuds")

    hindi_name =  driver.find_element(By.XPATH,"//tr[td[text()='Hindi']]//input[@formcontrolname='ProductSubCategoryShortName']")
    hindi_name.send_keys("Wireless earbuds")

    hindi_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Hindi']]//input[@placeholder='Enter Description']"
    )
    hindi_desc.send_keys("Wireless earbuds")

    afan_name = driver.find_element(
        By.XPATH, "//tr[td[text()='Afan Oromo']]//input[@formcontrolname='ProductSubCategoryShortName']")
    afan_name.send_keys("Wireless earbuds")
    afan_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Afan Oromo']]//input[@placeholder='Enter Description']"
    )
    afan_desc.send_keys("Wireless earbuds")
    amharic_name = driver.find_element(
        By.XPATH, "//tr[td[text()='Amharic']]//input[@formcontrolname='ProductSubCategoryShortName']")
    amharic_name.send_keys("Wireless earbuds")
    amharic_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='Amharic']]//input[@placeholder='Enter Description']"
    )
    amharic_desc.send_keys("Wireless earbuds")

    #eng_name
    eng_name = driver.find_element(
        By.XPATH, "//tr[td[text()='English']]//input[@formcontrolname='ProductSubCategoryShortName']")
    eng_name.send_keys("Wireless Earbuds")
    eng_desc = driver.find_element(
        By.XPATH, "//tr[td[text()='English']]//input[@placeholder='Enter Description']")
    eng_desc.send_keys("Wireless earbuds")

    add_sub_cat = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    add_sub_cat.click()

#--Orders--#
def orders():
    orders = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Orders']")))
    orders.click()
    view = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='View']")))
    view.click()


#--User Module--#
def user():
    user_module = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Users']")))
    user_module.click()
    new_user_add_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add User']")))
    new_user_add_btn.click()

    company_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@formcontrolname = 'CompanyID']")))
    select_company = Select(company_dropdown)
    select_company.select_by_visible_text("Digital Automation Enterprises")

    enter_email= driver.find_element(By.XPATH,"//input[@formcontrolname = 'Email']")
    enter_email.send_keys("admin@dae.com")

    enter_pass= driver.find_element(By.XPATH,"//input[@formcontrolname = 'PasswordHash']")
    enter_pass.send_keys("P@ssw0rd")

    user_country_dropdown = driver.find_element(By.XPATH,"//select[@formcontrolname = 'CountryID']")
    country_select = Select(user_country_dropdown)
    country_select.select_by_visible_text("Ethiopia")

    enter_phn_num= driver.find_element(By.XPATH,"//input[@formcontrolname = 'Phone']")
    enter_phn_num.send_keys("9874615860")

    role_dropdown = driver.find_element(By.XPATH,"//select[@formcontrolname = 'RoleID']")
    role_select = Select(role_dropdown)
    role_select.select_by_visible_text("Admin")

    add_user = driver.find_element(By.XPATH,"//button[normalize-space(text())='Add']")
    add_user.click()

  #--Reports Module--#
def reports():
    reports_module = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Reports']")))
    reports_module.click()

    order_report = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/Chainvest/BO/fulfillment-report']")))
    order_report.click()
    date_from = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='orderDateFrom']")))
    date_from.send_keys("01-08-2025")
    date_to = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='orderDateTo']")))
    date_to.send_keys("20-08-2025")
    search = driver.find_element(By.XPATH,"//button[normalize-space(text())='Search']")
    search.click()
    time.sleep(2)
    clear_btn = driver.find_element(By.XPATH,"//button[normalize-space(text())='Clear']")
    clear_btn.click()
    bank_reports = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/bankandsupplychain-report']")
    bank_reports.click()
    time.sleep(2)
    financial_reports = driver.find_element(By.XPATH,"//a[@href='/Chainvest/BO/financial-report']")
    financial_reports.click()

time.sleep(3)



login()
 time.sleep(2)

