""" BOOK STORE LANDING """

from demoQALocators.pageElements import BookStoreDisplay, BookStoreSearch, BookStoreLogin
from playwright.sync_api import expect


class BookStoreDisplayPage:
    def __init__(self, page):
        self.page = page
        self.searchField = page.locator(BookStoreSearch.SEARCH_INPUT)
        self.loginButton = page.locator(BookStoreLogin.LOGIN_BTN)
        self.bookStoreCatalog = page.locator(BookStoreDisplay.BOOK_TBL)
        
        self.bookStoreCatalogHeader = page.locator(BookStoreDisplay.BOOK_TBL_HEADER)
        self.bookStoreCatalogContent = page.locator(BookStoreDisplay.BOOK_TBL_BODY)
        self.bookStoreCatalog_Row1_bookImage = page.locator(BookStoreDisplay.BOOK_TBL_R1_IMG)
        self.bookStoreCatalog_Row1_bookTitle = page.locator(BookStoreDisplay.BOOK_TBL_R1_TITLE)
        self.bookSelected = page.locator(BookStoreDisplay.BOOK_1)
        self.bookStoreCatalog_Row1_bookAuthor = page.locator(BookStoreDisplay.BOOK_TBL_R1_AUTHOR)
        self.bookStoreCatalog_Row1_bookPublisher = page.locator(BookStoreDisplay.BOOK_TBL_R1_PUBLISHER)
        
        self.bookStoreCatalogPagination = page.locator(BookStoreDisplay.PAGINATION)
        self.bookStoreCatalogPagination_PreviousBtn = page.locator(BookStoreDisplay.PREVIOUS_BTN)
        self.bookStoreCatalogPagination_NextBtn = page.locator(BookStoreDisplay.NEXT_BTN)
        self.bookStoreCatalogPagination_Count = page.locator(BookStoreDisplay.PAGE_COUNT)
        self.bookStoreCatalogPagination_Input = page.locator(BookStoreDisplay.PAGE_INPUT)
        self.bookStoreCatalogPagination_Select = page.locator(BookStoreDisplay.PAGE_SELECT)

    def checkBookStoreSearchUI(self):
        # BOOKSTORE SEARCH INPUT ON LANDING PAGE
        expect(self.searchField).to_be_visible
        expect(self.searchField).to_be_empty

    def checkBookStoreLoginCTA(self):
        # BOOKSTORE LOGIN CTA ON LANDING PAGE
        expect(self.loginButton).to_be_visible
        expect(self.loginButton).to_have_text('Login')
        expect(self.loginButton).to_be_enabled
        
    def checkBookStoreCatalogUI(self):
        
        # BOOKSTORE LANDING PAGE
        expect(self.bookStoreCatalog).to_be_visible
        expect(self.bookStoreCatalogHeader).to_be_visible
        expect(self.bookStoreCatalogContent).to_be_visible    
        
        expect(self.bookStoreCatalog_Row1_bookImage).to_be_visible
        
        expect(self.bookStoreCatalog_Row1_bookTitle).to_be_visible
        expect(self.bookStoreCatalog_Row1_bookTitle).to_have_text('Git Pocket Guide')
        expect(self.bookStoreCatalog_Row1_bookTitle).not_to_be_disabled
        
        expect(self.bookStoreCatalog_Row1_bookAuthor).to_be_visible
        expect(self.bookStoreCatalog_Row1_bookAuthor).to_have_text('Richard E. Silverman')
        
        expect(self.bookStoreCatalog_Row1_bookPublisher).to_be_visible
        expect(self.bookStoreCatalog_Row1_bookPublisher).to_have_text("O'Reilly Media")            
   
    def checkBookStoreCatalogPagination(self):
        expect(self.bookStoreCatalogPagination).to_be_visible
        expect(self.bookStoreCatalogPagination_PreviousBtn).to_be_visible
        expect(self.bookStoreCatalogPagination_PreviousBtn).to_have_text('Previous')
        
        expect(self.bookStoreCatalogPagination_NextBtn).to_be_visible
        expect(self.bookStoreCatalogPagination_NextBtn).to_have_text('Next')
        
        expect(self.bookStoreCatalogPagination_Count).to_be_visible
        expect(self.bookStoreCatalogPagination_Input).to_be_visible
        expect(self.bookStoreCatalogPagination_Input).to_be_have_value('1')
        expect(self.bookStoreCatalogPagination_Select).to_be_visible
        
    def navigateToDetailsView(self):
        self.bookSelected.click()