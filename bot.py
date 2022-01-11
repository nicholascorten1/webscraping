"""
    Bot for browsing shop.datasight.app
"""

from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from segments import single_shopper_bevahiour, window_shopper_behaviour, researcher_behaviour, loyal_customer_behaviour
from utils.set_user import set_user





def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    i = 0
    while(i < 5):

        ## Set user: 
        user = set_user() 
        driver.delete_cookie('_ga')
        driver.add_cookie({
        'name': '_ga',
        'value': user
        })
        loyal_customer_behaviour()
        i = i + 1



if __name__ == "__main__":
    main() 
