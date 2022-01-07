"""
    Bot for browsing shop.datasight.app
"""



"""
Comments:
* Ik vind de naam commands.py niet echt logisch. Het gaat meer om het invullen van een formulier 
* In plaats van allerlei functies in bot.py te importeren, kun je ook een soort kapstok-functie maken in commands.py waarin je alles samenvoegt. Vervolgens kun je deze functie hier importeren. 
* je haalt twee keer de driver aan. in bot.py en in commands.py. Een keer is genoeg. je kan de driver als parameter in de kapstok functie beschrikbaar maken aan alle functies in commands.py. 
* Kijk naar de juiste manier van functies van documentatie voorzien. je kan de vscode extension "Python Docstring Generator" downloaden. Die kan je helpen. 
* In commands.py --> verwijder lines 123-148
* het is netter om in commands.py line 82 tot 89 in de functies zelf te verwerken
"""
from datetime import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

from config import set_chrome_options
from utils.set_user import set_user
from commands import open_website, open_shop, choose_beverages, pick_drink, add_to_cart, view_cart, proceed_checkout, fill_firstname, fill_lastname, pick_country, fill_street_address, fill_city, fill_state, fill_postcode, fill_phonenumber, fill_email



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
    

    driver.close()


if __name__ == "__main__":
    main() 
