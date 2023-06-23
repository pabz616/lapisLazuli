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
        #TODO assert all page elements
        pass

    def completeCustomerInfo(self):
        self.firstName.fill("Tester_FirstName")
        self.lastName.fill("Tester_LastName")
        self.zipCode.fill("10010")
        self.continue_button.click()
    