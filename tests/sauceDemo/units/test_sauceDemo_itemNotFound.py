from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
import time

from sauceLocators.page_elements import *
from sauceModels.saucedemo_PLP import ProductListPage
from sauceUtils.data import SauceDemoData, SauceDemoProducts

@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto('https://www.saucedemo.com/inventory-item.html?id=48')
    yield page

@pytest.mark.xfail(reason="Add to cart button should not be shown; When clicked, site crashes. Price does not belong either.")    
@pytest.mark.unitTest
def test_productsDetailsPage_item_not_found(page: Page):
        page.goto(SauceDemoData.sauceURL+f"inventory-item.html?id=48")
        expect(page.locator(SwagLabsPDPLocators.PRD_IMG)).to_be_visible()
        #
        expect(page.locator(SwagLabsPDPLocators.PRD_NAME)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_NAME)).to_have_text(SauceDemoProducts.NO_ITEM)
        #
        expect(page.locator(SwagLabsPDPLocators.PRD_DESC)).to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_DESC)).to_have_text(SauceDemoProducts.NO_ITEM_COPY)
        #
        expect(page.locator(SwagLabsPDPLocators.PRD_PRICE)).not_to_be_visible()
        expect(page.locator(SwagLabsPDPLocators.PRD_BTN)).not_to_be_visible()