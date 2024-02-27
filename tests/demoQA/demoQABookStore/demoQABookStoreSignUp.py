""" BOOK STORE NEW USER REGISTRATION """

from demoQALocators.pageElements import BookStoreRegistration, BookStoreLogin
from playwright.sync_api import expect

from faker import Faker
fake = Faker()


class BookStoreRegistrationPage:
    def __init__(self, page):
        self.page = page
        self.firstNameField = page.locator(BookStoreRegistration.REGISTER_FNAME)
        self.firstNameField_placeholder = self.firstNameField.get_attribute('placeholder')
        
        self.lastNameField = page.locator(BookStoreRegistration.REGISTER_LNAME)
        self.lastNameField_placeholder = self.lastNameField.get_attribute('placeholder')
        
        self.userNameField = page.locator(BookStoreRegistration.REGISTER_USN)
        self.userNameField_placeholder = self.userNameField.get_attribute('placeholder')
        
        self.passwordField = page.locator(BookStoreRegistration.REGISTER_PWD)
        self.passwordField_placeholder = self.passwordField.get_attribute('placeholder')
        
        self.captchaInput = page.locator(BookStoreRegistration.REGISTER_CAPTCHA)
        self.submitBtn = page.locator(BookStoreRegistration.REGISTER_SUBMIT_BTN)
        self.backToLoginBtn = page.locator(BookStoreRegistration.REGISTER_BACK_BTN)
        
    def checkUI(self):
        expect(self.firstNameField).to_be_visible()
        expect(self.firstNameField).to_be_editable()
        expect(self.firstNameField_placeholder).to_have_text('First Name')
        
        expect(self.lastNameField).to_be_visible()
        expect(self.lastNameField).to_be_editable()
        expect(self.lastNameField_placeholder).to_have_text('Last Name')
        
        expect(self.userNameField).to_be_visible()
        expect(self.userNameField).to_be_editable()
        expect(self.userNameField_placeholder).to_have_text('UserName')
        
        expect(self.passwordField).to_be_visible()
        expect(self.passwordField).to_be_editable()
        expect(self.passwordField_placeholder).to_have_text('Password')
        
        expect(self.submitBtn).to_be_visible()
        expect(self.submitBtn).not_to_be_disabled()
        
        expect(self.captchaInput).to_be_visible()
        
        expect(self.backToLoginBtn).to_be_visible()
        expect(self.backToLoginBtn).not_to_be_disabled()
              
    def completeRegistrationForm(self, fname, lname, usn, pwd):
        pass
    
    def confirmSuccessfulRegistration(self):
        pass
    
    def confirmErrorMessage(self):
        pass
    