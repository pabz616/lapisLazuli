from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re

from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData, SauceDemoProducts



@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    yield page

#PAGE    
@pytest.mark.unitTest
def test_productsListPage_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoProducts.productsURL))

#SECONDARY HEADER
@pytest.mark.unitTest   
def test_productsListPage_has_secondaryHeader_title(page: Page):
    expect(page).to_have_title(re.compile(SwagLabsProductsPageLocators.HEADER))

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.HEADER)).to_contain_text(SauceDemoProducts.productsTitle)

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_has_sort_dropdown(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD_SORT)).to_be_visible()
    
@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_is_actionable(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD_SORT)).not_to_be_disabled()

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_default_value(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.SELECTED_OPTION)).to_contain_text("Name (A to Z)")   

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_select_value(page: Page):
    page.locator(SwagLabsProductsPageLocators.PRD_SORT).select_option(['za'])
    expect(page.locator(SwagLabsProductsPageLocators.SELECTED_OPTION)).to_contain_text("Name (Z to A)")
   
    page.locator(SwagLabsProductsPageLocators.PRD_SORT).select_option(['lohi'])
    expect(page.locator(SwagLabsProductsPageLocators.SELECTED_OPTION)).to_contain_text("Price (low to high)")
    
    page.locator(SwagLabsProductsPageLocators.PRD_SORT).select_option(['hilo'])
    expect(page.locator(SwagLabsProductsPageLocators.SELECTED_OPTION)).to_contain_text("Price (high to low)")

#FIRST ITEM CONTAINERS
@pytest.mark.unitTest
def test_productsListPage_item1_image(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_IMG).first).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_item1_image_is_actionable(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_IMG).first).to_be_enabled()

@pytest.mark.unitTest
def test_productsListPage_item1_name_is_displayed(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_NAME).first).to_be_visible()

@pytest.mark.unitTest    
def test_productsListPage_item1_name_is_consistent(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_NAME).first).to_have_text(SauceDemoProducts.PRD1_NAME)    

@pytest.mark.unitTest
def test_productsListPage_item1_description(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_DESC).first).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_item1_price_amount_shown(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_PRICE).first).to_have_text(SauceDemoProducts.PRD1_PRICE)    

@pytest.mark.unitTest
def test_productsListPage_item1_price_amount_is_not_negative(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_PRICE).first).not_to_have_text("-$29.99")

@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first).to_be_visible()
    
@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_id(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first).to_have_id("add-to-cart-sauce-labs-backpack")

@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_is_functional(page: Page):
    expect(page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first).not_to_be_disabled()

#ITERATING THROUGH ALL ITEMS
@pytest.mark.unitTest
def test_productsListPage_all_item_images(page: Page):
    for img in page.get_by_role('img').all():
        expect(img).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_all_item_names(page: Page):
    for name in page.get_by_role('inventory_item_name').all():
        expect(name).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_all_item_descriptions(page: Page):
    for desc in page.get_by_role('inventory_item_desc').all():
        expect(desc).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_all_item_prices(page: Page):
    for price in page.get_by_role('inventory_item_price').all():
        expect(price).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_all_item_action_buttons(page: Page):
    for buttons in page.get_by_role('btn_inventory').all():
        expect(buttons).to_be_visible()
        expect(buttons).not_to_be_disabled()