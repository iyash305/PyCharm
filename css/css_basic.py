from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.expected_conditions import element_to_be_selected, element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#launch chrome
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
#go to url
driver.get("http://code-server-app/CSS/LoginPage.aspx?")
time.sleep(2)

#locate username
user_name= wait.until(EC.presence_of_element_located((By.NAME, "txtUsername")))
#enter username
user_name.send_keys("admin")


#locate password
password = wait.until(EC.presence_of_element_located((By.ID, "txtPassword")))
#enter password
password.send_keys('admin')


#login button
login = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
login.click()


time.sleep(2)

#three_line = driver.find_element(By.CLASS_NAME,"mdi")
#three_line.click()

#region
region = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/CSS/Region.aspx']")))
region.click()


#add region button
region_button = wait.until(EC.element_to_be_clickable((By.ID, "btnAddRegion")))
region_button.click()
time.sleep(1)


#region_details
region_details = driver.find_element(By.ID, "MRegion")
region_name = region_details.send_keys("Jammu")


#description
description = driver.find_element(By.ID, "MDescription")
description.send_keys("Test Description")
time.sleep(2)

checkbox = driver.find_element(By.ID,"MisActive")
if not checkbox.is_selected():
    checkbox.click()

time.sleep(2)


#save
save = driver.find_element(By.ID,"ContentPlaceHolder1_btnSave")
save.click()
time.sleep(2)
print(f"Added region is: {region_name}")

#edit

last_edit = wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'mdi-square-edit-outline')])[1]")))
last_edit.click()
#edit_region:
edit_region = wait.until(EC.visibility_of_element_located((By.ID, "MRegion")))
edit_region.clear()
edit_region.send_keys("Jammu & Kashmir")

save1 = driver.find_element(By.ID,"ContentPlaceHolder1_btnSave")
save1.click()


time.sleep(2)
"""
#last delete
delete_last = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//i[contains(@class,'mdi-delete')])[last()]")
    )
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_last)
time.sleep(0.5)
delete_last.click()

confirm_delete = wait.until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_btnDeleteContinue")))
confirm_delete.click()
time.sleep(1)
"""
#branch
branch = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/CSS/Branch.aspx']")))
branch.click()
time.sleep(1)

#add_branch
add_branch = wait.until(EC.presence_of_element_located((By.ID,"btnAddBranch")))
add_branch.click()
time.sleep(1)
select_region = Select(driver.find_element(By.ID, "ddlRegion"))
select_region.select_by_visible_text("Vidarbha")
branch_name=wait.until(EC.presence_of_element_located((By.ID,"txtBranchName")))
branch_name.send_keys("Inox")
city = wait.until(EC.presence_of_element_located((By.ID,"txtCityName")))
city.send_keys("Mumbai")
size = wait.until(EC.presence_of_element_located((By.ID,"RBBySize")))
size.click()

enter_size= wait.until(EC.presence_of_element_located((By.ID,"txtBySize")))
enter_size.send_keys("2")

is_active = wait.until(EC.presence_of_element_located((By.ID,"ChkIsActive")))
is_active.click()

save1 = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_btnSave")))
save1.click()
time.sleep(1)

ftp = wait.until(EC.presence_of_element_located((By.XPATH,"(//i[contains(@class, 'mdi-server')])[3]")))
ftp.click()
time.sleep(1)

ftp_username = wait.until(EC.presence_of_element_located((By.ID,"txtusername")))
ftp_username.clear()
ftp_username.send_keys("dae123")

server_name = wait.until(EC.presence_of_element_located((By.ID,"txtservername")))
server_name.clear()
server_name.send_keys("code-server-app")

server_password = wait.until(EC.presence_of_element_located((By.ID,"txtpassword")))
server_password.clear()
server_password.send_keys("P@ssw0rd786")

database_name = wait.until(EC.presence_of_element_located((By.NAME, "ctl00$ContentPlaceHolder1$txtdatabasename")))
database_name.clear()
database_name.send_keys("code-server-app")
time.sleep(0.5)

central_ftp =wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_centeralcheck")))
central_ftp.click()

ftp_server_name = wait.until(EC.presence_of_element_located((By.NAME,"ctl00$ContentPlaceHolder1$txtcenterftpname")))
ftp_server_name.clear()
ftp_server_name.send_keys("DAE")

ftp_username1 = wait.until(EC.presence_of_element_located((By.ID,"txtcenteruser")))
ftp_username1.clear()
ftp_username1.send_keys("dae123")

ftp_password = wait.until(EC.presence_of_element_located((By.ID,"txtcenterpassword")))
ftp_password.clear()
ftp_password.send_keys("P@ssw0rd786")

add_ftp = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_Add")))
add_ftp.click()
time.sleep(2)

