from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#data is being extracted from https://automated.pythonanywhere.com/

path_to_chromedriver = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\GabTheFolder\\Python projects\\PYTHON-AUTOMATION-PROJECTS\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path_to_chromedriver)



def get_driver():
    optionsForSearch = webdriver.ChromeOptions()

    #Set options to make browsing easier

    #Remvoes parts of the webpage that may interfere with the scraping
    optionsForSearch.add_argument("disable-infobars")
    
    #Starts the webpage as maximized --> the page may change shape to adapt to the device
    optionsForSearch.add_argument("start-maximized")
     
    #Remvoe sandboxes (used for security)
    optionsForSearch.add_argument("no-sandbox")
    
    
    optionsForSearch.add_experimental_option("excludeSwitches", ["enable-automation"])
    optionsForSearch.add_argument("disable-blank-features=AutomationControlled")
    
    #fixes the problem of the tab immediately closing after the code execution
    optionsForSearch.add_experimental_option("detach", True)

    
    driver = webdriver.Chrome(service=service, options=optionsForSearch)       #add the service attribute to fix the IDE problem

    URL = "https://automated.pythonanywhere.com/"   #Connects driver to webpage, just enter the URL
    driver.get(URL)

    return driver

#For the xpath, ommit the /text() at the end
def main():
    driver = get_driver()
    #This delay allows the program to retrieve the dynamic data, and not only the static one
    time.sleep(2)
    element = driver.find_element(by="xpath", 
                                  value="/html/body/div[1]/div/h1[2]")
    return element.text

print(main())
