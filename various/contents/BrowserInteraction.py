from selenium import webdriver

class BrowserInteration():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = False
    
    def testVariousBrowserInteraction(self):
        url = "http://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        
        # Window Maximize
        driver.maximize_window()
        
        # Open the URL
        driver.get(url)
        
        # Get Title
        title = driver.title
        print(" Title of the Page is .. " + title)
        
        # Get Current URL
        print("Current URL is ... " + driver.current_url)
        
        driver.refresh()
        print("Browser refreshed 1st time")
        
        driver.get(driver.current_url)
        print("Browser refreshed 2nd Time")
        
        # Open Another URL
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        
        #  Browser Back 
        driver.back()
        
        # Get Page Source
        p_source = driver.page_source
        print(p_source)
        
        driver.close()
        

obj = BrowserInteration()
obj.testVariousBrowserInteraction()
        