import pytest
from playwright.sync_api import Page
from utils.data import ProjectData as pd, DemoQA
from e2e.demoQABookStore.demoQABookStoreSearch import BookStoreSearchPage as Search
from api.demoQAClient.book_client import BooksClient

"""
STORED CROSS SITE SCRIPT INJECTION
TARGET: Search Input
GOAL: Enter input on the front end confirm it is not in the response; javascript is not executed; input is sanitized
"""

client = BooksClient()


@pytest.mark.security
@pytest.mark.high
class TestStoredCrossSiteScriptInjection:
    @pytest.fixture(scope="function", autouse=True)
    def before_each(self, page: Page):
        bookStoreUrl = DemoQA.baseUrl+'/books'
        page.goto(bookStoreUrl)
        yield

    def test_stored_xss_using_simple_string(self, page: Page):
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.simpleString)
        onBookStoreSearch.confirmXssIsNotStored(pd.simpleString, None)

    def test_stored_xss_using_html(self, page: Page):    
        onBookStoreSearch = Search(page)
        sanitized_element = "&gt;"
        onBookStoreSearch.enterSearchTerm(pd.simpleHTML)
        onBookStoreSearch.confirmXssIsNotStored(pd.simpleHTML, sanitized_element)
        
    def test_stored_xss_using_js_injection(self, page: Page):    
        onBookStoreSearch = Search(page)
        sanitized_element = "<script>"
        onBookStoreSearch.enterSearchTerm(pd.jsInjection)
        onBookStoreSearch.confirmXssIsNotStored(pd.jsInjection, sanitized_element)

    def test_stored_xss_using_anchor_tag(self, page: Page):    
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.anchorTag)
        onBookStoreSearch.confirmXssIsNotStored(pd.anchorTag, None)

    def test_stored_xss_using_character_escape_sequence(self, page: Page):
        onBookStoreSearch = Search(page)
        onBookStoreSearch.enterSearchTerm(pd.escapeSequence)
        onBookStoreSearch.confirmXssIsNotStored(pd.escapeSequence, None)
        
    def test_stored_xss_using_event_attribute_injection(self, page: Page):
        onBookStoreSearch = Search(page)
        sanitized_element = "onerror"
        onBookStoreSearch.enterSearchTerm(pd.xssImageTag)
        onBookStoreSearch.confirmXssIsNotStored(pd.xssImageTag, sanitized_element)
  
    def test_stored_xss_using_script_tag_variation(self, page: Page):
        onBookStoreSearch = Search(page)
        sanitized_element = "&lt;script&gt;"
        onBookStoreSearch.enterSearchTerm(pd.scriptTagVariation)
        onBookStoreSearch.confirmXssIsNotStored(pd.scriptTagVariation, sanitized_element)
 
    def test_stored_xss_using_encoding_bypass(self, page: Page):
        onBookStoreSearch = Search(page)
        sanitized_element = "&lt;script&gt;"
        onBookStoreSearch.enterSearchTerm(pd.encoding)
        onBookStoreSearch.confirmXssIsNotStored(pd.encoding, sanitized_element)