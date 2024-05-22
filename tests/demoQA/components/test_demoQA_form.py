import pytest
from playwright.sync_api import Page
from utils.data import DemoQA, ProjectData as pd
from components.demoQAComponentModels.demoQAForm import RegistrationPage


@pytest.mark.normal
class TestPracticeForm:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        registrationFormUrl = DemoQA.baseUrl+'/automation-practice-form'
        page.goto(registrationFormUrl)
        yield
    
    def test_registration_UI(self, page: Page):
        """Test that entire student registration form to spec"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.checkUI
        
    def test_successful_registration_form_submission(self, page: Page):
        """Test that student can successfully submit registration form"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.fname, pd.lname, pd.email, pd.tel, pd.birthday, pd.subj, pd.address)
        onRegistrationForm.confirmSuccessfulRegistration
        
    def test_unsuccessful_registration_form_submission(self, page: Page):
        """Test that validation occurs for blank registration form"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitBlankForm
        onRegistrationForm.confirmUnsuccessfulRegistration
        
    def test_mixed_character_inputs_at_registration_form_submission(self, page: Page):
        """Test for mixed characters at registration form""" 
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.mixedCharSet, pd.mixedCharSet, pd.mixedCharSet, pd.mixedCharSet, pd.birthday, pd.mixedCharSet, pd.mixedCharSet)
        onRegistrationForm.confirmUnsuccessfulRegistration
        
    def test_javascript_injection_at_registration_form_submission(self, page: Page):
        """Test for javascript vulnerability at registration form"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.jsInjection, pd.jsInjection, pd.jsInjection, pd.mixedCharSet, pd.birthday, pd.jsInjection, pd.jsInjection)
        onRegistrationForm.confirmUnsuccessfulRegistration
        
    def test_cross_site_script_injection_at_registration_form_submission(self, page: Page):
        """Test for javascript vulnerability using image tag at registration form""" 
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.xssImageTag, pd.xssImageTag, pd.xssImageTag, pd.xssImageTag, pd.xssImageTag, pd.xssImageTag, pd.xssImageTag)
        onRegistrationForm.confirmUnsuccessfulRegistration
        
    def test_script_injection_at_registration_form_submission(self, page: Page):
        """Test for javascript vulnerability using broken html at registration form"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.brokenHTML, pd.brokenHTML, pd.brokenHTML, pd.brokenHTML, pd.brokenHTML, pd.brokenHTML, pd.brokenHTML)
        onRegistrationForm.confirmUnsuccessfulRegistration

    def test_sql_injection_at_registration_form_submission(self, page: Page):
        """Test for SQL injection vulnerability at registration form"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.sqlInjection, pd.sqlInjection, pd.sqlInjection, pd.sqlInjection, pd.sqlInjection, pd.sqlInjection, pd.sqlInjection)
        onRegistrationForm.confirmUnsuccessfulRegistration    
        
    def test_unsuccessful_registration_form_submission_with_improper_email(self, page: Page):
        """Test that student cannot successfully submit registration form when email is invalid"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.fname, pd.lname, '.email@domain.com', pd.tel, pd.birthday, pd.subj, pd.address)
        onRegistrationForm.confirmUnsuccessfulRegistration   
        
    def test_unsuccessful_registration_form_submission_with_invalid_telephone(self, page: Page):
        """Test that student cannot successfully submit registration form when telephone is invalid"""
        
        onRegistrationForm = RegistrationPage(page)
        onRegistrationForm.submitForm(pd.fname, pd.lname, pd.email, 'phoneNumber', pd.birthday, pd.subj, pd.address)
        onRegistrationForm.confirmUnsuccessfulRegistration 