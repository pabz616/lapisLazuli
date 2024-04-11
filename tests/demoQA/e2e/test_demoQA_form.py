import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd
from demoQAModels.demoQAForm import RegistrationPage


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    registrationFormUrl = pd.baseUrl+'/automation-practice-form'
    page.goto(registrationFormUrl)
    yield
    
    
@pytest.mark.normal
def test_registration_UI(page: Page):
    """Test that entire student registration form to spec"""
    onRegistrationForm = RegistrationPage(page)
    onRegistrationForm.checkUI
    
    
@pytest.mark.normal
def test_registration_form_submission(page: Page):
    """Test that student can successfully submit registration form"""
    onRegistrationForm = RegistrationPage(page)
    
    onRegistrationForm.submitForm(pd.fname, pd.lname, pd.email, pd.tel, pd.birthday, pd.subj, pd.address)
    onRegistrationForm.confirmSuccessfulRegistration