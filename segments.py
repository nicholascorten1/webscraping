from website_touchpoints import *


#single page visitor website journey
def single_shopper_bevahiour(driver):
    open_shop(driver)
    close_website(driver)
  

#window shopper website journey
def window_shopper_behaviour(driver):
    open_shop(driver)
    pick_category(driver)
    pick_item(driver)
    open_shop(driver)
    pick_category(driver)
    pick_item(driver)
    close_website(driver)

#researcher website journey
def researcher_behaviour(driver):
    open_shop(driver)
    pick_category(driver)
    pick_item(driver)
    open_shop(driver)
    pick_category(driver)
    pick_item(driver)
    add_to_cart(driver)
    view_cart(driver)
    proceed_checkout(driver)
    fill_billing_details(driver)
    place_order(driver)
    close_website(driver)

#loyal customers website journey
def loyal_customer_behaviour(driver):
    open_shop(driver)
    pick_category(driver)
    pick_item(driver)
    add_to_cart(driver)
    view_cart(driver)
    proceed_checkout(driver)
    fill_billing_details(driver)
    place_order(driver)
    close_website(driver)



    
   

    
    







  