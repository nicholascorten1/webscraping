"""
    Bot for browsing shop.datasight.app
"""

from datetime import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from segments import single_shopper_bevahiour, window_shopper_behaviour, researcher_behaviour, loyal_customer_behaviour
from utils.set_user import set_user





def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    
    ## Set user: 
    user = set_user() 
    driver.delete_cookie('_ga')
    driver.add_cookie({
        'name': '_ga',
        'value': user
    })
    
    if segment == "single_shopper"
        single_shopper_bevahiour(driver)

    if segment == "window_shopper"
        window_shopper_bevahiour(driver)
    
    if segment == "researcher"
        researcher_bevahiour(driver)
    
    if segment == "loyal_customer"
        loyal_customer_behaviour(driver)


if __name__ == "__main__":
    main() 
