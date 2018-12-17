from base_package.Selenium_library import SeleniumDriver
import utilities.customlog as cl

class LoginPage(SeleniumDriver):

    log = cl.custom_logger(loglevel="DEBUG")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

     # locators

    _login_link = '//a[contains(text(),"Login")]'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'
    _search_course_field = 'search-courses'
    _login_error = '//div[contains(text(),"Invalid email or password")]'
    _title = 'Practice | Let\'s Kode It'

    def clickLoginlink(self):
        self.element_click(self._login_link,locator_type="xpath")

    def enterEmail(self,email):
        self.send_text(email,self._email_field)

    def enterPassword(self,password):
        self.send_text(password,self._pass_field)

    def clickLoginButton(self):
        self.element_click(self._login_button)

    def Login(self,eusername="",epass=""):
        self.clickLoginlink()
        self.enterEmail(eusername)
        self.enterPassword(epass)
        self.clickLoginButton()

    def verify_login_success(self):
        return self.is_element_present(self._search_course_field)

    def verify_login_fail(self):
        return self.is_element_present(self._login_error)

    def verify_login_title(self):
        return self.verify_title(self._title)