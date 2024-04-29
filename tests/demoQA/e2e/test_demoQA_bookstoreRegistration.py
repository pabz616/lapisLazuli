import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd

from demoQABookStore.demoQABookStoreRegistration import BookStoreRegistrationPage as Registration

from faker import Faker
fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
username = fake.color_name()+str(fake.port_number())+'!@'


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

    password = 'Password123!'
    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
    onBookStoreRegistrationPage.confirmSuccessfulRegistration
    
    
def test_BookStore_Registration_Duplicate_Account_Validation(page: Page):
    """Test that bookstore validation occurs if user exists"""

    sampleUsr = 'test'
    first_name = sampleUsr
    last_name = sampleUsr
    username = sampleUsr
    password = 'Password123!'
    
    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
    onBookStoreRegistrationPage.confirmErrorMessageForexisting_userIsDisplayed
   
   
@pytest.mark.normal
def test_BookStore_Registration_Required_Fields_Validation(page: Page):
    """Test that validation for required field occurs on bookstore registration"""

    first_name = ''
    last_name = ''
    username = ''
    password = ''

    onBookStoreRegistrationPage = Registration(page)
    onBookStoreRegistrationPage.completeRegistrationForm(first_name, last_name, username, password)
    onBookStoreRegistrationPage.confirmRequiredInputValidationState 
 
    
@pytest.mark.normal
def test_BookStore_Registration_Weak_Password_Validation(page: Page):
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
