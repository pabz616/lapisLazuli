
class QuotesPageLocators(object):
    PAGE_HEADING = '//h1/a'
    LOGIN_LINK = '[href="/login"]'
    USN_INPUT = '[id="username"]'
    PWD_INPUT = '[id="password"]'
    SUBMIT_BTN = '[class="btn btn-primary"]'
    LOGOUT_LINK = '[href="/logout"]'
    QUOTES_TEXT = '[class="quote"]'
    
class SauceDemoPageLocators(object):
    PAGE_HEADING = '[class="login_logo"]'
    USN_INPUT = '[id="user-name"]'
    PWD_INPUT = '[id="password"]'
    SUBMIT_BTN = '[id="login-button"]'
    
class SwagLabsPageLocators(object):
    PAGE_HEADING = '[class="title"]'
    MENU_BUTTON = '[id="react-burger-menu-btn"]'
    VIEW_ALL_ITEMS = '[id="inventory_sidebar_link"]'
    VIEW_ABOUT = '[id="about_sidebar_link"]'
    LOGOUT_LINK = '[id="logout_sidebar_link"]'
    RESET_APP = '[id="reset_sidebar_link"]'
    CLOSE_MENU = '[id="react-burger-cross-btn"]'