from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import os.path

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
    #optionsForSearch.add_experimental_option("detach", True)
    

    
    driver = webdriver.Chrome(service=service, options=optionsForSearch)       #add the service attribute to fix the IDE problem

   #Connects driver to webpage, just enter the URL
    driver.get(url)

    return driver

def clean_text(text):
    '''Filters and extracts only the temperature (the dynamic data) from the webpage'''
    output = int(text.split(": ")[1])
    return output

def create_file(scraped_temperature):
    '''Gets the current date and time, and creates a new file with a it in its name, as well as the average world
    temperature at that exact time written in it, and then saves it to its assigned folder'''
    
    folder_path = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\GabTheFolder\\Python projects\\PYTHON-AUTOMATION-PROJECTS\\Classes1,2,3,-Challenge+txtFiles"
    
    date = datetime.now()
    current_date = date.strftime("%d-%m-%Y")
    t = time.localtime()
    current_time = time.strftime("%H-%M-%S", t)
    
    file_name = current_date + "." + current_time + ".txt"
    file_at_path = os.path.join(folder_path, file_name)
    
    file = open(file_at_path, 'x')
    file.write(str(scraped_temperature))
    file.close()


def main():
    driver = get_driver("https://automated.pythonanywhere.com/")
    web_element = driver.find_element(by="xpath",
                                      value="/html/body/div[1]/div/h1[2]")
    time.sleep(2)
    element = web_element.text
    print(element)
    temperature = clean_text(element) 
    create_file(temperature)

    return temperature


number_of_iterations = int(input("How many temperatures do you want: "))
for i in range(number_of_iterations):
    main()