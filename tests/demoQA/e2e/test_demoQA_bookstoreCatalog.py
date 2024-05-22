import pytest
from playwright.sync_api import Page, expect
from utils.data import DemoQA
from e2e.demoQAPages.demoQABookStore import BookStoreDisplayPage as BookStore

bookStoreUrl = DemoQA.baseUrl+'/books'


@pytest.mark.high
class TestBookStoreCatalog:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(bookStoreUrl)
        yield

    def test_BookStore_UI(self, page: Page):
        """Test that entire bookstore displayed catalog page is to spec"""
        
        onBookStore = BookStore(page)
        onBookStore.checkBookStoreSearchUI
        onBookStore.checkBookStoreLoginCTA
        onBookStore.checkBookStoreCatalogUI
        onBookStore.checkBookStoreCatalogPagination

    @pytest.mark.skip(reason="Site fails to load product details page")
    def test_BookStore_BrowseSelection(self, page: Page):
        """Test that a user can select a book and navigate to the details page"""
        
        onBookStore = BookStore(page)
        onBookStore.navigateToDetailsView
        expect(page).to_have_url(bookStoreUrl+'?book=9781449325862')
