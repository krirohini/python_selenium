import time
from selenium import webdriver


class RadioAndCheckBox ():
    
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False

    def isSelected(self):
        driver = webdriver.Firefox()        
        url = "https://letskodeit.teachable.com/p/practice"       
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        
        bmw_rd = driver.find_element_by_id("bmwradio")
        bmw_rd.click()
        time.sleep(2)
        
        benz_rd = driver.find_element_by_id("benzradio")
        benz_rd.click()
        time.sleep(2)
        
        bmw_chk = driver.find_element_by_id("bmwcheck")
        bmw_chk.click()
        time.sleep(2)
        
        bennz_chk = driver.find_element_by_id("benzcheck")
        bennz_chk.click()
        # time.sleep(2)
        
        print("BMW Radio Button is Selected ?  " + str(bmw_rd.is_selected()))
        print("BENZ Radio Button is Selected ?  " + str(benz_rd.is_selected()))        
        print("BMW Radio Button is Selected ?  " + str(bmw_chk.is_selected()))
        print("BENZ Radio Button is Selected ?  " + str(bennz_chk.is_selected())) 
              
        driver.close()   
        
obj = RadioAndCheckBox()
obj.isSelected()
