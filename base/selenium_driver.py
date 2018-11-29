from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import os
import time
from selenium.common.exceptions import *

#class for GENERIC SELENIUM WEBDRIVER APIs

class SeleniumDriver():

    def __init__(self,driver):
        self.driver = driver

    # list of APIs created
    # 1. launch_url
    # 2. verify_title
    # 3. get_by_type
    # 4. get_element
    # 5. enter_text
    # 6. wait_for_element
    # 7. element_click
    # 8. is_element_present
    # 9. element_clear

##########################################################
    def launch_url(self, url):

        try:
            self.driver.get(url)
            print('Launched URL: '+url)
        except Exception as e:
            print('***** EXCEPTION  OCCURED *****: '+e)

##########################################################
    
    def get_by_type(self, locator_type="id"):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type =='css':
            return By.CSS_SELECTOR
        elif locator_type =='link':
            return By.LINK_TEXT
        elif locator_type == 'partial_link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type =='classname':
            return By.CLASS_NAME
        elif locator_type =='tagname':
            return By.TAG_NAME
        else:
            print('!!! INVALID LOCATOR TYPE : '+locator_type)

##########################################################
    
    def get_element(self,locator='', locator_type='id'):
        element = None
        try:
            if locator is not None:
                get_by = self.get_by_type(locator_type)
                element = self.driver.find_element(get_by,locator)
                print('Element is found using locator: {} and locator type{} '.
                      format(locator,locator_type))
                return element
            else:
                print('!!! LOCATOR ARGUMENT IS EMPTY ')
                return element
        except:
            print('!!! ELEMENT IS NOT FOUND USING locator: {} AND LOCATOR TYPE{}'.
                  format(locator, locator_type))
            return element

    ##########################################################
    
    def send_text(self,data, locator='', locator_type='ID',element=None):

        try:
            if element is not None :
                element.send_keys(data)
                print("data '{}' sent to element {}".format(data,element))
            else:
                element = self.get_element(locator,locator_type)
                if element:
                    element.send_keys(data)
                    print("data '{}' sent to element with locator: {} and locator type: {}"
                          .format(data, locator, locator_type))
                else:
                    print('!!! ELEMENT IS NOT FOUND')
        except:
            print('!!! Cant send data on the element with locator: {} and locator type: {}'
                  .format(locator, locator_type))
            print_stack()

    ##########################################################
    
    def element_click(self,locator='', locator_type='ID',element=None):

        try:
            if element is not None:
                element.click()
                print('element click is success')
            else:
                element = self.get_element(locator, locator_type)
                if element:
                    element.click()
                    print("Clicked element with locator: {} and locator type: {}"
                          .format(locator, locator_type))
                else:
                    print('!!! ELEMENT IS NOT FOUND')
        except:
            print('!!! Cant click on the element with locator: {} and locator type: {}'
                  .format(locator, locator_type))
            print_stack()

    ##########################################################
    
    def wait_for_element(self, locator, timeout = 10, locator_type='id', poll_frequency=1):

        element = None
        try:
            byType = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver,timeout,poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementNotInteractableException,
                                                     InvalidElementStateException])
            element=wait.until(ec.presence_of_element_located(byType,locator))
            print('Element appeared on the webpage')
        except:
            print('Element not appeared on the webpage')
            print_stack()
        return element

    ##########################################################

    def is_element_present(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                print('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return True
            else:
                print('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            print('!!! Element is not found!!!')
            return False


    ##########################################################


    def element_clear(self,locator = '', locator_type='id', element=None):
         try:
             if locator:
                 element=self.get_element(locator,locator_type)
             if element:
                 element.clear()
                 print('Element with locator: {} and locator type: {}'
                       .format(locator, locator_type))
             else:
                 print('!!! Element with locator: {} and locator type: {} is not found'
                       .format(locator, locator_type))
         except Exception as e:
             print('*** EXCEPTION OCCURED ***  '+str(e))


    ##########################################################

    def get_text(self,locator='', locator_type = 'id',element=None):

        try:
            if locator:
                element=self.get_element(locator,locator_type)
            if element:
                text = element.text
                print('Afer finding element,size of element: '+str(len(text)))
                if len(text) == 0:
                    text = element.get_attribute("innerText")
                if len(text)!= 0:
                    print('The text is "{}"'. format((text)))
                return text.strip()
            else:
                print('!!! Element is not found using locator: {} and locator type: {}'
                      .format(locator, locator_type))
                return None
        except:
            print('Failed to get text on the element')
            return None














