import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/rukes/AutoCheckout/chromedriver')

#6900xt page
browser.get('https://www.amd.com/en/direct-buy/5458372200/us')
browser.execute_script("window.open('about:blank');")
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.amd.com/en/direct-buy/5458372800/us')
browser.execute_script("window.open('about:blank');")
browser.switch_to.window(browser.window_handles[2])
browser.get('https://www.amd.com/en/direct-buy/5496921500/us')

#6800xt page

buyButton = False

while not buyButton:
    time.sleep(2)
    try:
        browser.switch_to.window(browser.window_handles[0])
        #If this works then the button is not pytopen
        addToCartBtn = addButton = browser.find_element_by_class_name("product-out-of-stock")


        #Button isn't ready restart the script
        print("Button isnt ready yet.")
        #refresh page
        browser.refresh()

    except:
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        try:
            addToCartBtn = addButton = browser.find_element_by_class_name("btn-shopping-cart btn-shopping-neutral use-ajax")
            print("Button for 6900xt was clicked.")
            addToCartBtn.click()
            buyButton = True

        except:
            print("Failed to add to cart")
        

    try:
        browser.switch_to.window(browser.window_handles[1])
        #If this works then the button is not pytopen
        addToCartBtn2 = addButton = browser.find_element_by_class_name("product-out-of-stock")


        #Button isn't ready restart the script
        print("Button isnt ready yet.")
        #refresh page
        browser.refresh()

    except:
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        try:
            addToCartBtn2 = addButton = browser.find_element_by_class_name("btn-shopping-cart btn-shopping-neutral use-ajax")
            print("Button for 6800xt was clicked.")
            addToCartBtn2.click()
            buyButton = True
        except:
            print("Failed to add to cart")

    try:
        browser.switch_to.window(browser.window_handles[2])
        #If this works then the button is not pytopen
        addToCartBtn2 = addButton = browser.find_element_by_class_name("product-out-of-stock")


        #Button isn't ready restart the script
        print("Button isnt ready yet.")
        #refresh page
        browser.refresh()

    except:
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        try:
            addToCartBtn2 = addButton = browser.find_element_by_class_name("btn-shopping-cart btn-shopping-neutral use-ajax")
            print("Button for 6800xt midnight was clicked.")
            addToCartBtn2.click()
            buyButton = True
        except:
            print("Failed to add to cart")

input("Enter any key to quit.") 
