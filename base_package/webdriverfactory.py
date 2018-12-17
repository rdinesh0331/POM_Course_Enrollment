from base_package.Selenium_library import SeleniumDriver
from selenium import webdriver

class WebDriverFactory():

   def __init__(self,browser):
        self.browser = browser


   def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """

        base_url="https://learn.letskodeit.com/p/practice"
        if self.browser.lower() == "firefox":
            driver = webdriver.Firefox()
        elif self.browser.lower()== "chrome":
            driver = webdriver.Chrome()
        elif self.browser.lower() == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        return driver

