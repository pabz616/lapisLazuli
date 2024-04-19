from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)
        self.continue_shopping_button = page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING)
        self.remove_item_button = page.locator(SwagLabsCartPageLocators.REMOVE_BTN)
        
        self.itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
        
    def checkUI(self):
        #TODO assert all page elements
        pass
    
    def proceedToCheckout(self):
        expect(self.checkout_button).to_be_visible()
        expect(self.checkout_button).to_be_enabled()
        self.checkout_button.click()
    
    def continueShopping(self):
        expect(self.continue_shopping_button).to_be_visible()
        expect(self.continue_shopping_button).to_be_enabled()
        self.continue_shopping_button.click()
    
    def removeItem(self):
        expect(self.remove_item_button).to_be_visible()
        expect(self.remove_item_button).to_be_enabled()
        self.remove_item_button.click()
        expect(self.itemAddedBadge).not_to_be_visible()
        expect(self.checkout_button).not_to_be_enabled()
        
    
    