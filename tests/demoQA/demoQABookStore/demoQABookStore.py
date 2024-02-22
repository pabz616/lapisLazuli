""" BOOK STORE LANDING """

from demoQALocators.pageElements import BookStoreDisplay
from playwright.sync_api import expect


class BookStoreDisplayPage:
    def __init__(self, page):
        self.page = page
        self.element = page.locator(BookStoreDisplay.element)
    
    def checkUI(self):
        expect(self.element).to_be_visible()
        expect(self.element).to_contain_text('whatever')
        
        # TODO check the page for the image, the title, the author, and the publisher