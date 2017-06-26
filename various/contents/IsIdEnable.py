from selenium import webdriver

class IsIdEnable():

    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False


    # Function to perform action, if the id is enabled otherwise, the action can't be performed
    def isEnable(self):
        driver = webdriver.Firefox()        
        driver.get("https://www.google.com/")
        
        # Window Maximize
        driver.maximize_window()        
       
        
        e1 = driver.find_element_by_id("gs_htif0")
        e1State = e1.is_enabled() 
        print(" E1 is  -> " + str(e1State))
        
        driver.implicitly_wait(10)
        
        e2 = driver.find_element_by_id("gs_taif0")
        e2State = e2.is_enabled() 
        print(" E2 is  -> " + str(e2State))
        
        # We can see in the DOM that e3 is not disable.
        # So, we can perform the action here by sending the data for google search.
        e3 = driver.find_element_by_id("lst-ib")
        e3State = e3.is_enabled() 
        print(" E3 is  -> " + str(e3State))
        e3.send_keys("letskodeit")
        
        driver.close()
        
obj = IsIdEnable()
obj.isEnable()