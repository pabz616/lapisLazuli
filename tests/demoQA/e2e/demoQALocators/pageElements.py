class BookStoreLogin(object):
    LOGIN_SUBMIT_BTN = '//button[@id="login"]'
    LOGIN_USN_INPUT = '//input[@id="userName"]'
    LOGIN_PWD_INPUT = '//input[@id="password"]'
    NEW_USER_BTN = '//button[@id="newUser"]'
    
    LOGIN_USN_INPUT_ERROR = '(//input[contains(@class,"is-invalid form-control")])[1]'
    LOGIN_PWD_INPUT_ERROR = '(//input[contains(@class,"is-invalid form-control")])[2]'
    LOGIN_ERROR_MSG = '//p[@id="name"]'
    

class BookStoreRegistration(object):
    REGISTER_BTN = '//button[@id="newUser"]'
    REGISTER_FNAME = '//input[@id="firstname"]'
    REGISTER_LNAME = '//input[@id="lastname"]'
    REGISTER_USN = '//input[@id="userName"]'
    REGISTER_PWD = '//input[@id="password"]'
    REGISTER_CAPTCHA = '//div[@class="recaptcha-checkbox-border"]'
    REGISTER_SUBMIT_BTN = '//button[@id="register"]'
    REGISTER_BACK_BTN = '//button[@id="gotologin"]'
    REGISTER_ERROR = '//p[@id="name"]'
    INVALID_STATE = '//input[contains(@class,"is-invalid form-control")]'


class BookStoreSearch(object):
    SEARCH_INPUT = '//input[@id="searchBox"]'
    

class BookStoreDisplay(object):
    BOOK_TBL = '//div[@class="ReactTable -striped -highlight"]'
    BOOK_TBL_HEADER = '//div[@class="rt-thead -header"]'
    BOOK_TBL_BODY = '//div[@class="rt-tbody"]'
    BOOK_TBL_ROW = '//div[@class="rt-tr-group"]'
    BOOK_TBL_R1_IMG = '//img[@alt="image"]'
    BOOK_TBL_R1_TITLE = '//div/span[@id="see-book-Git Pocket Guide"]/a'
    BOOK_TBL_R1_AUTHOR = '(//div[@class="rt-td"])[3]'
    BOOK_TBL_R1_PUBLISHER = '(//div[@class="rt-td"])[4]'
    BOOK_1 = '//a[@href="/books?book=9781449325862"]'
    PAGINATION = '//div[@class="-pagination"]'
    PREVIOUS_BTN = '//div[@class="-previous"]/button'
    NEXT_BTN = '//div[@class="-next"]/button' 
    PAGE_COUNT = '//span[@class="-pageInfo"]'
    PAGE_INPUT = '//div[@class="-pageJump"]/input'
    PAGE_SELECT = '//select[@aria-label="rows per page"]'
    NO_RESULTS = '//div[@class="rt-noData"]'
    LOGIN_NAV = '(//button)[2]'
    
    
class BookStoreUserProfile(object):
    AUTH_USER_LABEL = '//label[@id="userName-label"]'
    AUTH_USER_VALUE = '//label[@id="userName-value"]'
    LOGOUT_BTN = '//button[@id="submit"]'


class PracticeForm(object):
    FORM_TITLE = '//h5'
    STUDENT_FIRSTNAME = '[id="firstName"]'
    STUDENT_LASTNAME = '[id="lastName"]'
    STUDENT_EMAIL = '[id="userEmail"]'
    STUDENT_GENDER_M = '//label[@for="gender-radio-1"]'
    STUDENT_GENDER_F = '//label[@for="gender-radio-2"]'
    STUDENT_GENDER_O = '//label[@for="gender-radio-3"]'
    STUDENT_PHONE = '[id="userNumber"]'
    STUDENT_DOB = '[id="dateOfBirthInput"]'
    STUDENT_SUBJECT = '//div[contains(@class,"subjects-auto-complete__value-container")]'
    STUDENT_HOBBY1 = '//label[@for="hobbies-checkbox-1"]'
    STUDENT_HOBBY2 = '//label[@for="hobbies-checkbox-2"]'
    STUDENT_HOBBY3 = '//label[@for="hobbies-checkbox-3"]'
    STUDENT_PIC_UPLOAD = '[id="uploadPicture"]'
    STUDENT_ADDR = '[id="currentAddress"]'
    STUDENT_STATE_DDL = '[id="state"]'
    STUDENT_STATE_INPUT = '[id="react-select-3-input"]'
    STUDENT_CITY_DDL = '[id="city"]'
    SUBMIT_BUTTON = '[id="submit"]'
    CONFIRMATION_WINDOW = '//div[@class="modal-content"]'
    CLOSE_BUTTON = '//button[contains(.,"Close")]'
    
    STUDENT_FIRSTNAME_ERROR = ''
    STUDENT_LASTNAME_ERROR = ''
    STUDENT_EMAIL_ERROR = ''
    STUDENT_PHONE_ERROR = ''
    

    