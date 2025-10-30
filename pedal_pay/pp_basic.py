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
driver.get("https://automate.we-innovate.co/PedalPay/BO/login")


def login():
    email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
    email_field.send_keys("admin@pp.com")

    password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
    password_field.send_keys("P@ssw0rd")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign in')]"))).click()

def add_shop():
    add_shop_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='Add Shop']")))
    add_shop_btn.click()

    upload_input = wait.until(EC.presence_of_element_located((By.ID, "icon-upload")))
    upload_input.send_keys(r"/Users/mac/Desktop/DAE Work/bb.png")

    shop_name = wait.until(EC.presence_of_element_located((By.ID,"name")))
    shop_name.send_keys("Starbucks")

    shop_desc = wait.until(EC.presence_of_element_located((By.ID,"description")))
    shop_desc.send_keys("Grab a coffee and make your day memorable")

    shop_email = wait.until(EC.presence_of_element_located((By.ID,"email")))
    shop_email.send_keys("yash.indulkar@digital-enterprises.co.in")

    #shop_pass = wait.until(EC.presence_of_element_located((By.ID,"password")))
    #shop_pass.send_keys("Yash@1234")

    open_hours = wait.until(EC.presence_of_element_located((By.ID,"open_hours")))
    open_hours.send_keys("Mon-Sat 9AM - 8PM")

    address = wait.until(EC.presence_of_element_located((By.ID,"address")))
    address.send_keys("Kastanienallee 16")

    shop_land_mark = wait.until(EC.presence_of_element_located((By.ID,"landmark")))
    shop_land_mark.send_keys("Kastanienallee")

    shop_country = wait.until(EC.presence_of_element_located((By.ID, "country")))
    select = Select(shop_country)
    select.select_by_visible_text("Germany")

    state = wait.until(EC.presence_of_element_located((By.ID, "state")))
    select_state = Select(state)
    select_state.select_by_visible_text("Berlin")

    city = wait.until(EC.presence_of_element_located((By.ID,"city")))
    select_city = Select(city)
    select_city.select_by_visible_text("Berlin")

    shop_num = wait.until(EC.presence_of_element_located((By.ID, "number")))
    shop_num.send_keys("9421079522")

    #website = wait.until(EC.presence_of_element_located((By.ID,"website")))
    #website.send_keys("www.ccd.ge")

    #shop_insta = wait.until(EC.presence_of_element_located((By.ID,"instagram")))
    #shop_insta.send_keys("ccd_deu")

    #shop_fb = wait.until(EC.presence_of_element_located((By.ID,"facebook")))
    #shop_fb.send_keys("facebook.com/ccd")

    mon_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeMondayFrom")))
    select= Select(mon_time_from)
    select.select_by_visible_text("8:00 AM")
    mon_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeMondayTo")))
    select=Select(mon_time_to)
    select.select_by_visible_text("10:00 PM")
    tues_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeTuesdayFrom")))
    select= Select(tues_time_from)
    select.select_by_visible_text("8:00 AM")
    tues_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeTuesdayTo")))
    select=Select(tues_time_to)
    select.select_by_visible_text("10:00 PM")
    wed_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeWednesdayFrom")))
    select= Select(wed_time_from)
    select.select_by_visible_text("8:00 AM")
    wed_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeWednesdayTo")))
    select=Select(wed_time_to)
    select.select_by_visible_text("10:00 PM")
    thurs_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeThursdayFrom")))
    select= Select(thurs_time_from)
    select.select_by_visible_text("8:00 AM")
    thurs_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeThursdayTo")))
    select=Select(thurs_time_to)
    select.select_by_visible_text("10:00 PM")
    friday_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeFridayFrom")))
    select= Select(friday_time_from)
    select.select_by_visible_text("8:00 AM")
    friday_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeFridayTo")))
    select=Select(friday_time_to)
    select.select_by_visible_text("10:00 PM")
    sat_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeSaturdayFrom")))
    select= Select(sat_time_from)
    select.select_by_visible_text("8:00 AM")
    sat_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeSaturdayTo")))
    select=Select(sat_time_to)
    select.select_by_visible_text("10:00 PM")
    sun_time_from = wait.until(EC.presence_of_element_located((By.ID,"shopTimeSundayFrom")))
    select= Select(sun_time_from)
    select.select_by_visible_text("8:00 AM")
    sun_time_to = wait.until(EC.presence_of_element_located((By.ID,"shopTimeSundayTo")))
    select=Select(sun_time_to)
    select.select_by_visible_text("10:00 PM")

    active = driver.find_element(By.XPATH,"//input[@formcontrolname = 'isactive']")
    active.click()
    active.click()

    add_shop = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    add_shop.click()
    can = driver.find_element(By.XPATH, "//button[text()='Cancel']")
    can.click()


def rewards():
    shop_module = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()=' Shop Management ']")))
    shop_module.click()

    reward_category_module = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Reward Category']")))
    reward_category_module.click()