#Media
media = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/CSS/Media.aspx']")))
media.click()
time.sleep(0.5)
media_button = wait.until(EC.presence_of_element_located((By.ID,"exampleModal")))
media_button.click()
file_name = wait.until(EC.presence_of_element_located((By.ID,"FileUpload1"))).send_keys("E:\\Jude\\reebok.jpeg")
time.sleep(0.5)
caption = wait.until(EC.presence_of_element_located((By.ID,"Caption"))).send_keys("Wallpaper")
duration = wait.until(EC.presence_of_element_located((By.ID,"txtDuration"))).send_keys("10")
strt_date = wait.until(EC.presence_of_element_located((By.ID,"txtStartDate"))).send_keys(("08-08-2025"))
end_date = wait.until(EC.presence_of_element_located((By.ID,"TxtEndDate"))).send_keys(("12-08-2025"))
is_act = wait.until(EC.presence_of_element_located((By.ID,"ChkIsActive")))
if not is_act.is_selected():
    is_act.click()
media_save= wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_Button1"))).click()
time.sleep(5)


#Playlist
play_list = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/CSS/Playlist.aspx']")))
play_list.click()
time.sleep(2)

# Locate the eye icon using XPath
eye_symbol = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//i[contains(@class, 'mdi-eye')])[1]"))
)
eye_symbol.click()
time.sleep(2)
action = ActionChains(driver)
drag = wait.until(EC.presence_of_element_located((By.ID,"media_135")))
drop= wait.until(EC.presence_of_element_located((By.ID,"dropzone")))
drag1 = wait.until(EC.presence_of_element_located((By.ID,"media_136")))
drop1= wait.until(EC.presence_of_element_located((By.ID,"dropzone")))
action.drag_and_drop(drag,drop).perform()
action.drag_and_drop(drag1,drop1).perform()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 200);")
add_slot = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_btnOpenSlotAdd")))
add_slot.click()
slot_name = wait.until(EC.visibility_of_element_located((By.ID,"slotname")))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", slot_name)
slot_name.send_keys("Temporary")
strt_time = wait.until(EC.presence_of_element_located((By.ID,"txtStartDateslot"))).send_keys("12.45")
end_time = wait.until(EC.presence_of_element_located((By.ID,"txtEndDateslot"))).send_keys("14.45")
slot_active = wait.until(EC.presence_of_element_located((By.ID,"CheckBox")))
if not slot_active.is_selected():
    slot_active.click()
add = wait.until(EC.presence_of_element_located((By.ID,"addslot")))
add.click()
time.sleep(2)
close = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_clear")))
close.click()
time.sleep(5)

#Screen
screen = wait.until(EC.presence_of_element_located((By.XPATH,"//i[@class='mdi mdi-monitor']")))
screen.click()
time.sleep(2)
#add screen
add_screen = wait.until(EC.presence_of_element_located((By.ID,"btnAddScreen")))
add_screen.click()
time.sleep(0.8)
screen_name = wait.until(EC.presence_of_element_located((By.ID,"txtScreen")))
screen_name.clear()
screen_name.send_keys("Screen 151")
time.sleep(1.5)

play_list = Select(wait.until(EC.element_to_be_clickable((By.ID,"ddlPlaylist"))))
play_list.select_by_visible_text("Boisar")

screen_branch_name = Select(wait.until(EC.element_to_be_clickable((By.ID,"ddlBranchlist"))))
screen_branch_name.select_by_visible_text("Growels 101")

screen_save = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_Button1")))
screen_save.click()
time.sleep(2)

#ticker
ticker_select =wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/CSS/TickerMaster.aspx']")))
ticker_select.click()
time.sleep(0.5)
#addtickerbutton
add_ticker_button = wait.until(EC.presence_of_element_located((By.ID,"btnAddPlaylist")))
add_ticker_button.click()
time.sleep(0.5)
ticker_tag = wait.until(EC.presence_of_element_located((By.ID,"txttickertag")))
ticker_tag.send_keys("Ticker Infiniti")
ticker_text = wait.until(EC.presence_of_element_located((By.ID,"txttickertext")))
ticker_text.send_keys("WELCOME TO INFINITI  ")

font_name = Select(wait.until(EC.presence_of_element_located((By.ID,"ddlFontName"))))
font_name.select_by_visible_text("Calibri")

font_size = wait.until(EC.presence_of_element_located((By.ID,"txtFontName")))
font_size.send_keys("2")
font_speed = wait.until(EC.presence_of_element_located((By.ID,"txtSpeed")))
font_speed.send_keys("2")

direction = wait.until(EC.presence_of_element_located((By.ID,"RdoRTL")))
if not direction.is_selected():
    direction.click()

ticker_active = wait.until(EC.presence_of_element_located((By.ID,"ChkIsActive")))
if not ticker_active.is_selected():
    ticker_active.click()

ticker_save = wait.until(EC.presence_of_element_located((By.ID,"ContentPlaceHolder1_btnSave")))
ticker_save.click()
time.sleep(1)





#profile
profile= driver.find_element(By.XPATH, "//a[@role='button' and @data-bs-toggle='dropdown' and contains(@class, 'nav-user')]")
profile.click()
time.sleep(1)

#logout
logout= driver.find_element(By.XPATH, "//a[@href='?action=logout']")
logout.click()
time.sleep(2)

alert = driver.switch_to.alert


# Click "OK" (Yes)
alert.accept()