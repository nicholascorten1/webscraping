"""
Comment Maarten: 
* Kijk even naar hoe de try/except flow in Python werkt. Over het algemeen "try" je iets in een try en "catch" je een error in een except. Nu heb je driver.quit() staan. Dit zou dus betekenen dat je nooit een driver.quit() hebt. Qu
* probeer alles naar bot.py te verhuizen. Denk aan de code die in de main() functie staat. 
* je overschrijft het object "element" meerdere keren. Dit is voor het overzicht niet zo goed. Je hanteert de juiste naming convention voor "firstname"
* Ik ben zelf niet bekend met de xpath manier van dingen vinden. Het is een beetje trial-and-error. Er zijn dus meerdere maniereen.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options


driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())


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

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Proceed to checkout"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Place order']"))
    )
    element.click()

    """   
        first = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='billing_first_name']"))
    )
    first.send_keys("Sint")
    time.sleep(9) 
    """
except:
    pass


firstname = driver.find_element_by_id("billing_first_name")
firstname.send_keys("Sint")
