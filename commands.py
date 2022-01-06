from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import set_chrome_options
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())

base_url = "https://shop.datasight.app"

#opens the website
def open_website():
    driver.get(base_url)

#goes to the shop inside website
def open_shop():
    shop = driver.find_element_by_link_text("Shop")
    shop.click()

#goes to the beverages catergory inside the shop
def choose_beverages():
    beverages = driver.find_element_by_xpath('//*[@id="main"]/ul/li[3]/a/h2/mark')
    beverages.click()

#picks random drink insde the beverages category
def pick_drink():
    drinks = driver.find_element_by_xpath('//*[@id="main"]')
    all_drinks = drinks.find_elements_by_tag_name("li")
    random_drink = random.choice(all_drinks)
    random_drink.click()


open_website()
open_shop()
choose_beverages()
pick_drink()