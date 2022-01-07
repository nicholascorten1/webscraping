"""
    Bot for browsing shop.datasight.app
"""

from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from utils.set_user import set_user


base_url = "https://shop.datasight.app"


def main(): 

    
    


    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    response = driver.get(base_url)
    
    ## Set user: 
    user = set_user() 
    driver.delete_cookie('_ga')
    driver.add_cookie({
        'name': '_ga',
        'value': user
    })

    driver.close()


if __name__ == "__main__":
    main() 