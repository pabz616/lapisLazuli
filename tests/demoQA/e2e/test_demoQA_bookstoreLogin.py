import pytest
import re
from playwright.sync_api import Page, expect
from demoQAUtils.data import ProjectData as pd
from demoQABookStore.demoQABookStoreLogin import BookStoreLoginPage as BookStoreLogin


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    bookStoreUrl = pd.baseUrl+'/login'
    page.goto(bookStoreUrl)
    yield


@pytest.mark.high
def test_BookStore_Login_UI(page: Page):
    """Test that entire bookstore login page is to spec"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.checkUI

    
def test_BookStore_Login_Is_Successful(page: Page):
    """Test bookstore login functionality - valid login"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, pd.demoQAPwd)
    expect(page).to_have_url(re.compile(pd.baseUrl+r'/profile'))
