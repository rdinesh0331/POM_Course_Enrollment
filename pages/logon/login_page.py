

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # locators

    _login_link = '//a[contains(text(),"Login")]'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'
    _search_course_field = 'search-courses'
    _login_error = '//div[contains(text(),"Invalid email or password")]'c