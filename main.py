from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()

    #Set options to make browsing easier

    #Remvoes parts of the webpage that may interfere with the scraping
    options.add_argument("disable-infobars")
    #Starts the webpage as maximized --> the page may change shape to adapt to the device
    options.add_argument("start-maximized")
    #Avoid issues that occur when interacting with linux machines
    options.add_argument("disable-dev-shm-usage")
    #Remvoe sandboxes (used for security)
    options.add_argument("no-sandbox")
    ##
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features=AutomationControlled")

    driver = webdriver.Chrome()
    return driver
