from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from segments import *
from utils.set_user import create_user


def defined_user(amount_users):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = set_chrome_options())
    """
    list_of_users is a fixed list with a length chosen in amount_of_users (defined in bot.py)
    list_of_users consists of the cookie for every user (created in set_user)
    the last number of every cookie is the segment that user belongs to.
    so the 'if statement' executes the website journey that matches for that type of user
    """
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
