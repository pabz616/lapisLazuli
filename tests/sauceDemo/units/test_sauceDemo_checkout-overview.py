from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re

from sauceLocators.page_elements import *
from sauceUtils.data import *

@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    page.locator(SwagLabsProductsPageLocators.PRD1_BTN).first.click()
    page.locator(SwagLabsHeaderLocators.CART_BUTTON).click()
    page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN).click()
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.sample_zip)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    yield page
    
#PAGE    
@pytest.mark.unitTest
def test_checkout_step2_has_expected_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoOverview.orderOverviewURL))
    
    
#CART SECTION
#CART PAGE TITLE    
@pytest.mark.unitTest
def test_checkout_step2_title_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.SECTION_TITLE)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_step2_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.SECTION_TITLE)).to_have_text(SauceDemoOverview.orderOverviewSectionText)

#CART PAGE SECTION LABELS 
@pytest.mark.unitTest
def test_checkout_step2_quantity_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_LABEL)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_step2_quantity_label_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_LABEL)).to_have_text(SauceDemoOverview.orderOverviewCartQtyLabel)
    
@pytest.mark.unitTest
def test_checkout_step2_description_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.DESC_LABEL)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_step2_description_label_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.DESC_LABEL)).to_have_text(SauceDemoOverview.orderOverviewCartDescriptionLabel)
    
#CART ITEMS ADDED SECTION
@pytest.mark.unitTest
def test_checkout_step2_item_added_quantity_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_INPUT)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_step2_item_added_quantity_field_shows_item_added(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_INPUT)).not_to_be_empty()
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_INPUT)).to_have_text("1") 

@pytest.mark.unitTest
def test_checkout_step2_item_added_quantity_field_cannot_has_no_focus_state(page: Page):
    """Test that confirms the item added quantity field cannot be edited since it has no focus state"""
    expect(page.locator(SwagLabsOverviewPageLocators.QTY_INPUT)).not_to_be_focused()
    
@pytest.mark.unitTest
def test_checkout_step2_item_added_name_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.NAME)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step2_item_added_name_is_consistent(page: Page):
    item_added = page.locator(SwagLabsOverviewPageLocators.NAME)
    expect(item_added).to_have_text(SauceDemoOverview.orderOverviewCartItem)
        
@pytest.mark.unitTest
def test_checkout_step2_item_added_copy_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.DESC)).to_be_visible()

@pytest.mark.xfail(reason="Copy is incorrect")
@pytest.mark.unitTest
def test_checkout_step2_item_added_copy_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.DESC)).to_contain_text(SauceDemoOverview.cartItemCopy)
    
@pytest.mark.unitTest
def test_checkout_step2_item_added_price_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step2_item_added_price_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE)).to_contain_text(SauceDemoOverview.orderOverviewCartPrice)
    
# #OVERVIEW SECTION
@pytest.mark.unitTest
def test_checkout_step2_item_payment_information_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PAYMENT_INFO_LABEL).first).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step2_item_payment_information_label_is_consistent(page: Page, label = 'Payment Information'):
    expect(page.locator(SwagLabsOverviewPageLocators.PAYMENT_INFO_LABEL).first).to_have_text(label)

@pytest.mark.unitTest    
def test_checkout_step2_item_payment_information_value_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PAYMENT_INFO).first).to_have_text(SauceDemoOverview.orderOverviewPaymentInfo)

@pytest.mark.unitTest
def test_checkout_step2_item_shipping_information_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.SHIPPING_INFO_LABEL).nth(1)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step2_item_shipping_information_label_is_consistent(page: Page, label = 'Shipping Information'):
    expect(page.locator(SwagLabsOverviewPageLocators.PAYMENT_INFO_LABEL).nth(1)).to_have_text(label)

@pytest.mark.unitTest    
def test_checkout_step2_item_shipping_information_value_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.SHIPPING_INFO).nth(1)).to_have_text(SauceDemoOverview.orderOverviewShippingInfo)

@pytest.mark.unitTest
def test_checkout_step2_item_subtotal_label_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE_SUBTOTAL_LABEL).nth(2)).to_be_visible()

@pytest.mark.xfail(reason="Copy is incorrect. Should say Price Subtotal")
@pytest.mark.unitTest
def test_checkout_step2_item_subtotal_is_consistent(page: Page, label = 'Price Subtotal'):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE_SUBTOTAL_LABEL).nth(2)).to_have_text(label)

@pytest.mark.unitTest    
def test_checkout_step2_item_subtotal_value_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE_SUBTOTAL)).to_be_visible()

@pytest.mark.unitTest    
def test_checkout_step2_item_subtotal_value_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.PRICE_SUBTOTAL)).to_have_text(SauceDemoOverview.orderOverviewSumTotal)

@pytest.mark.unitTest    
def test_checkout_step2_item_subtotal_tax_value_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.TAX)).to_be_visible()

@pytest.mark.unitTest    
def test_checkout_step2_item_subtotal_tax_value_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.TAX)).to_have_text(SauceDemoOverview.orderOverviewTax)

def test_checkout_step2_item_total_value_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.TOTAL)).to_be_visible()

@pytest.mark.unitTest    
def test_checkout_step2_item_total_value_is_consistent(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.TOTAL)).to_have_text(SauceDemoOverview.orderOverviewTotal)

#ACTIONS
@pytest.mark.unitTest    
def test_checkout_step2_finish_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.FINISH_BUTTON)).to_be_visible()

@pytest.mark.unitTest    
def test_checkout_step2_finish_button_has_text(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.FINISH_BUTTON)).to_have_text("Finish")

@pytest.mark.unitTest    
def test_checkout_step2_finish_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.FINISH_BUTTON)).not_to_be_disabled()

@pytest.mark.unitTest    
def test_checkout_step2_cancel_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.CANCEL_BUTTON)).to_be_visible()

@pytest.mark.unitTest    
def test_checkout_step2_cancel_button_has_text(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.CANCEL_BUTTON)).to_have_text("Cancel")

@pytest.mark.unitTest    
def test_checkout_step2_cancel_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsOverviewPageLocators.CANCEL_BUTTON)).not_to_be_disabled()