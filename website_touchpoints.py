from selenium.webdriver.common.keys import Keys
import random
import names
from faker import Faker

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




#close the website
def close_website(driver):
    driver.quit()

#goes to the shop inside website
def open_shop(driver):
    shop = driver.find_element_by_link_text("Shop")
    shop.click()

#picks a category inside the shop
def pick_category(driver):
    categories = driver.find_element_by_xpath('//*[@id="main"]')
    all_categories = categories.find_elements_by_tag_name("li")
    random_category = random.choice(all_categories)
    random_category.click()

#picks item inside the chosen category
def pick_item(driver):
    items = driver.find_element_by_xpath('//*[@id="main"]')
    all_items = items.find_elements_by_tag_name("li")
    random_item = random.choice(all_items)
    random_item.click()
    
#adds product to cart
def add_to_cart(driver):
    add_cart = driver.find_element_by_name('add-to-cart')
    add_cart.click()

#pick random amount of this product
def pick_amount(driver):
    random_amount = random.randint(1,7)
    amount = driver.find_element_by_xpath('//*[@id="quantity_61d71827d036c"]')
    amount.clear()
    amount.send_keys(random_amount)

#views cart
def view_cart(driver):
    view_cart = driver.find_element_by_link_text("View cart")
    view_cart.click()
    
#proceeds to checkout
def proceed_checkout(driver):
    checkout = driver.find_element_by_link_text('Proceed to checkout')
    checkout.click()

#fill in billing details
def fill_billing_details(driver):
    fill_name = driver.find_element_by_xpath('//*[@id="billing_first_name"]')
    fill_name.send_keys(first_name)

#fill in last name
    fill_last_name = driver.find_element_by_xpath('//*[@id="billing_last_name"]')
    fill_last_name.send_keys(last_name)

#picks country from dropdown list
    dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_country_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_countries = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    all_countries.send_keys("Netherlands", Keys.RETURN)
  
#fills in the random street address generated above
    address_street = driver.find_element_by_xpath('//*[@id="billing_address_1"]')
    address_street.send_keys(street)

#fills in the random postal code generated above
    postal_code = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
    postal_code.send_keys(postcode)

#fills in the random city generated above
    address_city = driver.find_element_by_xpath('//*[@id="billing_city"]')
    address_city.send_keys(city)

#picks random state
    '''dropdown_arrow = driver.find_element_by_xpath('//*[@id="billing_state_field"]/span/span/span[1]/span/span[2]/b')
    dropdown_arrow.click()
    all_states = driver.find_elements_by_tag_name("li")
    random_state = random.choice(all_states)
    random_state.click()'''

#fills in the random phone number generated above
    phone_number = driver.find_element_by_xpath('//*[@id="billing_phone"]')
    phone_number.send_keys(countrycode + phone)

#fills in the random email address from first name & last name
    phone_number = driver.find_element_by_xpath('//*[@id="billing_email"]')
    phone_number.send_keys(first_name + last_name + "@gmail.com")

#places the order
def place_order(driver):
    order = driver.find_element_by_xpath('//*[@id="place_order"]')
    order.click()