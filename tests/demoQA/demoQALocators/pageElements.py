class TextFormLocators(object):
    PAGE_HEADER = '[class="main-header"]'
    FULLNAME_INPUT_LABEL = '[id="userName-label"]'
    FULLNAME_INPUT = '[id="userName"]'
    EMAIL_INPUT_LABEL = '[id="userEmail-label"]'
    EMAIL_INPUT = '[id="userEmail"]'
    EMAIL_INPUT_ERROR = '//input[contains(@class,"mr-sm-2 field-error form-control")]'
    ADDRESS_INPUT_LABEL = '[id="currentAddress-label"]'
    ADDRESS_INPUT = '//textarea[@id="currentAddress"]'
    PERM_ADDRESS_INPUT_LABEL = '[id="permanentAddress-label"]'
    PERM_ADDRESS_INPUT = '//textarea[@id="permanentAddress"]'
    SUBMIT_BUTTON = '[id="submit"]'
    RESULTS_OUTPUT = '[id="output"]'
    
    
class CheckBoxLocators(object):
    PAGE_HEADER = '[class="main-header"]'
    HOME_TOGGLE = '//button[@aria-label="Toggle"]'
    DESKTOP_TOGGLE = '(//button[@aria-label="Toggle"])[2]'
    EXPAND = '//button[@aria-label="Expand all"]'
    COLLAPSE = '//button[@aria-label="Collapse all"]'
    HOME_CHKBX = '//span[@class="rct-checkbox"]'
    HOME_CHKBX_TITLE = '//span[@class="rct-title"]'
    MESSAGE = '[id="result"]'
    SUBDIR1 = '(//span[@class="rct-text"])[1]'
    SUBDIR2 = '(//span[@class="rct-text"])[2]'
    SUBDIR3 = '(//span[@class="rct-text"])[3]'
    SUBDIR4 = '(//span[@class="rct-text"])[4]'
    SUBDIR5 = '(//span[@class="rct-text"])[5]'
    SUBDIR6 = '(//span[@class="rct-text"])[6]'
    SUBDIR7 = '(//span[@class="rct-text"])[7]'
    SUBDIR8 = '(//span[@class="rct-text"])[8]'
    SUBDIR9 = '(//span[@class="rct-text"])[9]'

    
class RadioButtonLocators(object):
    PAGE_HEADER = '[class="main-header"]'
    RB_QUESTION = '//div[class="mb-3"]'
    RB_ANSWER1_LABEL = '//label[@for="yesRadio"]'
    RB_ANSWER1 = '//input[@id="yesRadio"]'
    RB_ANSWER2_LABEL = '//label[@for="impressiveRadio"]'
    RB_ANSWER2 = '//input[@id="impressiveRadio"]'
    RB_ANSWER3_LABEL = '//label[@for="noRadio"]'
    RB_ANSWER3 = '//input[@id="noRadio"]'
    MSG = '//p[@class="mt-3"]'
    
    
class LinksLocators(object):
    PAGE_HEADER = '[class="main-header"]'
    MSG = '//p[@id="linkResponse"]'
    
    
class DatePickerLocators(object):
    PAGE_HEADER = '//h1[class="text-center"]'
    DATE = '//input[@id="datePickerMonthYearInput"]'
    DATE_PICKER = '//div[@class="react-datepicker"]'
    DATETIME = '//input[@id="dateAndTimePickerInput"]'