""" BOOK STORE NEW USER REGISTRATION """

from demoQALocators.pageElements import BookStoreSignUp
from playwright.sync_api import expect


class BookStoreRegistrationPage:
    def __init__(self, page):
        self.page = page
        self.element = page.locator(BookStoreSignUp.element)
        
    def checkUI(self):
        expect(self.element).to_be_visible()
        expect(self.element).to_contain_text('whatever')
        
    def fillForm(self, fname, lname, usn, pwd):
        pass
    
    # TODO - test valid user creation, invalid, random data, boundary, password strength, required fields
    
    def confirmSuccessfulRegistration(self):
        pass
    
    def confirmErrorMessage(self):
        pass
    