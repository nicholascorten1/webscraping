"""
    Bot for browsing shop.datasight.app
"""

from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from utils.set_user import create_user
#from define_user import defined_user
from segments import *

base_url = "https://shop.datasight.app"

amount_users = 2

def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    
    driver.get(base_url)


    ## Set user: 
    user = create_user() 
    driver.delete_cookie('_ga')
    driver.add_cookie({
    'name': '_ga',
    'value': user
    })
    list_of_users = []

    for i in range(amount_users):
        ga_id = create_user()
        list_of_users.append(ga_id)

    for j in range(len(list_of_users)):
        segment_type = eval(list_of_users[j][-1])
        if segment_type == 1:
            single_shopper_bevahiour(driver)

        elif segment_type == 2:
            window_shopper_behaviour(driver)

        elif segment_type == 3:
            researcher_behaviour(driver)

        else:
            loyal_customer_behaviour(driver)



if __name__ == "__main__":
    main() 
