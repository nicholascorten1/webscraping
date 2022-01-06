from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import set_chrome_options
import time
import random
import names
from faker import Faker

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
    
#adds product to cart
def add_to_cart():
    add_cart = driver.find_element_by_name('add-to-cart')
    add_cart.click()

#pick random amount of this product
def pick_amount():
    random_amount = random.randint(1,7)
    amount = driver.find_element_by_xpath('//*[@id="quantity_61d71827d036c"]')
    amount.clear()
    amount.send_keys(random_amount)

#views cart
def view_cart():
    view_cart = driver.find_element_by_link_text('View cart')
    view_cart.click()
    
#proceeds to checkout
def proceed_checkout():
    checkout = driver.find_element_by_link_text('Proceed to checkout')
    checkout.click()

#fill in first name
first_name = names.get_first_name()
def fill_firstname():
    fill_name = driver.find_element_by_xpath('//*[@id="billing_first_name"]')
    fill_name.send_keys(first_name)

#fill in last name
last_name = names.get_last_name()
def fill_lastname():
    fill_last_name = driver.find_element_by_xpath('//*[@id="billing_last_name"]')
    fill_last_name.send_keys(last_name)

#picks country from dropdown list
def pick_country():
    dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_country_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_countries = driver.find_elements_by_tag_name("li")
    random_country = random.choice(all_countries)
    random_country.click()

#fills in a random address
fake = Faker()
address = fake.address().split('\n', 1)[0]
def fill_address():
    address_line = driver.find_element_by_xpath('//*[@id="billing_address_1"]')
    address_line.send_keys(address)


#ik wil graag deze functies in de bot.py plaatsen maar momenteel krijg ik error wnr ik ze daar run
#daarom plaats ik ze tijdelijk hier, zodat ik de functies zelf kan testen
open_website()
open_shop()
choose_beverages()
pick_drink()
add_to_cart()
view_cart()
proceed_checkout()
fill_firstname()
fill_lastname()
pick_country()
fill_address()