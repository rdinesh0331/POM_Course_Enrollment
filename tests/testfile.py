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
        # self.driver.find_element().
        # self.baseObj= SeleniumDriver(self.driver)


    def test_func(self):

        # element = self.get_element(locator="carselect")
        # print(element)
        # # self.baseObj.scroll_browser(direction='down')
        # sel = Select(element)
        # print(sel)
        # # sel.select_by_value("benz")
        # self.select_from_list('Benz','carselect')
        element_list = self.get_elements('//select[@id="carselect"]//option','xpath')

        for element in element_list:
            print(element.text)




# if __name__ == "__main_":
# #     TestFile.test_func()

t = TestFile()
t.test_func()



