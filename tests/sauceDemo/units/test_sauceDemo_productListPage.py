from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
import time

from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData, SauceDemoProducts



@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    time.sleep(1)
    yield page

#PAGE    
@pytest.mark.unitTest
def test_productsListPage_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoProducts.productsURL))

#SECONDARY HEADER
@pytest.mark.unitTest   
def test_productsListPage_has_secondaryHeader_title(page: Page):
    expect(page).to_have_title(re.compile(SwagLabsPLPLocators.HEADER))

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsPLPLocators.HEADER)).to_contain_text(SauceDemoProducts.productsTitle)

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_has_sort_dropdown(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD_SORT)).to_be_visible()
    
@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_is_actionable(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD_SORT)).not_to_be_disabled()

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_default_value(page: Page):
    expect(page.locator(SwagLabsPLPLocators.SELECTED_OPTION)).to_contain_text("Name (A to Z)")   

@pytest.mark.unitTest
def test_productsListPage_secondaryHeader_sort_dropdown_select_value(page: Page):
    page.locator(SwagLabsPLPLocators.PRD_SORT).select_option(['za'])
    expect(page.locator(SwagLabsPLPLocators.SELECTED_OPTION)).to_contain_text("Name (Z to A)")
   
    page.locator(SwagLabsPLPLocators.PRD_SORT).select_option(['lohi'])
    expect(page.locator(SwagLabsPLPLocators.SELECTED_OPTION)).to_contain_text("Price (low to high)")
    
    page.locator(SwagLabsPLPLocators.PRD_SORT).select_option(['hilo'])
    expect(page.locator(SwagLabsPLPLocators.SELECTED_OPTION)).to_contain_text("Price (high to low)")

#FIRST ITEM CONTAINERS
@pytest.mark.unitTest
def test_productsListPage_item1_image(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_IMG).first).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_item1_image_is_actionable(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_IMG).first).to_be_enabled()

@pytest.mark.unitTest
def test_productsListPage_item1_name_is_displayed(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_NAME).first).to_be_visible()

@pytest.mark.unitTest    
def test_productsListPage_item1_name_is_consistent(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_NAME).first).to_have_text(SauceDemoProducts.PRD1_NAME)    

@pytest.mark.unitTest
def test_productsListPage_item1_description(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_DESC).first).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_item1_price_amount_shown(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_PRICE).first).to_have_text(SauceDemoProducts.PRD1_PRICE)    

@pytest.mark.unitTest
def test_productsListPage_item1_price_amount_is_not_negative(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_PRICE).first).not_to_have_text("-$29.99")

@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_BTN).first).to_be_visible()
    
@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_id(page: Page, element_id= "add-to-cart-sauce-labs-backpack"):
    expect(page.locator(SwagLabsPLPLocators.PRD1_BTN).first).to_have_id(element_id)

@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_button_is_functional(page: Page):
    expect(page.locator(SwagLabsPLPLocators.PRD1_BTN).first).not_to_be_disabled()
    
@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_clicked_state(page: Page, element_id= "remove-sauce-labs-backpack"):
    """Test that the button id changes after ADD TO CART is clicked"""
    page.locator(SwagLabsPLPLocators.PRD1_BTN).first.click()
    expect(page.locator(SwagLabsPLPLocators.PRD1_REMOVE).first).to_have_id(element_id)
    expect(page.locator(SwagLabsPLPLocators.PRD1_REMOVE).first).to_have_text("Remove")
    
@pytest.mark.unitTest
def test_productsListPage_item1_addToCart_text_changed_to_remove(page: Page):
    """Test that the button text changes to REMOVE after ADD TO CART is clicked"""
    page.locator(SwagLabsPLPLocators.PRD1_BTN).first.click()
    expect(page.locator(SwagLabsPLPLocators.PRD1_REMOVE).first).to_have_text("Remove")
    

#ITERATING THROUGH ALL ITEMS
@pytest.mark.unitTest
def test_productsListPage_all_item_images(page: Page):
    for img in page.get_by_role('img').all():
        expect(img).to_be_visible()

@pytest.mark.unitTest
def test_productsListPage_all_item_names(page: Page):
    for name in page.get_by_role('inventory_item_name').all():
        expect(name).to_be_visible()
        expect(name).to_have_attribute('href')

@pytest.mark.unitTest
def test_productsListPage_all_item_descriptions(page: Page):
    for desc in page.get_by_role('inventory_item_desc').all():
        expect(desc).to_be_visible()
        expect(desc).not_to_have_text(SauceDemoData.mixed_char)
        expect(desc).not_to_have_text(SauceDemoData.script)
        
@pytest.mark.unitTest
def test_productsListPage_all_item_prices(page: Page):
    for price in page.get_by_role('inventory_item_price').all():
        expect(price).to_be_visible()
        expect(price).not_to_have_text('$0.00')
        expect(price).not_to_have_text(SauceDemoData.alpha_num)
        expect(price).not_to_have_text(SauceDemoData.short_number)

@pytest.mark.unitTest
def test_productsListPage_all_item_action_buttons(page: Page):
    for button in page.locator(SwagLabsPLPLocators.ADD_TO_CART).all():        
        expect(button).to_be_visible()
        expect(button).to_have_text('Add to cart')
        expect(button).not_to_be_disabled()