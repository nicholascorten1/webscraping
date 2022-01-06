from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import set_chrome_options

driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())

def open_shop():
    try:
        shop = driver.find_element_by_link_text("Shop")
        shop.click()

    except:
        pass
