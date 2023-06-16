from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re

from sauceLocators.page_elements import *
from sauceUtils.data import *


@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    page.locator(SwagLabsPLPLocators.ADD_TO_CART).first.click()
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
    expect(page.locator(SwagLabsCartPageLocators.QTY_LABEL)).to_have_text(SauceDemoCart.cartQtyLabel)
    
@pytest.mark.unitTest
def test_cartPage_description_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC_LABEL)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_description_label_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC_LABEL)).to_have_text(SauceDemoCart.cartDescriptionLabel)
    
#CART ITEMS ADDED SECTION
@pytest.mark.unitTest
def test_cartPage_item_added_quantity_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_item_added_quantity_field_shows_item_added(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).not_to_be_empty()
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).to_have_text("1") 

@pytest.mark.unitTest
def test_cartPage_item_added_quantity_field_cannot_has_no_focus_state(page: Page):
    """Test that confirms the item added quantity field cannot be edited since it has no focus state"""
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).not_to_be_focused()
    
@pytest.mark.unitTest
def test_cartPage_item_added_name_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.NAME)).to_be_visible()

@pytest.mark.unitTest
def test_cartPage_item_added_name_is_consistent(page: Page):
    item_added = page.locator(SwagLabsCartPageLocators.NAME)
    expect(item_added).to_have_text(SauceDemoCart.cartItem)
        
@pytest.mark.unitTest
def test_cartPage_item_added_name_redirect_to_product_details(page: Page):
    """Test that the product name is actionable by virtue of redirecting to the product details page"""
    page.locator(SwagLabsCartPageLocators.NAME).click()
    expect(page).not_to_have_url(re.compile(SauceDemoCart.cartURL))   

@pytest.mark.unitTest
def test_cartPage_item_added_copy_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC)).to_be_visible()

@pytest.mark.xfail(reason="Copy is incorrect")
@pytest.mark.unitTest
def test_cartPage_item_added_copy_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.DESC)).to_contain_text(SauceDemoCart.cartItemCopy)
    
@pytest.mark.unitTest
def test_cartPage_item_added_price_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.PRICE)).to_be_visible()

@pytest.mark.unitTest
def test_cartPage_item_added_price_is_consistent(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.PRICE)).to_contain_text(SauceDemoCart.cartItemPrice)
    
@pytest.mark.unitTest
def test_cartPage_item_added_REMOVE_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.REMOVE_BTN)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_item_added_REMOVE_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.REMOVE_BTN)).not_to_be_disabled()

@pytest.mark.xfail(reason="Checkout button remains actionable, user can proceed thru checkout w/o an item in cart")
@pytest.mark.unitTest
def test_cartPage_item_added_REMOVE_button_clicked(page: Page):
    """Test that entire item is removed from cart, checkout btn is disabled"""
    page.locator(SwagLabsCartPageLocators.REMOVE_BTN).click()
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.QTY_INPUT)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.NAME)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.DESC)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.PRICE)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.REMOVE_BTN)).not_to_be_visible()
    expect(page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)).to_be_disabled()
    
    
@pytest.mark.unitTest
def test_cartPage_item_added_REMOVE_button_clicked_state(page: Page, element_id= "remove-sauce-labs-backpack"):
    expect(page.locator(SwagLabsCartPageLocators.REMOVE_BTN)).to_have_id(element_id)
    expect(page.locator(SwagLabsCartPageLocators.REMOVE_BTN)).to_have_text(SauceDemoCart.cartRemoveItemBtnText)
    
@pytest.mark.unitTest
def test_cartPage_item_added_CHECKOUT_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_item_added_CHECKOUT_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)).not_to_be_disabled()

@pytest.mark.unitTest
def test_cartPage_item_added_CHECKOUT_redirect_to_checkout_page(page: Page):
    page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN).click()
    expect(page).to_have_url(re.compile(SauceDemoCheckout.orderCheckoutURL))
    
@pytest.mark.unitTest
def test_cartPage_item_added_CHECKOUT_button_clicked_state(page: Page, element_id= "checkout"):
    expect(page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)).to_have_id(element_id)
    expect(page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN)).to_have_text(SauceDemoCart.cartCheckoutBtnText)
    
@pytest.mark.unitTest
def test_cartPage_item_added_CONTINUE_SHOPPING_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING)).to_be_visible()
    
@pytest.mark.unitTest
def test_cartPage_item_added_CONTINUE_SHOPPING_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING)).not_to_be_disabled()

@pytest.mark.unitTest
def test_cartPage_item_added_CONTINUE_SHOPPING_redirect_back_to_product_list_page(page: Page):
    page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING).click()
    expect(page).to_have_url(re.compile(SauceDemoProducts.productsURL))
    
@pytest.mark.unitTest
def test_cartPage_item_added_CONTINUE_SHOPPING_button_clicked_state(page: Page, element_id= "continue-shopping"):
    expect(page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING)).to_have_id(element_id)
    expect(page.locator(SwagLabsCartPageLocators.CONTINUE_SHOPPING)).to_have_text(SauceDemoCart.cartContinueBtnText)