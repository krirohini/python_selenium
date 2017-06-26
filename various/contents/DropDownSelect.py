import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class DropDownSelect():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False

    def dropDown(self):
        driver = webdriver.Firefox()        
        url = "https://letskodeit.teachable.com/p/practice"       
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        
        element = driver.find_element_by_id("carselect")
        sel = Select(element)
        
        print("Select BMW by Value")
        sel.select_by_value("bmw")
        time.sleep(2)
        
        print("Select BENZ by index")
        sel.select_by_index(1)
        time.sleep(2)
        
        print("Select HONDA by Visible Text")
        sel.select_by_visible_text("Honda")
        time.sleep(2)
        
        print("Select BMW by index")
        sel.select_by_index(0)
        time.sleep(2)
        
        driver.close()
        
obj = DropDownSelect()
obj.dropDown()