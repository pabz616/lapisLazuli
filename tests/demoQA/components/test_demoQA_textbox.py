import pytest
from playwright.sync_api import Page
from demoQAComponentModels.demoQAText import TextBoxPage
from demoQAUtils.data import ProjectData as pd, DemoQATextForm as testData, InvalidEmailAddresses as testEmails


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.normal
# use --browser-channel "chrome" to run tests in chrome, not chromium
class TestTextInputs:
    def before_each(page: Page):
        textBoxPageUrl = pd.baseUrl+'/text-box'
        page.goto(textBoxPageUrl)
        yield

    def test_textbox_UI(page: Page):
        """Test that entire textbox page is to spec"""
        
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.checkUI()

    def test_submit_textbox_form(page: Page):
        """Test that form submission is successful"""
        
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResultsAreVisible(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    def test_required_validation_occurs_for_missing_name(page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm('', testData.cEmail, testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResultsAreVisible(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    def test_required_validation_occurs_error_for_missing_email(page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(
            testData.cName, '', testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResultsAreVisible(
            testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    def test_required_validation_occurs_error_for_missing_current_address(page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(testData.cName, testData.cEmail, '', '')
        onTextBoxPage.confirmResultsAreVisible(
            testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    def test_validation_occurs_for_invalid_email_address(page: Page):
        onTextBoxPage = TextBoxPage(page)
        for email in testEmails.badEmails:
            onTextBoxPage.fillForm(testData.cName, f"{email}", testData.cAddress, testData.cPermAddress)
            onTextBoxPage.confirmEmailInputErrorState()

