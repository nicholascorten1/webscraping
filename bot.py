"""
    Bot for browsing shop.datasight.app
"""

from datetime import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from utils.set_user import set_user
from commands import open_website, open_shop, choose_beverages, pick_drink, add_to_cart, view_cart, proceed_checkout, fill_firstname, fill_lastname, pick_country, fill_street_address, fill_city, fill_state, fill_postcode, fill_phonenumber, fill_email, place_order





def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    
    ## Set user: 
    user = set_user() 
    driver.delete_cookie('_ga')
    driver.add_cookie({
        'name': '_ga',
        'value': user
    })
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
    fill_state()
    fill_postcode()
    fill_phonenumber()
    fill_email() 
    fill_phonenumber()
    fill_email()
    place_order()
    time.sleep(10)
   



    driver.close()


if __name__ == "__main__":
    main() 
