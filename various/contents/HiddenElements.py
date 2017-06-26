import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class HiddenElements():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False

    def letKodeIt(self):
        driver = webdriver.Firefox()        
        url = "https://letskodeit.teachable.com/p/practice"       
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        
        # Find the state of the Text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()   # True if visible, False if hiddenn        
        # Exception if not present in the DOM
        print("Text is visible .. " +str(textBoxState))
        time.sleep(2)
        
        # Click the Hide button 
        driver.find_element_by_id("hide-textbox").click()
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible .. " +str(textBoxState))
        time.sleep(2)
        
        # Click the Show Button
        textShowBoxElement = driver.find_element_by_id("show-textbox").click()
        #textBoxState = textBoxElement.is_displayed()
        print("Text is visible .. " +str(textShowBoxElement.is_displayed()))
        time.sleep(2)
        
        driver.close()
        
    
    def testExpedia(self):
        driver = webdriver.Firefox()        
        url = "https://www.expedia.com"       
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        
        driver.find_element_by_id("tab-flight-tab-hp").click()
        time.sleep(2)
        
        drpDownElement = driver.find_element_by_id("package-1-children-hp-package")
        print("Text is visible .. " +str(drpDownElement.is_displayed()))
        
        driver.close()
    
obj = HiddenElements()
obj.letKodeIt()
obj.testExpedia()
        
        
        
        
        
        
        
        