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
import utilities.customlog as cl

#class for GENERIC SELENIUM WEBDRIVER APIs

class SeleniumDriver():

    log = cl.custom_logger(loglevel="DEBUG")
    def __init__(self,driver):
        self.driver = driver

    # list of APIs created
    # 1. launch_url
    # 2. get_title
    # 3. get_by_type
    # 4. get_element
    # 5. enter_text
    # 6. wait_for_element
    # 7. element_click
    # 8. is_element_present
    # 9. element_clear
    #10. is_element_displayed
    #11. is_element_enabled
    #12. scroll_browser
    #13. select_from_list
    #14. get_elements
    #15. verify_text_contains
    #16. verify_text_match
    #17. verify_list_match
    #18. verify_data_exists_in_list

    ##########################################################
    def launch_url(self, url):

        try:
            self.driver.get(url)
            print('Launched URL: '+url)
        except Exception as e:
            self.log.error('***** EXCEPTION  OCCURED *****: '+e)

##########################################################

    def get_title(self):
        return self.driver.title

##########################################################

    def verify_title(self,expected_title):
        try:
            actual_title = self.get_title()
            if expected_title in actual_title:
                self.log.info('Title: {} matched'.format(expected_title))
                return True
            else:
                self.log.error("Title {} mismatch, actual title: {}".format(expected_title,actual_title))
                return False
        except Exception as e:
            self.log.error ("### EXCEPTION OCCURED "+e)
            return False


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
            self.log.error('!!! INVALID LOCATOR TYPE : '+locator_type)

