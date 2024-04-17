from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re

from sauceLocators.page_elements import *
from sauceUtils.data import *

@pytest.fixture(scope="function", autouse=True)
def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    page.locator(SwagLabsPLPLocators.PRD1_BTN).first.click()
    page.locator(SwagLabsHeaderLocators.CART_BUTTON).click()
    page.locator(SwagLabsCartPageLocators.CHECKOUT_BTN).click()
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.sample_zip)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    page.locator(SwagLabsOverviewPageLocators.FINISH_BUTTON).click()
    yield page
    
#PAGE    
@pytest.mark.unitTest
def test_checkout_completion_has_expected_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoConfirmation.orderConfirmationURL))
    
@pytest.mark.unitTest
def test_checkout_complete_title_is_displayed(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.SECTION_TITLE)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_complete_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.SECTION_TITLE)).to_have_text(SauceDemoConfirmation.orderConfirmationSectionText)
    
def test_checkout_complete_item_added_badge_is_no_longer_shown(page: Page):
    """Test that on the global header, when the order is completed, the badge counter disappears"""
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_be_visible()
    
def test_checkout_complete_iconography_is_displayed(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.IMG)).to_be_visible()

def test_checkout_complete_iconography_class_attribute(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.IMG)).to_have_class('pony_express')

def test_checkout_complete_success_message_header_is_displayed(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.HEADER)).to_be_visible()
    
def test_checkout_complete_success_message_header_text_is_consistent(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.HEADER)).to_have_text(SauceDemoConfirmation.successMessageHeader)
    
def test_checkout_complete_success_message_copy_displayed(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.COPY)).to_be_visible()
    
def test_checkout_complete_success_message_copy_is_consistent(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.COPY)).to_have_text(SauceDemoConfirmation.successMessageCopy)
 
 #ACTION   
@pytest.mark.unitTest    
def test_checkout_complete_BACK_HOME_button_is_displayed(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.BTN)).to_be_visible()
    

@pytest.mark.unitTest    
def test_checkout_complete_BACK_HOME_button_has_datatest_attribute(page: Page, data_test_value='back-to-products'):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.BTN)).to_have_attribute('data-test', data_test_value)
    
@pytest.mark.unitTest    
def test_checkout_complete_BACK_HOME_button_has_id(page: Page, btn_id='back-to-products'):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.BTN)).to_have_id(btn_id)

@pytest.mark.unitTest    
def test_checkout_complete_BACK_HOME_button_has_text(page: Page, btn_text='Back Home'):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.BTN)).to_have_text(btn_text)

@pytest.mark.unitTest    
def test_checkout_complete_BACK_HOME_button_is_actionable(page: Page):
    expect(page.locator(SwagLabsOrderConfirmationPageLocators.BTN)).not_to_be_disabled()