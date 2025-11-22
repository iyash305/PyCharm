from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading
import time

URL = "http://192.168.0.3/Chainvest/BO/admin-login"

NUM_USERS = 25 # change to 10, 20, 50, 100 as needed

success_count = 0
failure_count = 0
lock = threading.Lock()

def run_test(user_id):
    global success_count, failure_count

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")   # comment if you want browsers visible
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)

        start_time = time.time()
        driver.get(URL)

        load_time = round(time.time() - start_time, 2)
        print(f"[User {user_id}] Page loaded in {load_time} seconds")

        # -------------------------------------------
        # Optional: Perform login (uncomment & update)
        #
        # driver.find_element(By.ID, "username").send_keys("admin")
        # driver.find_element(By.ID, "password").send_keys("admin123")
        # driver.find_element(By.ID, "loginBtn").click()
        #
        # time.sleep(1)
        #
        # if "dashboard" in driver.current_url.lower():
        #     print(f"[User {user_id}] Login Success")
        # -------------------------------------------

        with lock:
            success_count += 1

        driver.quit()

    except Exception as e:
        print(f"[User {user_id}] Failed → {e}")
        with lock:
            failure_count += 1


def start_stress_test():
    threads = []

    print(f"\n🚀 Starting Stress Test with {NUM_USERS} users...\n")

    for user in range(NUM_USERS):
        t = threading.Thread(target=run_test, args=(user+1,))
        threads.append(t)
        t.start()
        time.sleep(0.05)   # small stagger to avoid instant spike

    for t in threads:
        t.join()

    print("\n===== TEST RESULTS =====")
    print(f"Total Users: {NUM_USERS}")
    print(f"Success: {success_count}")
    print(f"Failed: {failure_count}")
    print("========================\n")


if __name__ == "__main__":
    start_stress_test()
