from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.firstName = page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)
        self.lastName = page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)
        self.zipCode = page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)
        self.continue_button = page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON)
  
    
    def checkUI(self):
        expect(self.firstName).to_be_visible()
        expect(self.firstName).to_be_editable()

        expect(self.lastName).to_be_visible()
        expect(self.lastName).to_be_editable()
        
        expect(self.zipCode).to_be_visible()
        expect(self.zipCode).to_be_editable()
        
        expect(self.continue_button).to_be_visible()
        expect(self.continue_button).to_be_enabled()
        
    def completeCustomerInfo(self, fName, lName, zipCode):
        self.firstName.fill(fName)
        self.lastName.fill(lName)
        self.zipCode.fill(zipCode)
        self.continue_button.click()
    