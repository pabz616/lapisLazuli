""" BOOK STORE SEARCH """

from demoQALocators.pageElements import BookStoreSearch
from playwright.sync_api import expect


class BookStoreSearchPage:
    def __init__(self, page):
        self.page = page
        self.element = page.locator(BookStoreSearch.element)
        
    def checkUI(self):

        expect(self.element).to_be_visible()
        expect(self.element).to_contain_text('whatever')
        
        # LOGIN BUTTON
        
        # BOOKSTORE CATALOG
        
    def searchTerm(self, term):
        self.element.fill(term)
        
        # TODO - search for valid term, invalid term, random characters, long characters, foreign titles