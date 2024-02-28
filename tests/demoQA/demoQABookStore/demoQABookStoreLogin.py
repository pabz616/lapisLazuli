""" BOOK STORE USER LOGIN """

from demoQALocators.pageElements import BookStoreLogin
from playwright.sync_api import expect


class BookStoreLoginPage:
    def __init__(self, page):
        self.page = page
        self.usernameField = page.locator(BookStoreLogin.LOGIN_USN_INPUT)
        self.usernameField_placeholder = self.usernameField.get_attribute('placeholder')
        
        self.passwordField = page.locator(BookStoreLogin.LOGIN_PWD_INPUT)
        self.passwordField_placeholder = self.passwordField.get_attribute('placeholder')
        
        self.loginBtn = page.locator(BookStoreLogin.LOGIN_SUBMIT_BTN)
        self.registrationBtn = page.locator(BookStoreLogin.NEW_USER_BTN)
        
    def checkUI(self):
        expect(self.usernameField).to_be_visible()
        expect(self.usernameField).to_be_editable()
        expect(self.usernameField_placeholder).to_have_text('UserName')
        
        expect(self.passwordField).to_be_visible()
        expect(self.passwordField).to_be_editable()
        expect(self.passwordField_placeholder).to_have_text('Password')
        
        expect(self.loginBtn).to_be_visible()
        expect(self.loginBtn).not_to_be_disabled()
        
        expect(self.registrationBtn).to_be_visible()
        expect(self.registrationBtn).not_to_be_disabled()
        
    def submitLogin(self, usn, pwd):
        self.usernameField.fill(usn)
        self.passwordField.fill(pwd)
        self.loginBtn.click()
        
        # TODO - test valid user login, invalid, random data, boundary, password strength, required fields
        
    def navigateToBookStoreRegistrationPage(self):
        self.registrationBtn.click()
        pass
        
    def confirmLoginFailed(self):
        pass