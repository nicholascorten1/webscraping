from logging import captureWarnings
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

#generates random names
first_name = names.get_first_name()
last_name = names.get_last_name()

#generates random billing details for the checkout
fake = Faker()
street = fake.street_address()
city = fake.city()
state = fake.street_suffix()
postcode = fake.postcode()
countrycode = fake.country_calling_code()
phone = fake.msisdn()


def buy_item():
#opens the website
    driver.get(base_url)

#maximises the chrome window
    driver.maximize_window()

#goes to the shop inside website
    shop = driver.find_element_by_link_text("Shop")
    shop.click()

#goes to the beverages catergory inside the shop
    categories = driver.find_element_by_xpath('//*[@id="main"]')
    all_categories = categories.find_elements_by_tag_name("li")
    random_category = random.choice(all_categories)
    random_category.click()

#picks item inside the chosen category
    items = driver.find_element_by_xpath('//*[@id="main"]')
    all_items = items.find_elements_by_tag_name("li")
    random_item = random.choice(all_items)
    random_item.click()
    
#adds product to cart
    add_cart = driver.find_element_by_name('add-to-cart')
    add_cart.click()

#views cart
    view_cart = driver.find_element_by_link_text('View cart')
    view_cart.click()
    
#proceeds to checkout
    checkout = driver.find_element_by_link_text('Proceed to checkout')
    checkout.click()

#fill in first name
    fill_name = driver.find_element_by_xpath('//*[@id="billing_first_name"]')
    fill_name.send_keys(first_name)

#fill in last name
    fill_last_name = driver.find_element_by_xpath('//*[@id="billing_last_name"]')
    fill_last_name.send_keys(last_name)

#picks country from dropdown list
    dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_country_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_countries = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    all_countries.send_keys("United States", Keys.RETURN)

#fills in the random street address generated above
    address_street = driver.find_element_by_xpath('//*[@id="billing_address_1"]')
    address_street.send_keys(street)

#fills in the random city generated above
    address_city = driver.find_element_by_xpath('//*[@id="billing_city"]')
    address_city.send_keys(city)

#picks random state
    dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_state_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_states = driver.find_elements_by_tag_name("li")
    random_state = random.choice(all_states)
    random_state.click()

#fills in the random postal code generated above
    postal_code = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
    postal_code.send_keys(postcode)

#fills in the random phone number generated above
    phone_number = driver.find_element_by_xpath('//*[@id="billing_phone"]')
    phone_number.send_keys(countrycode + phone)

#fills in the random email address from first name & last name
    phone_number = driver.find_element_by_xpath('//*[@id="billing_email"]')
    phone_number.send_keys(first_name + last_name + "@gmail.com")

#places the order
    order = driver.find_element_by_xpath('//*[@id="place_order"]')
    order.click()


buy_item()




