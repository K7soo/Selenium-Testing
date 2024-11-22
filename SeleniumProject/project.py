from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time, pandas as pd

# VARIABLES #
service = Service(executable_path="chromedriver.exe")   # SET CHRM DRVR FILE AS SERVICE
driver = webdriver.Chrome(service=service)              # SET SERVICE VARIABLE TO DRIVER
driver.maximize_window()                                # MAX WINDOW
driver.get("https://google.com")                        # OPENS GOOGLE URL ON BOOT
method_list = []        
description_list = []                 

# FUNCTIONS
def driver_wait_function(method, tag, type):
    if type == 1:   # WAIT UNTIL ELEMENT IS CLICKABLE BY DRIVER
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((method, tag)))
        return element
    if type == 2:   # WAIT UNTIL ELEMENT IS SEEN/LOCATED BY DRIVER
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((method, tag)))
        return element
    
    # GET TABLES
def format_table(format):
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows[1:]:  
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) == 2:  
            method = columns[0].text
            description = columns[1].text
            method_list.append(method)
            description_list.append(description)
    return format

# TEST SCRIPT (LIKE MABL) #

# GO TO SEARCH BAR #
driver_wait_function(By.CLASS_NAME, "gLFyf", 2)
input_variable = driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Web Scraping", Keys.ENTER)

# SEARCH #
driver_wait_function(By.PARTIAL_LINK_TEXT, "What is Web Scraping and How to Use It?", 2)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "What is Web Scraping and How to Use It?").click()

# SIGN IN #
driver_wait_function(By.XPATH, "//a[contains(text(), 'Sign In')]", 1)
button_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]").click()
driver_wait_function(By.ID, "luser", 1)
username_input = driver.find_element(By.ID, "luser").send_keys("kcdominb6fu")
driver_wait_function(By.ID, "password", 1)
password_input = driver.find_element(By.ID, "password").send_keys("SirEst0ngPog1!") # UNO NAMAN SIR OHH!
button_element = driver.find_element(By.XPATH, "//*[@id='Login']/button").click()

# FIND SELENIUM TAB #
for attempt in range(3):
    try:
        selenium_element = driver_wait_function(By.XPATH, "//*[@id='hslider']/li[2]/a", 1)
        selenium_element.click()
        break
    except StaleElementReferenceException:
        print("Retrying to find and click the Selenium tab due to stale element.")

# SCRAPE THE PAGE AND FORMAT DATA #
    # GO TO TABLE TO SCRAPE DATA
driver_wait_function(By.XPATH, "//*[@id='post-427949']/div[3]/table[1]", 2)
table = driver.find_element(By.XPATH, "//*[@id='post-427949']/div[3]/table[1]")
format_table(table)

data_frame = pd.DataFrame({
    "Method": method_list,
    "Description": description_list
})
print(data_frame)

# INACTIVE TIME BEFORE SLEEP AND QUIT OF TEST #
time.sleep(10)
driver.quit()
# END OF SCRIPT #
