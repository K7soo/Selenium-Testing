from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd

# LINK TO WEBDRIVER -- SOFTWARE #
# https://sites.google.com/chromium.org/driver/ 

# OPEN GOOGLE CHROME #
service = Service(executable_path="chromedriver.exe")   # PATH
driver = webdriver.Chrome(service=service)              # DRIVER VAR
driver.maximize_window()
driver.get("https://google.com")
# VARIABLES #
method_list = []
description_list = []

# FUNCTIONS
def button_click():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign In')]")))
    button_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]")
    button_element.click()

def driver_wait_function(method, test, type):
    if type = 1:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign In')]")))
    pass

# GO TO SEARCH BAR #
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_variable = driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Web Scraping", Keys.ENTER)

# SEARCH #
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "What is Web Scraping and How to Use It?"))
)
# FIND THE NEAREST STRING RELATED TO SEARCH
link = driver.find_element(By.PARTIAL_LINK_TEXT, "What is Web Scraping and How to Use It?").click()

button_click() # FIND SIGN IN BUTTON

# SIGN IN #
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "luser"))
)
username_input = driver.find_element(By.ID, "luser").send_keys("kcdominb6fu")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
)
password_input = driver.find_element(By.ID, "password").send_keys("Ascens1oN@")
button_element = driver.find_element(By.XPATH, "//*[@id='Login']/button").click()

# FIND SELE TAB #
for attempt in range(3):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='hslider']/li[2]/a"))
        ).click()
        break  # Exit loop if successful
    except StaleElementReferenceException:
        print("Retrying to find and click the Selenium tab due to stale element.")

# SCRAPE THE PAGE #
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='post-427949']/div[3]/table[1]"))
)
table = driver.find_element(By.XPATH, "//*[@id='post-427949']/div[3]/table[1]")

# ROW SCRAPE
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:  # Skip the header row
    columns = row.find_elements(By.TAG_NAME, "td")
    if len(columns) == 2:  
        method = columns[0].text
        description = columns[1].text
        method_list.append(method)
        description_list.append(description)

# DATA FRAME CREATION #
data_frame = pd.DataFrame({
    "Method": method_list,
    "Description": description_list
})

# DISPLAY THE DATA #
print(data_frame)

# INACTIVE TIME BEFORE SLEEP AND QUIT OF TEST #
time.sleep(5)
driver.quit()

# END OF SCRIPT #
