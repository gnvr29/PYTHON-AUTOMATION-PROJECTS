from selenium import webdriver

def get_driver():
    optionsForSearch = webdriver.ChromeOptions()

    #Set options to make browsing easier

    #Remvoes parts of the webpage that may interfere with the scraping
    optionsForSearch.add_argument("disable-infobars")
    #Starts the webpage as maximized --> the page may change shape to adapt to the device
    optionsForSearch.add_argument("start-maximized")
    #Avoid issues that occur when interacting with linux machines
    optionsForSearch.add_argument("disable-dev-shm-usage")
    #Remvoe sandboxes (used for security)
    optionsForSearch.add_argument("no-sandbox")
    ##
    optionsForSearch.add_experimental_option("excludeSwitches", ["enable-automation"])
    optionsForSearch.add_argument("disable-blank-features=AutomationControlled")

    driver = webdriver.Chrome(options=optionsForSearch)
    #Connects driver to webpage, just enter the URL
    driver.get("https://automated.pythonanywhere.com/")

    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by= "xpath", value="/html/body/div[1]/div/h1[1]/text()")
    return element.text

print(main)