'''
Author: rdinesh0331@ Dineshkumar Rajendran

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.select import Select
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
    #10. is_element_displayed
    #11. is_element_enabled

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
                print('Element is found using locator: {} and locator type {} '.
                      format(locator,locator_type))
                return element
            else:
                print('!!! LOCATOR ARGUMENT IS EMPTY ')
                return element
        except:
            print('!!! ELEMENT IS NOT FOUND USING locator: {} AND LOCATOR TYPE {}'.
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
                print('After finding element,size of element: '+str(len(text)))
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

    ##########################################################

    def is_element_displayed(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                result = element.is_displayed()
                print('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return result
            else:
                print('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            print('!!! Element is not found!!!')
            return False

    ##########################################################

    def is_element_enabled(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                result = element.is_enabled()
                print('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return result
            else:
                print('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            print('!!! Element is not found!!!')
            return False

    ##########################################################

    def scroll_browser(self, direction="up"):

        try:
            if direction.lower() == 'up':
                self.driver.execute_script('window.scrollBy(0,-1000);')
                print('Window scrolled '+direction)
            elif direction.lower()=='down':
                self.driver.execute_script('window.scrollBy(0,1000);')
                print('Window scrolled '+direction)
            else:
                print('!!!! Invalid direction ')
        except Exception as e:
            print('**** EXCEPTION OCCURED **** Method name: scroll_browser')

    ##########################################################

    def select_from_list(self, data, locator = '',locator_type='id', select_type="visibletext", element = ''):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                sel = Select(element)
                if select_type.lower() == 'visibletext':
                    sel.select_by_visible_text(data.strip())
                    print('Value {} selected using visible text'.format(data))
                elif select_type.lower() == 'index':
                    sel.select_by_index(data.strip())
                    print('Value {} selected using index'.format(data))
                elif select_type.lower() == 'value':
                    sel.select_by_value(data.strip())
                    print('Value {} selected using value'.format(data))
                else:
                    print('!!! INVALID SELECT TYPE')
            else:
                print('!!! ELEMENT IS NOT FOUND')
        except Exception as e:
            print('!!! EXCEPTION OCCURED when selecting the list '+ str(e))

    ##########################################################

    def get_elements(self,locator='', locator_type='id'):
        element = None
        try:
            if locator is not None:
                get_by = self.get_by_type(locator_type)
                element = self.driver.find_elements(get_by,locator)
                print('Element list found using locator: {} and locator type {} '.
                      format(locator,locator_type))
                return element
            else:
                print('!!! LOCATOR ARGUMENT IS EMPTY ')
                return element
        except:
            print('!!! ELEMENT LIST NOT FOUND USING locator: {} AND LOCATOR TYPE {}'.
                  format(locator, locator_type))
            return element

    ##########################################################

    def verify_text_contains(self, actualtext, expectedtext):

            print('Expected text from Application web UI: '+expectedtext)
            print('Actual text from Appplication web UI: '+actualtext)
            if expectedtext in actualtext:
                print('Verification contains')
                return True
            else:
                print('!!! VERIFICATION FAILED')
                return False

    ##########################################################

    def verify_text_match(self, actualtext, expectedtext):

            print('Expected text from Application web UI: '+expectedtext)
            print('Actual text from Appplication web UI: '+actualtext)
            if expectedtext == actualtext:
                print('Verification contains')
                return True
            else:
                print('!!! VERIFICATION FAILED')
                return False

    ##########################################################

    def verify_list_match(self,actual_list,expected_list):

        if set(actual_list)==set(expected_list):
            print('LIST MATCHED')
            return True
        else:
            print('!!! LIST MATCH FAILED')
            return False


    ##########################################################

    def verify_data_exists_in_list(self, data, locator='', locator_type='id', elementlist=None):

        try:
            if locator:
                elementlist= self.get_elements(locator, locator_type)
                if elementlist is not None:
                    for element in elementlist:
                        if element.text == data:
                            print ('List value present')
                            return True
                    print('!!! Value {} is not present in the element list'.format(data))
                    return False
                else:
                    print('!!! ELEMENT LIST IS BLANK')
                    return False
        except Exception as e:
            print('*** EXCEPTION occured *** '+e)
            return False






