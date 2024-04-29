""" BOOK STORE NEW USER REGISTRATION """

from demoQALocators.pageElements import BookStoreRegistration
from playwright.sync_api import expect
from demoQAUtils.data import ErrorMessages as msg


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
        
        self.errorMsg = page.locator(BookStoreRegistration.REGISTER_ERROR)
        self.formErrorState = page.locator(BookStoreRegistration.INVALID_STATE)
        
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
        expect(self.captchaInput).not_to_be_checked()
        
        expect(self.backToLoginBtn).to_be_visible()
        expect(self.backToLoginBtn).not_to_be_disabled()
              
    def completeRegistrationForm(self, fname, lname, usn, pwd):
        self.firstNameField.fill(fname)
        self.lastNameField.fill(lname)
        self.userNameField.fill(usn)
        self.passwordField.fill(pwd)
        
        self.submitBtn.click()
    
    def confirmSuccessfulRegistration(self):
        pass
    
    def confirmPasswordErrorMessage(self):
        expect(self.errorMsg).to_be_visible()
        expect(self.errorMsg).to_have_text(msg.passwordValidationMsg)
    
    def confirmRequiredInputValidationState(self):
        fname_required = self.formErrorState.nth(1)
        lname_required = self.formErrorState.nth(2)
        usn_required = self.formErrorState.nth(3)
        pwd_required = self.formErrorState.nth(4)
        
        expect(fname_required).to_be_visible()
        expect(lname_required).to_be_visible()
        expect(usn_required).to_be_visible()
        expect(pwd_required).to_be_visible()
        
    def confirmErrorMessageForexisting_userIsDisplayed(self):
        expect(self.errorMsg).to_be_visible()
        expect(self.errorMsg).to_have_text(msg.userExistsMsg)

    def clearForm(self):
        self.firstNameField.clear()
        self.lastNameField.clear()
        self.userNameField.clear()
        self.passwordField.clear()
        