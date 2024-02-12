from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path_to_chromedriver = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\GabTheFolder\\Python projects\\PYTHON-AUTOMATION-PROJECTS\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path_to_chromedriver)



def get_driver(url):
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

   #Connects driver to webpage, just enter the URL
    driver.get(url)

    return driver

def clean_text(text):
    '''Filters and extracts only the temperature (the dynamic data) from the webpage'''
    output = int(text.split(": ")[1])
    return output


def main():
        driver = get_driver("https://automated.pythonanywhere.com/login/")
        driver.find_element(by="id",
                            value="id_username").send_keys("automated")
        time.sleep(2)
        driver.find_element(by="id",
                            value="id_password").send_keys("automatedautomated" + Keys.RETURN)
        time.sleep(2)
        driver.find_element(by="xpath",
                            value="/html/body/nav/div/a").click()
        time.sleep(2)
        element = driver.find_element(by="xpath",
                                      value="/html/body/div[1]/div/h1[2]").text
        
        return clean_text(element)
        
print(main())



