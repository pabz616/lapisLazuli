import pytest
from playwright.sync_api import Page
from demoQAUtils.data import DemoQA
from api.demoQAClient.book_client import BooksClient
from api.demoQAAssertions import assertions as confirm


"""
PARAMETER POLLUTION
TARGET: Book Selection
GOAL: Ensure no vulnerabilities encountered when the url parameter is altered
"""

client = BooksClient()
bookSelectionUrl = DemoQA.baseUrl+'/books'

paramList = ["aaa", "", "!@#$%^&'", "<script>alert(1)</script>", "OR 1=1;##", "&url=https://mysite.com"]

 
@pytest.mark.security
@pytest.mark.high
def test_parameter_pollution(page: Page):    
    for params in paramList:         
        page.goto(bookSelectionUrl+f"?book={params}")
        response = client.get_searched_book()
        confirm.ok_response_status(response, 200), "should fail"
        # expect(response).not_to_be_ok(), "Vulnerability found! Attacker can manipulate the request and bypass security mechanisms"