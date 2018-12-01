


class RegisterCourses():

    def __init__(self,driver):
        self.driver = driver


    _search_course_field_ = "search-courses"
    _search_course_button = "search-course-button"
    _course_field = "//div[contains(text(), 'JavaScript')]"
    _enroll_button = "enroll-button-top"
    _cardNo = 'cardnumber'
    _cardExpiration = 'exp-date'
    _cvccode= 'cvc'
    _postalcode = 'postal'
    _agreeterms = 'agreed_to_terms_checkbox'
