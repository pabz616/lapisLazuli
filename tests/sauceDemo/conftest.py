import pytest
from playwright.sync_api import sync_playwright, Page, expect

from sauceUtils.data import SauceDemoData
from sauceModels.saucedemo_login import LoginPage
from sauceModels.saucedemo_PLP import ProductListPage

@pytest.fixture(scope="function", autouse=True)
def create_browser_context(context, page: Page) -> None:
    # page = context.new_page()
    page.goto(SauceDemoData.sauceURL)
    
    onLoginPage = LoginPage(page)
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    yield context