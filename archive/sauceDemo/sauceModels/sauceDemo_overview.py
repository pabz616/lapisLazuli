from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect

class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator(SwagLabsOverviewPageLocators.FINISH_BUTTON)
    
 
    def confirmPurchaseDetails(self):
        #TODO assert all page elements
        expect(self.finish_button).to_be_visible()
        expect(self.finish_button).to_be_enabled()
        self.finish_button.click()