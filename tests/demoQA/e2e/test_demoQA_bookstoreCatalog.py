import pytest
import re
from playwright.sync_api import Page, expect
from demoQAUtils.data import ProjectData as pd
from demoQABookStore.demoQABookStore import BookStoreDisplayPage as BookStore


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    bookStoreUrl = pd.baseUrl+'/books'
    page.goto(bookStoreUrl)
    yield


@pytest.mark.high
def test_BookStore_UI(page: Page):
    """Test that entire bookstore displayed catalog page is to spec"""
    
    onBookStore = BookStore(page)
    onBookStore.checkBookStoreSearchUI
    onBookStore.checkBookStoreLoginCTA
    onBookStore.checkBookStoreCatalogUI
    onBookStore.checkBookStoreCatalogPagination


@pytest.mark.high    
def test_BookStore_BrowseSelection(page: Page):
    """Test that a user can select a book and navigate to the details page"""
    
    onBookStore = BookStore(page)
    onBookStore.navigateToDetailsView
    expect(page).to_have_url(re.compile(pd.baseUrl+r'/books'))