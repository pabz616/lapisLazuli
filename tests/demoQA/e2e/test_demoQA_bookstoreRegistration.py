import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd
from demoQABookStore.demoQABookStore import BookStoreDisplayPage as Home
from demoQABookStore.demoQABookStoreLogin import BookStoreLoginPage as Login
from demoQABookStore.demoQABookStoreSignUp import BookStoreRegistrationPage as Registration


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    bookStoreUrl = pd.baseUrl+'/register'
    page.goto(bookStoreUrl)
    yield


@pytest.mark.high
def test_BookStore_Registration_UI(page: Page):
    """Test that entire bookstore registration form displayed is to spec"""
    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.checkUI
       

@pytest.mark.normal
def test_BookStore_Successful_Registration(page: Page):
    """Test that bookstore new user registration is successful"""
    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.completeRegistrationForm
    onBookStoreRegistrationPage.confirmSuccessfulRegistration
   
    
@pytest.mark.normal
def test_BookStore_UnSuccessful_Registration(page: Page):
    
    """Test that bookstore new user registration with improper data is not successful"""
    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.completeRegistrationForm
    onBookStoreRegistrationPage.confirmErrorMessage
    
#TODO Test required fields, invalid data, weak username