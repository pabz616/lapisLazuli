import pytest
from playwright.sync_api import Page
from e2e.demoQAPages.demoQABookStoreLogin import BookStoreLoginPage as BookStoreLogin
from e2e.demoQAPages.demoQABookStoreRegistration import BookStoreRegistrationPage as Registration
from e2e.demoQAPages.demoQABookStore import BookStoreDisplayPage as onBookstore
from demoQAUtils.data import DemoQA, ProjectData as pd


"""
SQL INJECTION
TARGET: Form inputs
GOAL: Ensure no vulnerabilities encountered for the target input
"""


@pytest.mark.security
class TestSQLInjection:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(DemoQA.baseUrl)
        yield
        
    def test_BookStore_SQL_Injection_In_URL(self, page: Page):
        page.goto(DemoQA.baseUrl + '/books?book=9781449325862' + pd.sqlInjection2)
        onBookstore.confirmPageRedirectionIsUnsuccessful
 
 
@pytest.mark.security
class TestSQLInjectionInSearch:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(DemoQA.baseUrl)
        yield
        
    def test_SQL_Injection_In_Search_Input(self, page: Page):
        pass


@pytest.mark.security
class TestSQLInjectionAtLogin:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(DemoQA.baseUrl+'/login')
        yield
                
    def test_SQL_Injection_At_Login_Username(self, page: Page):
        """Test SQL injection in query parameter should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(pd.sqlInjection, 'password123')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation

    def test_SQL_Injection_At_Login_Password(self, page: Page):
        """Test SQL injection at password should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
    
    def test_SQL_Injection_using_NULL_BYTE(self, page: Page):
        """Test SQL injection employing a Null Byte at password should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, 'password/%')
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
    def test_SQL_Injection_with_URL_ENCODED_STRING_At_Login(self, page: Page):
        """Test SQL injection using URL ENCODING at login should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection_endcoded)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation
        
    def test_SQL_Injection_with_LOWERCASE_PAYLOAD_At_Login(self, page: Page):
        """Test SQL injection using URL ENCODING at login should fail"""
        
        onBookStoreLogin = BookStoreLogin(page)
        onBookStoreLogin.submitLogin(DemoQA.usn, pd.sqlInjection_lowercase)
        onBookStoreLogin.confirmInvalidLoginCredentialsValidation


@pytest.mark.security
class TestSQLInjectionAtRegistration:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        page.goto(DemoQA.baseUrl+'/register')
        yield

    def test_SQL_Injection_At_Registration(self, page: Page):
        """Test that bookstore validation occurs if user exists"""
        onBookStoreRegistrationPage = Registration(page)

        first_name = 'tester1'
        last_name = 'tester1'
        username = 'tester1' + pd.sqlInjection2 + '*@example.com'
        password = 'Password123!'
       
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
        onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed
        
    def test_SQL_Injection_using_NULL_BYTE_At_Registration(self, page: Page):
        """Test that registration fails when a sql injection using a null byte is attempted"""
        onBookStoreRegistrationPage = Registration(page)

        first_name = 'hack%00'
        last_name = 'hack\x00'
        username = 'tester1' + pd.sqlInjection2 + '*@example.com'
        password = 'Password123!'
       
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
        onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed