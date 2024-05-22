import pytest
from playwright.sync_api import Page
from components.demoQAComponentModels.demoQAText import TextBoxPage
from utils.data import DemoQA, DemoQATextForm as testData, InvalidEmailAddresses as testEmails


@pytest.mark.normal
class TestTextInputs:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        textBoxPageUrl = DemoQA.baseUrl+'/text-box'
        page.goto(textBoxPageUrl)
        yield

    def test_textbox_UI(self, page: Page):
        """Test that entire textbox page is to spec"""
        
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.checkUI()

    def test_submit_textbox_form(self, page: Page):
        """Test that form submission is successful"""
        
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResults(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    @pytest.mark.skip(reason="Bug! No validation occurred for name input")
    def test_required_validation_occurs_for_missing_name(self, page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm('', testData.cEmail, testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResults(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    @pytest.mark.skip(reason="Bug! No validation occurred for email input")
    def test_required_validation_occurs_error_for_missing_email(self, page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(
            testData.cName, '', testData.cAddress, testData.cPermAddress)
        onTextBoxPage.confirmResults(
            testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    @pytest.mark.skip(reason="Bug! No validation occurred for current address")
    def test_required_validation_occurs_error_for_missing_current_address(self, page: Page):
        onTextBoxPage = TextBoxPage(page)
        onTextBoxPage.fillForm(testData.cName, testData.cEmail, '', '')
        onTextBoxPage.confirmResults(
            testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)

    def test_validation_occurs_for_invalid_email_address(self, page: Page):
        onTextBoxPage = TextBoxPage(page)
        for email in testEmails.badEmails:
            onTextBoxPage.fillForm(testData.cName, f"{email}", testData.cAddress, testData.cPermAddress)
            onTextBoxPage.confirmEmailInputErrorState()

