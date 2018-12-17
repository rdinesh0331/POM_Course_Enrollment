import pytest
import unittest
from pages.logon.login_page import LoginPage
from utilities.testrunstatus import TestRunStatus

@pytest.mark.usefixtures("oneTimeSetup","setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse = True)
    def setupClass(self,oneTimeSetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestRunStatus(self.driver)


    def test_VerifyLoginSuccess(self):
        self.lp.Login("test@email.com","abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark_result(result1,"Title mismatch")
        result2 = self.lp.verify_login_success()
        self.ts.mark_final_result("Verify Login success",result2, "Login failed")

