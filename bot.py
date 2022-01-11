"""
    Bot for browsing shop.datasight.app
"""

from datetime import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from uninvolved_shoppers import uninvolved_userflow
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

    uninvolved_userflow()
    

   





if __name__ == "__main__":
    main() 
