import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd, DemoQA
from e2e.demoQAPages.demoQABookStoreRegistration import BookStoreRegistrationPage as Registration

from faker import Faker
fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
username = fake.color_name()+str(fake.port_number())+'!@'


@pytest.mark.high
class TestBookStoreRegistration:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        bookStoreUrl = DemoQA.baseUrl+'/register'
        page.goto(bookStoreUrl)
        yield

    def test_BookStore_Registration_UI(self, page: Page):
        """Test that entire bookstore registration form displayed is to spec"""
        onBookStoreRegistrationPage = Registration(page)
        onBookStoreRegistrationPage.checkUI
        
    def test_BookStore_Successful_Registration(self, page: Page):
        """Test that bookstore new user registration is successful"""
        
        password = 'Password123!'
        onBookStoreRegistrationPage = Registration(page)
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
        onBookStoreRegistrationPage.confirmSuccessfulRegistration
        
    def test_BookStore_Registration_Duplicate_Account_Validation(self, page: Page):
        """Test that bookstore validation occurs if user exists"""

        sampleUsr = 'test'
        first_name = sampleUsr
        last_name = sampleUsr
        username = sampleUsr
        password = 'Password123!'
        
        onBookStoreRegistrationPage = Registration(page)
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
        onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed
    
    def test_BookStore_Registration_Required_Fields_Validation(self, page: Page):
        """Test that validation for required field occurs on bookstore registration"""

        first_name = ''
        last_name = ''
        username = ''
        password = ''

        onBookStoreRegistrationPage = Registration(page)
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
        onBookStoreRegistrationPage.confirmRequiredInputValidationState 
    
    def test_BookStore_Registration_Weak_Password_Validation(self, page: Page):
        """Test that validation occurs on bookstore registration for weak password"""

        onBookStoreRegistrationPage = Registration(page)
        
        # SHORT PASSWORD
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, fake.color_name())
        onBookStoreRegistrationPage.confirmPasswordErrorMessage
        
        # ALL NUMBERS
        onBookStoreRegistrationPage.clearForm
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, str(fake.port_number()))
        onBookStoreRegistrationPage.confirmPasswordErrorMessage
        
        # FOREIGN CHARACTER
        onBookStoreRegistrationPage.clearForm
        onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, pd.sanskrit)
        onBookStoreRegistrationPage.confirmPasswordErrorMessage
