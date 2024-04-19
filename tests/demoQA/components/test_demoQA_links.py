import pytest
from playwright.sync_api import Page
from demoQAModels.demoQALinks import LinksPage
from demoQAUtils.data import ProjectData, DemoQAResponseMsg as statusMsg

@pytest.fixture(scope="function", autouse=True)
# use --browser-channel "chrome" to run tests in chrome, not chromium
def before_each(page: Page):
    textBoxPageUrl = ProjectData.baseUrl+'/links'
    page.goto(textBoxPageUrl)
    yield
    

@pytest.mark.normal
def test_links_UI(page: Page):
    """Test that entire links page is to spec"""
    onLinksPage = LinksPage(page)
    onLinksPage.checkUI

# checking the link text, element id, and api response message
def test_API_Response_Created(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Created', 'created', statusMsg.created)
        
def test_API_Response_No_Content(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('No Content', 'no-content', statusMsg.noContent)

def test_API_Response_Moved(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Moved', 'moved', statusMsg.moved)    

def test_API_Response_Bad_Request(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Bad Request', 'bad-request', statusMsg.badRequest)    

def test_API_Response_Unauthorized(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Unauthorized', 'unauthorized', statusMsg.unauthorized) 
 
def test_API_Response_Forbidden(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Forbidden', 'forbidden', statusMsg.forbidden)

def test_API_Response_Not_Found(page: Page):
    onLinksPage = LinksPage(page)
    onLinksPage.checkLink('Not Found', 'invalid-url', statusMsg.invalidUrl)