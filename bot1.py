from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://shop.datasight.app")

link = driver.find_element_by_link_text("Shop")
link.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT, "Uncategorized"))
    )
    element.click()
except:
    driver.quit()
#driver.quit()