from selenium import webdriver
from selenium.webdriver.common.by import By
from builtins import str
import time

class RadioButtonFindElements():
    
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False

    def radioFindElementsList(self):
        driver = webdriver.Firefox()        
        url = "https://letskodeit.teachable.com/p/practice"       
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        
        radioButtonList = driver.find_elements(
                                By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        
        listSize = len(radioButtonList)        
        print("Size of the Radio Button List is ...  " + str(listSize))
        
        for radioButton in radioButtonList :
            isSelected = radioButton.is_selected()
            
            if not isSelected :
                radioButton.click()
                time.sleep(2)
                
        driver.close()
        
obj = RadioButtonFindElements()
obj.radioFindElementsList()
        