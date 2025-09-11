import logging
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging
import os

# ---------- Custom Log Folder ----------
log_folder = r"C:\Users\manoj\Desktop\Logs\PedalPayLogs"   # 👈 change path as you like
os.makedirs(log_folder, exist_ok=True)  # create folder if it doesn't exist
log_file = os.path.join(log_folder, "pedal_pay.log")
# ----------------- Logging Config -----------------
logging.basicConfig(
    filename="pedal_pay.log",  # log file will be saved here
    level=logging.INFO,        # DEBUG for extra detail if needed
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# --------------------------------------------------

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("http://code-server-app/PedalPay/BO/login")
logging.info("Opened PedalPay login page")

def login():
    try:
        email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_field.send_keys("yash@gmail.com")
        logging.info("Entered email: yash@gmail.com")

        password_field = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password_field.send_keys("Yash@1234")
        logging.info("Entered password: ********")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Sign in')]"))).click()
        logging.info("Clicked Sign in button")

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Dashboard') or contains(text(),'Shop Management')]")))
        logging.info("Login successful ✅")

    except Exception as e:
        logging.error(f"Login failed ❌ {e}")
        raise

def add_shop():
    try:
        logging.info("Adding shop...")
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='Add Shop']"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "icon-upload"))).send_keys(r"C:\Users\manoj\Desktop\SampleImages\bonanza.png")
        logging.info("Uploaded shop image")

        driver.find_element(By.ID,"name").send_keys("Cafe Coffee Day")
        logging.info("Entered shop name: Cafe Coffee Day")

        driver.find_element(By.ID,"description").send_keys("Grab a coffee and make your day memorable")
        driver.find_element(By.ID,"email").send_keys("ccd@pp.com")
        driver.find_element(By.ID,"password").send_keys("Yash@1234")
        driver.find_element(By.ID,"number").send_keys("8764349912")
        logging.info("Filled shop details")

        driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
        logging.info("Shop submitted successfully ✅")

        driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
        logging.info("Closed shop form")
    except Exception as e:
        logging.error(f"Error while adding shop ❌ {e}")
        raise

def rewards():
    try:
        logging.info("Adding reward category and reward...")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()=' Shop Management ']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Reward Category']"))).click()

        wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space(text())='Add Reward Category']"))).click()
        logging.info("Opened Add Reward Category form")

        driver.find_element(By.ID, "icon-upload").send_keys(r"C:\Users\manoj\Desktop\SampleImages\bonanza.png")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Reward Category title']").send_keys("Shopping Offers")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter description']").send_keys("Flat 10% discount on selected stores")

        driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']").click()
        logging.info("Reward category added successfully ✅")

        # continue for reward addition...
    except Exception as e:
        logging.error(f"Error while handling rewards ❌ {e}")
        raise

def country():
    try:
        logging.info("Adding country...")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Country Management']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space(text())='Add Country']"))).click()

        driver.find_element(By.ID, "icon-upload").send_keys(r"C:\Users\manoj\Desktop\SampleImages\india.png")
        driver.find_element(By.ID, "name").send_keys("India")
        driver.find_element(By.ID, "description").send_keys("Country of diversity")

        driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']").click()
        logging.info("Country added successfully ✅")
    except Exception as e:
        logging.error(f"Error while adding country ❌ {e}")
        raise

def challenge():
    try:
        logging.info("Adding challenge...")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Challenge Management']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space(text())='Add Challenge']"))).click()

        driver.find_element(By.ID, "icon-upload").send_keys(r"C:\Users\manoj\Desktop\SampleImages\challenge.png")
        driver.find_element(By.ID, "title").send_keys("Daily Ride")
        driver.find_element(By.ID, "description").send_keys("Complete 5 km daily")

        driver.find_element(By.XPATH, "//button[normalize-space(text())='Add']").click()
        logging.info("Challenge added successfully ✅")
    except Exception as e:
        logging.error(f"Error while adding challenge ❌ {e}")
        raise

def cycling_config():
    try:
        logging.info("Configuring cycling setup...")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Cycling Config']"))).click()

        driver.find_element(By.ID,"distance").send_keys("10")
        driver.find_element(By.ID,"speed").send_keys("20")
        driver.find_element(By.ID,"time").send_keys("30")
        logging.info("Cycling config details filled")

        driver.find_element(By.XPATH, "//button[normalize-space(text())='Update']").click()
        logging.info("Cycling config updated successfully ✅")
    except Exception as e:
        logging.error(f"Error while configuring cycling setup ❌ {e}")
        raise

# ---------------- Run Workflow ----------------
try:
    login()
    add_shop()
    rewards()
    country()
    challenge()
    cycling_config()
    logging.info("All workflows completed successfully 🎉")
except Exception as main_e:
    logging.error(f"Workflow stopped due to error: {main_e}")

time.sleep(8)
driver.quit()
