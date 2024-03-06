""" BOOK STORE USER PROFILE """
 
from demoQALocators.pageElements import BookStoreUserProfile, BookStoreSearch, BookStoreDisplay
from playwright.sync_api import expect
from demoQAUtils.data import ProjectData as pd


class BookStoreProfilePage:
    def __init__(self, page):
        self.page = page
        self.searchField = page.locator(BookStoreSearch.SEARCH_INPUT)
        self.bookStoreCatalog = page.locator(BookStoreDisplay.BOOK_TBL)
        self.bookStoreProfileLogoutButton = page.locator(BookStoreUserProfile.LOGOUT_BTN)
        self.loggedInUser = page.locator(BookStoreUserProfile.AUTH_USER_VALUE)
        
    def checkUI(self):
        # BOOKSTORE SEARCH INPUT ON PROFILE PAGE
        expect(self.searchField).to_be_visible()
        expect(self.searchField).to_be_empty()
        expect(self.searchField).to_have_placeholder('Type to search')
        
        # BOOKSTORE LOGOUT BUTTON ON PROFILE PAGE
        expect(self.bookStoreProfileLogoutButton).to_be_visible()
        expect(self.bookStoreProfileLogoutButton).not_to_be_disabled()
        
        # BOOKSTORE LOGGED IN USER SHOWN ON PROFILE PAGE
        expect(self.loggedInUser).to_be_visible()
        expect(self.loggedInUser).to_contain_text(pd.demoQAUsn)
        
        # BOOKSTORE CATALOG ON PROFILE PAGE
        expect(self.bookStoreCatalog).to_be_visible
        