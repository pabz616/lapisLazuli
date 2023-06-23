from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)
        
    def checkUI(self):
        #TODO assert all page elements
        pass
    
    def proceedToCheckout(self):
        expect(self.checkout_button).to_be_visible()
        expect(self.checkout_button).to_be_enabled()
        self.checkout_button.click()