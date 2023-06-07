from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData
from sauceModels.saucedemo_login import LoginPage


@pytest.mark.unit_test
@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto(SauceDemoData.sauceURL)
    
    onLoginPage = LoginPage(page)
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    yield
    
    #TODO repurpose login authentication

def test_productsPage_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoData.productsURL))
    
def test_productsPageHeader_has_title(page: Page):
    expect(page).to_have_title(re.compile(SauceDemoData.pageTitle))

#GLOBAL HEADER LOGO    
def test_productsPageHeader_has_logo(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.HEADER_LOGO)).to_be_visible()

#GLOBAL HEADER MENU
def test_productsPageHeader_has_menu_button(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).to_be_visible()
        
def test_productsPageHeader_menu_button_has_id(page: Page, element_id="react-burger-menu-btn"):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).to_have_id(element_id)
    
def test_productsPageHeader_menu_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).not_to_be_disabled()

def test_productsPageHeader_menu_button_not_immediately_focused_when_page_is_accessed(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.MENU_BUTTON)).not_to_be_focused()
    
#GLOBAL HEADER CART BUTTON
def test_productsPageHeader_has_cart_button(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).to_be_visible()
    
def test_productsPageHeader_cart_button_has_id(page: Page, element_id="shopping_cart_container"):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).to_have_id(element_id)
    
def test_productsPageHeader_cart_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsHeaderLocators.CART_BUTTON)).not_to_be_disabled()