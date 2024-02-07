import pytest
from playwright.sync_api import Page
from demoQAModels.demoQARadioButtons import RadioButtonPage
from demoQAUtils.data import ProjectData


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    textBoxPageUrl = ProjectData.baseUrl+'/radio-button'
    page.goto(textBoxPageUrl)
    yield
    
@pytest.mark.normal
def test_radiobutton_UI(page: Page):
    """Test that entire textbox page is to spec"""
    onRadioButtonPage = RadioButtonPage(page)
    onRadioButtonPage.checkUI
    
@pytest.mark.normal
def test_message_for_YES_answer(page: Page):
    """Test for the message when the answer to the displayed question is 'YES'"""
    onRadioButtonPage = RadioButtonPage(page)
    onRadioButtonPage.selectYes
    onRadioButtonPage.checkMessage('You have selected Yes')
    
@pytest.mark.normal
def test_message_for_IMPRESSIVE_answer(page: Page):
    """Test for the message when the answer to the displayed question is 'IMPRESSIVE'"""
    onRadioButtonPage = RadioButtonPage(page)
    onRadioButtonPage.selectImpressive
    onRadioButtonPage.checkMessage('You have selected Impressive')
      
@pytest.mark.normal
def test_message_for_NO_answer(page: Page):
    """Test for the message when the answer to the displayed question is 'No'"""
    onRadioButtonPage = RadioButtonPage(page)
    onRadioButtonPage.selectNo
    onRadioButtonPage.checkMessage('You have selected No')