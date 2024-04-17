from sauceLocators.page_elements import *
from playwright.sync_api import sync_playwright, expect
from sauceUtils.data import *

class OrderCompletePage:
    def __init__(self, page):
        self.page = page
        self.success_pageTitle = page.locator(SwagLabsOrderConfirmationPageLocators.SECTION_TITLE)
        self.success_image = page.locator(SwagLabsOrderConfirmationPageLocators.IMG)
        self.success_message = page.locator(SwagLabsOrderConfirmationPageLocators.MSG)
        self.success_copy = page.locator(SwagLabsOrderConfirmationPageLocators.COPY)        
        self.home_button = page.locator(SwagLabsOrderConfirmationPageLocators.BTN)
        
    def confirmOrderSuccessDetails(self):
        expect(self.success_pageTitle).to_be_visible()
        expect(self.success_pageTitle).to_have_text('Checkout: Complete!')
        #
        expect(self.success_image).to_be_visible()
        expect(self.success_image).to_have_attribute("alt", SauceDemoConfirmation.successImageAlt)
        #
        expect(self.success_message).to_be_visible()
        expect(self.success_message).to_have_text(SauceDemoConfirmation.successMessage)
        #
        expect(self.success_copy).to_be_visible()
        expect(self.success_copy).to_have_text(SauceDemoConfirmation.successCopy)
        #
        expect(self.home_button).to_be_visible()
        expect(self.home_button).to_be_enabled()
        self.home_button.click()