import pytest
from playwright.sync_api import Page
from demoQAUtils.data import ProjectData as pd, DemoQA
from demoQABookStore.demoQABookStoreSearch import BookStoreSearchPage as Search

"""
REFLECTED CROSS SITE SCRIPT INJECTION
TARGET: Search Input
GOAL: Ensure these characters are filtered <>’’&””
"""


@pytest.mark.security
@pytest.mark.high
@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    bookStoreUrl = DemoQA.baseUrl+'/books'
    page.goto(bookStoreUrl)
    yield


def test_xss_using_html_tag(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.simpleHTML)
    onBookStoreSearch.confirmNoAlertShown

    
def test_xss_using_html_entities(page: Page):
    """Test by replacing < and > with HTML entities &lt; and &gt;"""
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.htmlEntities)
    onBookStoreSearch.confirmNoAlertShown


def test_xss_using_image_tag(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.xssImageTag)
    onBookStoreSearch.confirmNoAlertShown
    

def test_xss_with_a_character_escape_sequence(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.escapeSequence)
    onBookStoreSearch.confirmNoAlertShown
    
    
def test_xss_with_lower_case_script(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.jsInjection)
    onBookStoreSearch.confirmNoAlertShown


def test_xss_with_upper_case_script(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.jsInjectionAllCaps)
    onBookStoreSearch.confirmNoAlertShown


def test_xss_with_double_encoding(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.encoding)
    onBookStoreSearch.confirmNoAlertShown
 
 
def test_xss_with_recursive_filters(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm("-prompt()-")
    onBookStoreSearch.confirmNoAlertShown
 

def test_xss_with_anchor_tags_no_whitespace(page: Page):
    onBookStoreSearch = Search(page)
    onBookStoreSearch.enterSearchTerm(pd.anchorTag)
    onBookStoreSearch.confirmNoAlertShown
        