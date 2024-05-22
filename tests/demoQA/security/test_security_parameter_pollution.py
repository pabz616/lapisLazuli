import pytest
from playwright.sync_api import Page
from demoQABookStore.demoQABookStore import BookStoreDisplayPage as onBookstore
from utils.data import DemoQA


"""
PARAMETER POLLUTION
TARGET: Book Selection
GOAL: Ensure no vulnerabilities encountered when the url parameter is altered
"""

bookSelectionUrl = DemoQA.baseUrl+'/books'


@pytest.mark.security
@pytest.mark.high
def test_parameter_pollution(page: Page):    
    for params in DemoQA.parameterList:         
        page.goto(bookSelectionUrl+f"?book={params}")
        onBookstore.confirmPageRedirectionIsUnsuccessful
