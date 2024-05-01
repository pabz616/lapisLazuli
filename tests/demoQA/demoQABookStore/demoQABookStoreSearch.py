""" BOOK STORE SEARCH """

from demoQALocators.pageElements import BookStoreSearch, BookStoreDisplay
from playwright.sync_api import expect


class BookStoreSearchPage:
    def __init__(self, page):
        self.page = page
        self.searchField = page.locator(BookStoreSearch.SEARCH_INPUT)
        self.bookStoreCatalog = page.locator(BookStoreDisplay.BOOK_TBL)
        self.noResultsElement = page.locator(BookStoreDisplay.NO_RESULTS)
        
        self.alert = page.on("dialog", lambda dialog: dialog.accept())
        
    def checkUI(self):

        expect(self.searchField).to_be_visible()
        expect(self.searchField).to_be_empty()
        expect(self.searchField).to_have_placeholder('Type to search')
           
    def enterSearchTerm(self, term):
        self.searchField.fill(term)
        
    def confirmResults(self):
        expect(self.noResultsElement).not_to_be_visible
        
    def confirmNoResults(self):
        expect(self.noResultsElement).to_be_visible
        
    def confirmNoAlertShown(self):
        expect(self.alert).not_to_be_visible
        