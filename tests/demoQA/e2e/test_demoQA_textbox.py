import pytest
from playwright.sync_api import Page
from demoQAModels.demoQAText import TextBoxPage
from demoQAUtils.data import DemoQATextForm as testData


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    textBoxPageUrl = testData.baseUrl+'/text-box'
    page.goto(textBoxPageUrl)
    yield


@pytest.mark.normal
def test_textbox_UI(page: Page):
    """Test that entire textbox page is to spec"""
    onTextBoxPage = TextBoxPage(page)
    onTextBoxPage.checkUI()


@pytest.mark.normal
def test_submit_textbox_form(page: Page):
    """Test that form submission is successful"""
    onTextBoxPage = TextBoxPage(page)
    onTextBoxPage.fillForm(testData.cName, testData.cEmail,
                           testData.cAddress, testData.cPermAddress)
    onTextBoxPage.confirmResultsAreVisible(
        testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)


@pytest.mark.normal
def test_required_validation_occurs_for_missing_name(page: Page):
    onTextBoxPage = TextBoxPage(page)
    onTextBoxPage.fillForm('', testData.cEmail, testData.cAddress, testData.cPermAddress)
    onTextBoxPage.confirmResultsAreVisible(testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)


@pytest.mark.normal
def test_required_validation_occurs_error_for_missing_email(page: Page):
    onTextBoxPage = TextBoxPage(page)
    onTextBoxPage.fillForm(
        testData.cName, '', testData.cAddress, testData.cPermAddress)
    onTextBoxPage.confirmResultsAreVisible(
        testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)


@pytest.mark.normal
def test_required_validation_occurs_error_for_missing_current_address(page: Page):
    onTextBoxPage = TextBoxPage(page)
    onTextBoxPage.fillForm(testData.cName, testData.cEmail, '', '')
    onTextBoxPage.confirmResultsAreVisible(
        testData.cName, testData.cEmail, testData.cAddress, testData.cPermAddress)


@pytest.mark.normal
def test_validation_occurs_for_invalid_email_address(page: Page):
    badEmails = ['badEmail', 'email.domain.com', '@domain.com',
                           '#@%^%#$@#$@#.com', 'email@domain.com (Joe Smith)', 'email@domain@domain.com', '.email@domain.com',
                           'email.@domain.com', 'email..email@domain.com', 'あいうえお@domain.com', 'email@-domain.com', 'email@.domain.com',
                           'email@111.222.333.44444', 'email@domain..com']

    onTextBoxPage = TextBoxPage(page)
    
    invalidEmailAddress = [emails for emails in badEmails]
    onTextBoxPage.fillForm(testData.cName, invalidEmailAddress, testData.cAddress, testData.cPermAddress)
    onTextBoxPage.confirmEmailInputErrorState()
