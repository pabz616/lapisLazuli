from locators.page_elements import *

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator(SauceDemoPageLocators.USN_INPUT)
        self.password_field = page.locator(SauceDemoPageLocators.PWD_INPUT)
        self.submit_button = page.query_selector(SauceDemoPageLocators.SUBMIT_BTN)
        
    def checkUI(self):
        self.username_field.is_visible()
        self.username_field.is_editable()
    
        self.password_field.is_visible()
        self.password_field.is_enabled()
    
        self.submit_button.is_visible()
        self.submit_button.is_enabled()
        
    def submitLogin(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
        
    