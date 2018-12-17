from base_package.selenium_driver import SeleniumDriver
import utilities.customlog as cl
import logging


class BasePage(SeleniumDriver):

    log = cl.custom_logger(loglevel="DEBUG")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

##########################################################

    def verify_title(self, expected_title):
        try:
            actual_title = self.get_title()
            if expected_title in actual_title:
                self.log.info('Title: {} matched'.format(expected_title))
                return True
            else:
                self.log.error("Title {} mismatch, actual title: {}".format(expected_title, actual_title))
                return False
        except Exception as e:
            self.log.error("### EXCEPTION OCCURED " + e)
            return False

##########################################################

    def verify_text_contains(self, actualtext, expectedtext):

        print('Expected text from Application web UI: ' + expectedtext)
        print('Actual text from Appplication web UI: ' + actualtext)
        if expectedtext in actualtext:
            print('Verification contains')
            return True
        else:
            print('!!! VERIFICATION FAILED')
            return False

##########################################################

    def verify_text_match(self, actualtext, expectedtext):

        print('Expected text from Application web UI: ' + expectedtext)
        print('Actual text from Appplication web UI: ' + actualtext)
        if expectedtext == actualtext:
            print('Verification contains')
            return True
        else:
            print('!!! VERIFICATION FAILED')
            return False

##########################################################

    def verify_list_match(self, actual_list, expected_list):

        if set(actual_list) == set(expected_list):
            print('LIST MATCHED')
            return True
        else:
            print('!!! LIST MATCH FAILED')
            return False

##########################################################