#     add_reward_category = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Reward Category']")))
#     add_reward_category.click()
#
# # Upload file
#     reward_upload = driver.find_element(By.ID, "icon-upload")
#     reward_upload.send_keys(r"/Users/mac/Desktop/DAE Work/box.png")
#
# # Reward Category
#     reward_category = driver.find_element(By.XPATH, "//input[@placeholder='Enter Reward Category title']")
#     reward_category.send_keys("Shopping Offers")
#
# # Description
#     reward_description = driver.find_element(By.XPATH, "//input[@placeholder='Enter description']")
#     reward_description.send_keys("Flat 10% discount on selected stores")
#
# # Add button
#     add_btn = driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']")
#     add_btn.click()
#
#     latest_edit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]")))
#     latest_edit_btn.click()
#
#     edit_description = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//input[@placeholder='Enter description']")))
#     edit_description.clear()
#     edit_description.send_keys("Updated: Now 15% discount on all stores")
#
#     save_btn = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[normalize-space(text())='Update']")))
#     save_btn.click()

    rewards_module = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Rewards']")))
    rewards_module.click()

    add_reward = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Reward']")))
    add_reward.click()


    upload_input = wait.until(EC.presence_of_element_located((By.ID, "icon-upload")))
    upload_input.send_keys(r"/Users/mac/Desktop/DAE Work/box.png")

# 2. Reward Category (dropdown)
    reward_category = wait.until(EC.element_to_be_clickable((By.ID, "rewardsCategory_Id")))
    Select(reward_category).select_by_visible_text("Cafés")

# 3. Shop (dropdown)
    shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='shop_id']")))
    Select(shop).select_by_visible_text("Bonanza Coffee Roasters")

# 4. Reward Title
    reward_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Reward Title']")))
    reward_title.send_keys("Free Coffee")


    description = wait.until(EC.visibility_of_element_located((By.ID, "description")))

    description.send_keys("Get a free cappuccino when you spend €5 or more.")


    credit_coins = wait.until(EC.presence_of_element_located((By.ID, "credit_coins")))
    credit_coins.send_keys("150")


    min_spend = wait.until(EC.presence_of_element_located((By.ID, "minimum_spend")))
    min_spend.send_keys("€20")


    valid_from = wait.until(EC.presence_of_element_located((By.ID, "valid_from")))
    valid_from.send_keys("01-10-2025")


    valid_to = wait.until(EC.presence_of_element_located((By.ID, "valid_to")))
    valid_to.send_keys("30-10-2025")


    discount_type = wait.until(EC.presence_of_element_located((By.ID, "discount_type")))
    discount_type.send_keys("Fixed")


    discount_value = wait.until(EC.presence_of_element_located((By.ID, "discount")))
    discount_value.send_keys("5")


    limit_type = wait.until(EC.presence_of_element_located((By.ID, "redemption_limit_type")))
    limit_type.send_keys("PerUser")


    limit_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='redemption_limit']")))
    limit_value.send_keys("1")


    valid_on = wait.until(EC.presence_of_element_located((By.ID, "valid_on")))
    valid_on.send_keys("Weekdays")


    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Add']")))
    add_btn.click()

    # latest_reward_edit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]")))
    # latest_reward_edit_btn.click()
    # reward_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Reward Title']")))
    # reward_title.clear()
    # reward_title.send_keys("Free Espresso")
    # reward_update = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Update']")))
    # reward_update.click()

def country():
    master_module = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Master']")))
    master_module.click()

    country_module = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Country']")))
    country_module.click()

    add_country_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Country']")))
    add_country_btn.click()

    file_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='icon-upload']"))
)

# Send the local file path to the hidden input
    file_input.send_keys(r"C:\Users\manoj\Desktop\SampleImages\swiss.png")

    country_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    country_input.send_keys("Switzerland")

# Description
    desc_input = driver.find_element(By.ID, "description")
    desc_input.send_keys("Country famous for Alps and chocolates")

# Country Code
    code_input = driver.find_element(By.ID, "countrycode")
    code_input.send_keys("41")

# Digit Validate
    digit_validate_input = driver.find_element(By.ID, "digitvalidate")
    digit_validate_input.send_keys("10")

# Currency
    currency_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Currency']")
    currency_input.send_keys("CHF")

# Value Per Credit
    value_input = driver.find_element(By.ID, "valuepercredit")
    value_input.send_keys("10")



# Click Add button
    add_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    add_btn.click()


