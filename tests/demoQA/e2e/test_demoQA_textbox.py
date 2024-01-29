import pytest
from playwright.sync_api import Page
from demoQAModels.demoQAText import TextBoxPage
from demoQAUtils.data import DemoQATextForm


@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    textBoxPageUrl = DemoQATextForm.baseUrl+'/text-box'
    page.goto(textBoxPageUrl)
    yield


@pytest.mark.normal
def test_textbox_UI(page: Page):
    """Test that entire textbox page is to spec"""
    onTextBoxPage = TextBoxPage(Page)
    onTextBoxPage.checkUI()