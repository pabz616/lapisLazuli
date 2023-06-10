from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
import time

from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData


@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoData.sauceURL+'inventory.html')
    yield page
    
@pytest.mark.unitTest
def test_productsPage_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoData.sauceURL+'inventory.html'))

@pytest.mark.unitTest   
def test_productsPageHeader_has_title(page: Page):
    expect(page).to_have_title(re.compile(SauceDemoData.pageTitle))

#GLOBAL HEADER LOGO
@pytest.mark.unitTest    
def test_productsPageHeader_has_logo(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.HEADER_LOGO)).to_be_visible()

#GLOBAL HEADER MENU
@pytest.mark.unitTest
def test_productsPageHeader_has_menu_button(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).to_be_visible()

@pytest.mark.unitTest        
def test_productsPageHeader_menu_button_has_id(page: Page, element_id="react-burger-menu-btn"):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).to_have_id(element_id)

@pytest.mark.unitTest    
def test_productsPageHeader_menu_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).not_to_be_disabled()

@pytest.mark.unitTest
def test_productsPageHeader_menu_button_not_immediately_focused_when_page_is_accessed(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).not_to_be_focused()
    
#GLOBAL HEADER CART BUTTON
@pytest.mark.unitTest
def test_productsPageHeader_has_cart_button(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).to_be_visible()
    
@pytest.mark.unitTest
def test_productsPageHeader_cart_button_has_id(page: Page, element_id="shopping_cart_container"):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).to_have_id(element_id)
    
@pytest.mark.unitTest
def test_productsPageHeader_cart_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).not_to_be_disabled()
    
@pytest.mark.unitTest
def test_productsPageHeader_cart_button_item_added_badge_is_not_displayed(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_be_visible()
    
@pytest.mark.unitTest
def test_productsPageHeader_cart_button_item_added_badge_is_displayed(page: Page):
    page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first.click()
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).to_be_visible()

@pytest.mark.unitTest
def test_productsPageHeader_cart_button_item_added_badge_count_is_displayed(page: Page):
    page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first.click()
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).to_have_text("1")

@pytest.mark.unitTest
def test_productsPageHeader_cart_button_item_added_badge_count_values(page: Page):
    """Test that the following CART ITEM ADDED values are not possible"""
    page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first.click()
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text("")
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text("0")
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text("99")
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text("-1")
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text("A")