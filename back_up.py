from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    all_countries = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    all_countries.send_keys("United States", Keys.RETURN)
  

#generates random billing details for the checkout
fake = Faker()
street = fake.street_address()
city = fake.city()
state = fake.street_suffix()
postcode = fake.postcode()
countrycode = fake.country_calling_code()
phone = fake.msisdn()

#fills in the random street address generated above
def fill_street_address():
    address_street = driver.find_element_by_xpath('//*[@id="billing_address_1"]')
    address_street.send_keys(street)

#fills in the random city generated above
def fill_city():
    address_city = driver.find_element_by_xpath('//*[@id="billing_city"]')
    address_city.send_keys(city)

#picks random state
def pick_state():
    dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_state_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_states = driver.find_elements_by_tag_name("li")
    random_state = random.choice(all_states)
    random_state.click()

#fills in the random postal code generated above
def fill_postcode():
    postal_code = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
    postal_code.send_keys(postcode)

#fills in the random phone number generated above
def fill_phonenumber():
    phone_number = driver.find_element_by_xpath('//*[@id="billing_phone"]')
    phone_number.send_keys(countrycode + phone)

#fills in the random email address from first name & last name
def fill_email():
    phone_number = driver.find_element_by_xpath('//*[@id="billing_email"]')
    phone_number.send_keys(first_name + last_name + "@gmail.com")

#places the order
def place_order():
    order = driver.find_element_by_xpath('//*[@id="place_order"]')
    order.click()



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
fill_street_address()
fill_city()
pick_state()
fill_postcode()
fill_phonenumber()
fill_email()
place_order()