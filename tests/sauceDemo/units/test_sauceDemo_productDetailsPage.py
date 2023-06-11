from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
import time

from sauceLocators.page_elements import *
from sauceModels.saucedemo_PLP import ProductListPage
from sauceUtils.data import SauceDemoData, SauceDemoProducts

@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto('https://www.saucedemo.com/inventory-item.html?id=4')
    yield page
    
@pytest.mark.unitTest
def test_productsDetailsPage_all_items(page: Page):
    for item in range(1, 6, 1):
        page.goto(SauceDemoData.sauceURL+f"inventory-item.html?id={item}")
        expect(page.locator(SwagLabsPDPLocators.PRD_IMG)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_NAME)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_DESC)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_PRICE)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_BTN)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_BTN)).not_to_be_disabled()
        


