import pytest
from playwright.sync_api import Page, expect
from demoQAUtils.data import ProjectData as pd, DemoQA
from e2e.demoQAPages.demoQABookStoreLogin import BookStoreLoginPage as BookStoreLogin
from e2e.demoQAPages.demoQABookStoreProfile import BookStoreProfilePage as BookStoreProfile


bookStoreLoginUrl = DemoQA.baseUrl+'/login'
profileUrl = DemoQA.baseUrl+'/profile'


@pytest.mark.high
class TestBookStoreLogin:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(bookStoreLoginUrl)
        yield

    def test_BookStore_Login_UI(self, page: Page):
        """Test that entire bookstore login page is to spec"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.checkUI

    def test_BookStore_Login_Is_Successful(self, page: Page):
        """Test bookstore login functionality - valid login"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreProfile = BookStoreProfile(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, DemoQA.pwd)
        expect(page).to_have_url(profileUrl)
        onBookStoreProfile.checkUI
        
    def test_BookStore_Login_Required_Fields(self, page: Page):
        """Test bookstore login functionality - validation for required fields"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin('', '')
        onBookStoreLogin.confirmRequiredFieldsValidation

    def test_BookStore_Login_Invalid_Username_Validation(self, page: Page):
        """Test bookstore login functionality - validation for invalid username submitted"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(pd.mixedCharSet, DemoQA.pwd)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
    def test_BookStore_Login_Invalid_Password_Validation(self, page: Page):
        """Test bookstore login functionality - validation for invalid password submitted"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.mixedCharSet)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
    def test_BookStore_Login_Short_Password_Validation(self, page: Page):
        """Test bookstore login functionality - validation for short password submitted"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, 'pass')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
                
    def test_BookStore_Login_Common_Login_Credentials(self, page: Page):
        """Test bookstore login functionality - common login like 'admin/admin' or 'admin/password123' should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin('admin', 'password123')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
    def test_BookStore_Login_JS_Injection_At_Username(self, page: Page):
        """Test bookstore login functionality - JS injection at username should fail"""

        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(pd.jsInjection, 'password123')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation

    def test_BookStore_Login_JS_Injection_At_Password(self, page: Page):
        """Test bookstore login functionality - JS injection at password should fail"""

        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.jsInjection)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
                
    def test_BookStore_Login_SQL_Injection_At_Username(self, page: Page):
        """Test bookstore login functionality - SQL injection at username should fail"""

        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(pd.sqlInjection, 'password123')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation

    def test_BookStore_Login_SQL_Injection_At_Password(self, page: Page):
        """Test bookstore login functionality - SQL injection at password should fail"""

        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
