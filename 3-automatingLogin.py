from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time



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

    URL = "https://automated.pythonanywhere.com/login/"   #Connects driver to webpage, just enter the URL
    driver.get(URL)

    return driver

#we used id instead of an xpath, because the id is very specific and it is more practical to use it instead of having to provide an entire path
#The .send_keys() is used to enter the username and password into the login field
#Keys.RETURN was imported to automate the process of pressing enter/return
#.click() is used to click on the element
def main():
    driver = get_driver()
    driver.find_element(by="id", 
                        value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id",
                        value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", 
                        value="/html/body/nav/div/a").click()
    print(driver.current_url)
    

main()