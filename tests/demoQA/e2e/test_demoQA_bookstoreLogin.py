import pytest
import re
from playwright.sync_api import Page, expect
from demoQAUtils.data import ProjectData as pd
from demoQABookStore.demoQABookStoreLogin import BookStoreLoginPage as BookStoreLogin
from demoQABookStore.demoQABookStoreProfile import BookStoreProfilePage as BookStoreProfile


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
    onBookStoreProfile = BookStoreProfile(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, pd.demoQAPwd)
    
    expect(page).to_have_url(re.compile(pd.baseUrl+r'/profile'))
    onBookStoreProfile.checkUI
    

def test_BookStore_Login_Required_Fields(page: Page):
    """Test bookstore login functionality - validation for required fields"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin('', '')
    onBookStoreLogin.confirmRequiredFieldsValidation


def test_BookStore_Login_Invalid_Username_Validation(page: Page):
    """Test bookstore login functionality - validation for invalid username submitted"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.mixedCharSet, pd.demoQAPwd)
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    

def test_BookStore_Login_Invalid_Password_Validation(page: Page):
    """Test bookstore login functionality - validation for invalid password submitted"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, pd.mixedCharSet)
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
 
    
def test_BookStore_Login_Short_Password_Validation(page: Page):
    """Test bookstore login functionality - validation for short password submitted"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, 'pass')
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    
    
def test_BookStore_Login_Common_Login_Credentials(page: Page):
    """Test bookstore login functionality - common login like 'admin/admin' or 'admin/password123' should fail"""
    
    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin('admin', 'password123')
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    
    
def test_BookStore_Login_JS_Injection_At_Username(page: Page):
    """Test bookstore login functionality - JS injection at username should fail"""

    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.jsInjection, 'password123')
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation

    
def test_BookStore_Login_JS_Injection_At_Password(page: Page):
    """Test bookstore login functionality - JS injection at password should fail"""

    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, pd.jsInjection)
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    
    
def test_BookStore_Login_SQL_Injection_At_Username(page: Page):
    """Test bookstore login functionality - SQL injection at username should fail"""

    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.sqlInjection, 'password123')
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation

    
def test_BookStore_Login_SQL_Injection_At_Password(page: Page):
    """Test bookstore login functionality - SQL injection at password should fail"""

    onBookStoreLogin = BookStoreLogin(page)
    onBookStoreLogin.submitLogin(pd.demoQAUsn, pd.sqlInjection)
    onBookStoreLogin.confirmInvalidLoginCredentialsValidation
