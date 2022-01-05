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

# waiting up to 10 seconds for the driver to find the element that is called "beverages"
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='beverages']"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='View cart']"))
    )
    element.click()
except:
    driver.quit()