"""
    Bot for browsing shop.datasight.app
"""

from datetime import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from utils.set_user import set_user
from commands import buy_item





def main(): 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    
    ## Set user: 
    user = set_user() 
    driver.delete_cookie('_ga')
    driver.add_cookie({
        'name': '_ga',
        'value': user
    })
    buy_item()
   





if __name__ == "__main__":
    main() 