##########################################################
    
    def get_element(self,locator='', locator_type='id'):
        element = None
        try:
            if locator is not None:
                get_by = self.get_by_type(locator_type)
                element = self.driver.find_element(get_by,locator)
                self.log.info('Element is found using locator: {} and locator type {} '.
                      format(locator,locator_type))
                return element
            else:
                self.log.error('!!! LOCATOR ARGUMENT IS EMPTY ')
                return element
        except:
            self.log.error('!!! ELEMENT IS NOT FOUND USING locator: {} AND LOCATOR TYPE {}'.
                  format(locator, locator_type))
            return element

    ##########################################################
    
    def send_text(self,data, locator='', locator_type='ID',element=None):

        try:
            if element is not None :
                element.send_keys(data)
                self.log.info("data '{}' sent to element {}".format(data,element))
            else:
                element = self.get_element(locator,locator_type)
                if element:
                    element.send_keys(data)
                    self.log.info("data '{}' sent to element with locator: {} and locator type: {}"
                          .format(data, locator, locator_type))
                else:
                    self.log.error('!!! ELEMENT IS NOT FOUND')
        except:
            self.log.error('!!! Cant send data on the element with locator: {} and locator type: {}'
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
                    self.log.info("Clicked element with locator: {} and locator type: {}"
                          .format(locator, locator_type))
                else:
                    self.log.error('!!! ELEMENT IS NOT FOUND')
        except:
            self.log.error('!!! Cant click on the element with locator: {} and locator type: {}'
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
            self.log.info('Element appeared on the webpage')
        except:
            self.log.error('Element not appeared on the webpage')
            print_stack()
        return element

    ##########################################################

    def is_element_present(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return True
            else:
                self.log.error('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            self.log.error('!!! Element is not found!!!')
            return False


    ##########################################################


    def element_clear(self,locator = '', locator_type='id', element=None):
         try:
             if locator:
                 element=self.get_element(locator,locator_type)
             if element:
                 element.clear()
                 self.log.info('Element with locator: {} and locator type: {}'
                       .format(locator, locator_type))
             else:
                 self.log.error('!!! Element with locator: {} and locator type: {} is not found'
                       .format(locator, locator_type))
         except Exception as e:
             self.log.error('*** EXCEPTION OCCURED ***  '+str(e))


    ##########################################################

    def get_text(self,locator='', locator_type = 'id',element=None):

        try:
            if locator:
                element=self.get_element(locator,locator_type)
            if element:
                text = element.text
                self.log.info('After finding element,size of element: '+str(len(text)))
                if len(text) == 0:
                    text = element.get_attribute("innerText")
                if len(text)!= 0:
                    self.log.info('The text is "{}"'. format((text)))
                return text.strip()
            else:
                self.log.error('!!! Element is not found using locator: {} and locator type: {}'
                      .format(locator, locator_type))
                return None
        except:
            self.log.error('Failed to get text on the element')
            return None

    ##########################################################

    def is_element_displayed(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                result = element.is_displayed()
                self.log.info('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return result
            else:
                self.log.error('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            self.log.error('!!! Element is not found!!!')
            return False

    ##########################################################

    def is_element_enabled(self, locator='', locator_type='id', element=None):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                result = element.is_enabled()
                self.log.info('Element present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return result
            else:
                self.log.error('!!! Element is not present using locator: {} and locator type: {}'
                      .format (locator, locator_type))
                return False
        except:
            self.log.error('!!! Element is not found!!!')
            return False

    ##########################################################

    def scroll_browser(self, direction="up"):

        try:
            if direction.lower() == 'up':
                self.driver.execute_script('window.scrollBy(0,-1000);')
                self.log.info('Window scrolled '+direction)
            elif direction.lower()=='down':
                self.driver.execute_script('window.scrollBy(0,1000);')
                self.log.info('Window scrolled '+direction)
            else:
                self.log.error('!!!! Invalid direction ')
        except Exception as e:
            self.log.error('**** EXCEPTION OCCURED **** Method name: scroll_browser')

    ##########################################################

    def select_from_list(self, data, locator = '',locator_type='id', select_type="visibletext", element = ''):

        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                sel = Select(element)
                if select_type.lower() == 'visibletext':
                    sel.select_by_visible_text(data.strip())
                    self.log.info('Value {} selected using visible text'.format(data))
                elif select_type.lower() == 'index':
                    sel.select_by_index(data.strip())
                    self.log.info('Value {} selected using index'.format(data))
                elif select_type.lower() == 'value':
                    sel.select_by_value(data.strip())
                    self.log.info('Value {} selected using value'.format(data))
                else:
                    self.log.error('!!! INVALID SELECT TYPE')
            else:
                self.log.error('!!! ELEMENT IS NOT FOUND')
        except Exception as e:
            self.log.error('!!! EXCEPTION OCCURED when selecting the list '+ str(e))

    ##########################################################

    def get_elements(self,locator='', locator_type='id'):
        element = None
        try:
            if locator is not None:
                get_by = self.get_by_type(locator_type)
                element = self.driver.find_elements(get_by,locator)
                self.log.info('Element list found using locator: {} and locator type {} '.
                      format(locator,locator_type))
                return element
            else:
                self.log.error('!!! LOCATOR ARGUMENT IS EMPTY ')
                return element
        except:
            self.log.error('!!! ELEMENT LIST NOT FOUND USING locator: {} AND LOCATOR TYPE {}'.
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

    ##########################################################

    def save_screenshot(self,message):

            filename = message+"."+str(round(time.time()))+".png"
            screenshotdirectory = '..\screenshots'
            relativefilepath = screenshotdirectory+filename
            currentdirectory = os.path.dirname(__file__)
            destinationfile = os.path.join(currentdirectory, relativefilepath)
            destinationdirectory = os.path.join((currentdirectory,screenshotdirectory))
            try:
                if not os.path.exists(destinationdirectory):
                    os.mkdir(destinationdirectory)
                self.driver.save_screenshot(destinationfile)
                print('Screenshot saved to destination directory: {} and file name: {}'
                      .format(destinationdirectory,filename))
            except Exception as e:
                print ('!!! Exception occured while saving the screenshot '+e)







