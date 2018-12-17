'''
Utility - TestRunStatus
CheckPoint class implementation
It provides functionality to assert the result
'''

from base_package.Selenium_library import SeleniumDriver
import utilities.customlog as cl

class TestRunStatus(SeleniumDriver):

    log = cl.custom_logger(loglevel="DEBUG")

    def __init__(self,driver):
        super().__init__(driver)
        self.resultSet = []

    def set_result(self, result, resultMessage):

       try:
           if result is not None:
                if result:
                    self.resultSet.append("PASS")
                    self.log.info("### VERIFICATION PASSED")
                else:
                    self.resultSet.append("FAIL")
                    self.info.error("### VERIFICATION FAILED"+ resultMessage)
                    self.save_screenshot(resultMessage)
           else:
                self.resultSet.append("FAIL")
                self.info.error("### VERIFICATION FAILED" + resultMessage)
                self.save_screenshot(resultMessage)

       except Exception as e:
            self.resultSet.append("FAIL")
            self.info.error("### EXCEPTION OCCURED"+ e)
            self.save_screenshot(resultMessage)


    def mark_result(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(self.result, resultMessage)


    def mark_final_result(self,testcaseName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """

        self.set_result(result, resultMessage)

        if "FAIL" in self.resultSet:
            self.log.error(testcaseName+"  TEST RUN FAILED")
            self.resultSet.clear()
            assert True == False

        else:
            self.info.info(testcaseName+"  TEST RUN PASSED")
            self.resultSet.clear()
            assert True == True