def challenge():
    time.sleep(2)
    gamification_module = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space(text())='Gamification']")))
    gamification_module.click()

    challenge_module = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Challenge']")))
    challenge_module.click()

    add_challenge_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.), 'Add Challenge')]")))
    add_challenge_btn.click()

    challenge_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='icon-upload']")))
    challenge_icon.send_keys(r"C:\Users\manoj\Desktop\SampleImages\ironman.png")

    challenge_title = wait.until(EC.presence_of_element_located((By.ID, "title")))
    challenge_title.send_keys("Ironman")

    challenge_desc = wait.until(EC.presence_of_element_located((By.ID, "description")))
    challenge_desc.send_keys("The toughest challenge as a Cyclist")

    challenge_from = wait.until(EC.presence_of_element_located((By.ID, "fromdate")))
    challenge_from.send_keys("01-09-2025")

    challenge_to = wait.until(EC.presence_of_element_located((By.ID, "todate")))
    challenge_to.send_keys("30-08-2025")

    credit_get = wait.until(EC.presence_of_element_located((By.ID, "creditgets")))
    credit_get.send_keys("250")

    km_to_drive = wait.until(EC.presence_of_element_located((By.ID, "kmtodrive")))
    km_to_drive.send_keys("100")

    how_it_works = wait.until(EC.presence_of_element_located((By.ID, "howitworks")))
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
                          how_it_works,
                          "Once the challenge is completed, 250 coins will be credited to your account")

    challenge_is_active = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='isactive']"))
    )
    challenge_is_active.click()

    add_challenge = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_challenge.click()

    challenge_edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]")))
    challenge_edit_btn.click()

    update_credit_get = wait.until(EC.presence_of_element_located((By.ID, "creditgets")))
    update_credit_get.clear()
    update_credit_get.send_keys("178")

    update_challenge = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']")))
    update_challenge.click()

def cycling_config():
    time.sleep(2)
    cyc_config_module = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space(text())='Cycling Configurations']")))
    cyc_config_module.click()

    kind_of_cyclist_module = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'kindofcyclist')]"))
    )
    kind_of_cyclist_module.click()

    add_kind_of_cyclist_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Kind Of Cyclist']")))
    add_kind_of_cyclist_btn.click()

    kind_of_cyclist_icon = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='icon-upload']")))
    kind_of_cyclist_icon.send_keys(r"C:\Users\manoj\Desktop\SampleImages\ironman.png")

    kind_of_cyclist_name = wait.until(EC.presence_of_element_located((By.ID,"name")))
    kind_of_cyclist_name.send_keys("Track Cyclist")

    kind_of_cyclist_desc = wait.until(EC.presence_of_element_located((By.ID, "description")))
    driver.execute_script("""
    arguments[0].value = arguments[1];
    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    """, kind_of_cyclist_desc,
                          "Races on a velodrome, a specially designed banked track. These cyclists use bikes with no brakes or gears, built for maximum speed on the smooth surface.")
    add_kind_of_cyclist = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Add']")))
    add_kind_of_cyclist.click()

    kind_of_cyclist_edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", kind_of_cyclist_edit_btn)
    time.sleep(1)
    kind_of_cyclist_edit_btn.click()

    kind_of_cyclist_desc_update = wait.until(EC.presence_of_element_located((By.ID, "description")))
    driver.execute_script("""
       arguments[0].value = arguments[1];
       arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
       arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
       """, kind_of_cyclist_desc_update,
                          "Race on a velodrome, a specially designed banked track. These cyclists use bikes with no brakes or gears, built for maximum speed on the smooth surface.")
    update_kind_of_cyclist = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']")))
    update_kind_of_cyclist.click()

    cycling_frequency = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'cyclingfrequency')]"))
    )
    cycling_frequency.click()

    add_cycling_frequency_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Add Cycling Frequency']")))
    add_cycling_frequency_btn.click()

    cycling_frequency =wait.until(EC.presence_of_element_located((By.ID,"name")))
    cycling_frequency.send_keys("Challenger")

    cycling_desc = wait.until(EC.presence_of_element_located((By.ID,"description")))
    cycling_desc.send_keys("Challenger")

    add_cycling_frequency = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Add']")))
    add_cycling_frequency.click()

    cycling_frequency_edit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space(text())='Edit'])[1]")))
    cycling_frequency_edit_btn.click()
    cycling_desc_update = wait.until(EC.presence_of_element_located((By.ID, "description")))
    cycling_desc_update.clear()
    cycling_desc_update.send_keys("Challenger1")

    update_kind_of_cyclist = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']")))
    update_kind_of_cyclist.click()

    eco_motivation_module = wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space(text())='Eco Motivation']")))
    eco_motivation_module.click()

    add_eco_motivation_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Eco Motivation']")))
    add_eco_motivation_btn.click()

    eco_motivation_upload_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='icon-upload']"))
    )
    eco_motivation_upload_input.send_keys(r"C:\Users\manoj\Desktop\SampleImages\ironman.png")

    eco_motivation_title = wait.until(EC.presence_of_element_located((By.ID,"title")))
    eco_motivation_title.send_keys("Cycle to Work")

    eco_motivation_detail = wait.until(EC.presence_of_element_located((By.ID,"description")))
    driver.execute_script("""
           arguments[0].value = arguments[1];
           arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
           arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
           """, eco_motivation_detail,
                          "Reduce carbon emissions while staying fit.")


    add_eco_motivation = wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add']")))
    add_eco_motivation.click()

    update_eco_motivation = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[normalize-space(text())='Edit'])[1]")))
    update_eco_motivation.click()

    eco_motivation_desc = wait.until(EC.presence_of_element_located((By.ID,"description")))
    driver.execute_script("""
               arguments[0].value = arguments[1];
               arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
               arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
               """, eco_motivation_desc,
                          "Reduce carbon emissions while staying fit.")


    update_eco_motivation_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Update']")))
    update_eco_motivation_btn.click()





login()
add_shop()
# rewards()
#country()
#challenge()
#cycling_config()


time.sleep(8)