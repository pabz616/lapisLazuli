""" BOOK STORE USER LOGIN """

from demoQALocators.pageElements import BookStoreLogin
from playwright.sync_api import expect


class BookStoreLoginPage:
    def __init__(self, page):
        self.page = page
        self.registrationBtn = page.locator(BookStoreLogin.NEW_USER_BTN)
        # self.element = page.locator(BookStoreLogin.element)
        
    def checkUI(self):
        pass
        # expect(self.element).to_be_visible()
        # expect(self.element).to_contain_text('whatever')
        
    def submitLogin(self, usn, pwd):
        self.element.fill(usn)
        self.element.fill(pwd)
        self.element.click()
        
        # TODO - test valid user login, invalid, random data, boundary, password strength, required fields
        
    def navigateToBookStoreRegistrationPage(self):
        pass
    
    def confirmLoginIsSuccessful(self):
        pass
    
    def confirmLoginFailed(self):
        pass