from base_package.selenium_driver import SeleniumDriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

class TestFile(SeleniumDriver):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://learn.letskodeit.com/p/practice')
        # self.baseObj= SeleniumDriver(self.driver)


    def test_func(self):
        element = self.get_element("carselect")
        # self.baseObj.scroll_browser(direction='down')
        sel = Select(element)
        sel.select_by_value("BMW")



# if __name__ == "__main_":
# #     TestFile.test_func()

t = TestFile()
t.test_func()



