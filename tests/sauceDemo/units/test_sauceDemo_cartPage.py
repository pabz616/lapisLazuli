from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re

from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData, SauceDemoProducts, SauceDemoCart
import time

@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first.click()
    page.locator(SwagLabsHeaderLocators.CART_BUTTON).click()
    yield page

#PAGE    
@pytest.mark.unitTest
def test_cartPage_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoCart.cartURL))

#CART PAGE TITLE    
@pytest.mark.unitTest
def test_cartPage_title_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.SECTION_TITLE)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.SECTION_TITLE)).to_have_text(SauceDemoCart.cartPageTitle)

#CART PAGE SECTION LABELS 
@pytest.mark.unitTest
def test_cartPage_quantity_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_LABEL)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_quantity_label_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_LABEL)).to_have_text("QTY")
    
@pytest.mark.unitTest
def test_cartPage_description_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC_LABEL)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_description_label_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC_LABEL)).to_have_text("Description")
    
#CART ITEMS ADDED SECTION
@pytest.mark.unitTest
def test_cartPage_item_quantity_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_item_quantity_field_shows_item_added(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).not_to_be_empty()
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).to_have_text("1") 

@pytest.mark.unitTest
def test_cartPage_item_quantity_field_cannot_be_updated(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).not_to_be_focused()
    
@pytest.mark.unitTest
def test_cartPage_item_name_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).to_be_visible()
    
