import pytest
from playwright.sync_api import Page
from components.demoQAComponentModels.demoQARadioButtons import RadioButtonPage
from demoQAUtils.data import DemoQA


@pytest.mark.normal
# use --browser-channel "chrome" to run tests in chrome, not chromium
class TestRadioButton:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        textBoxPageUrl = DemoQA.baseUrl+'/radio-button'
        page.goto(textBoxPageUrl)
        yield

    def test_radiobutton_UI(self, page: Page):
        """Test that entire radio buttons page is to spec"""
        
        onRadioButtonPage = RadioButtonPage(page)
        onRadioButtonPage.checkUI

    def test_message_for_YES_answer(self, page: Page):
        """Test for the message when the answer to the displayed question is 'YES'"""
        
        onRadioButtonPage = RadioButtonPage(page)
        onRadioButtonPage.selectYes
        onRadioButtonPage.checkMessage('You have selected Yes')

    def test_message_for_IMPRESSIVE_answer(self, page: Page):
        """Test for the message when the answer to the displayed question is 'IMPRESSIVE'"""
        
        onRadioButtonPage = RadioButtonPage(page)
        onRadioButtonPage.selectImpressive
        onRadioButtonPage.checkMessage('You have selected Impressive')

    def test_message_for_NO_answer(self, page: Page):
        """Test for the message when the answer to the displayed question is 'No'"""
        onRadioButtonPage = RadioButtonPage(page)
        onRadioButtonPage.selectNo
        onRadioButtonPage.checkMessage('You have selected No')