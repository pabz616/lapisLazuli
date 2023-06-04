from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.firstName = page.locator(SwagLabsCustomerInfoPageLocators.FNAME_INPUT)
        self.lastName = page.locator(SwagLabsCustomerInfoPageLocators.LNAME_INPUT)
        self.zipCode = page.locator(SwagLabsCustomerInfoPageLocators.ZIP_INPUT)
        self.continue_button = page.locator(SwagLabsCustomerInfoPageLocators.CONTINUE_BUTTON)
    
    def checkUI(self):
        #TODO assert all page elements
        pass

    def completeCustomerInfo(self):
        self.firstName.fill("Tester_FirstName")
        self.lastName.fill("Tester_LastName")
        self.zipCode.fill("10010")
        self.continue_button.click()
    