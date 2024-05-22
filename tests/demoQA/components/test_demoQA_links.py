import pytest
from playwright.sync_api import Page
from components.demoQAComponentModels.demoQALinks import LinksPage
from utils.data import DemoQA, DemoQAResponseMsg as statusMsg


# use --browser-channel "chrome" to run tests in chrome, not chromium
class TestLinks:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        textBoxPageUrl = DemoQA.baseUrl+'/links'
        page.goto(textBoxPageUrl)
        yield        

    def test_links_UI(self, page: Page):
        """Test that entire links page is to spec"""
        
        onLinksPage = LinksPage(page)
        onLinksPage.checkUI

    def test_API_Response_Created(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Created', 'created', statusMsg.created)
            
    def test_API_Response_No_Content(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('No Content', 'no-content', statusMsg.noContent)

    def test_API_Response_Moved(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Moved', 'moved', statusMsg.moved)    

    def test_API_Response_Bad_Request(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Bad Request', 'bad-request', statusMsg.badRequest)    

    def test_API_Response_Unauthorized(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Unauthorized', 'unauthorized', statusMsg.unauthorized) 

    def test_API_Response_Forbidden(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Forbidden', 'forbidden', statusMsg.forbidden)

    def test_API_Response_Not_Found(self, page: Page):
        onLinksPage = LinksPage(page)
        onLinksPage.checkLink('Not Found', 'invalid-url', statusMsg.invalidUrl)