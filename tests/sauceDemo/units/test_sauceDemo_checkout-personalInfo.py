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
    yield page

#PAGE    
@pytest.mark.unitTest
def test_checkout_step1_has_expected_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoCheckout.orderCheckoutURL))
    
@pytest.mark.unitTest
def test_checkout_step1_has_section_title(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.SECTION_TITLE)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_section_title_is_consistent(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.SECTION_TITLE)).to_have_text(SauceDemoCheckout.orderCheckoutSectionText)

#CUSTOMER FIRST NAME INPUT
@pytest.mark.unitTest
def test_checkout_step1_has_customer_firstname_input(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_is_editable(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).to_be_editable()

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_is_text(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).to_have_attribute("type", "text")

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_has_id(page: Page, element_id= "first-name"):
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).to_have_id(element_id)

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_is_a_required_field(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    
    #DIRTY STATE
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).first).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text(SauceDemoCheckout.orderCheckoutFNameErrorMsg)
    
@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_accepts_mixed_characters(page: Page):
    """Testing that the input accepts mixed characters, no error shown"""
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.mixed_char)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).first).not_to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_has_minimum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.short_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).first).not_to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_has_maximum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.long_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).first).not_to_be_visible()

#CUSTOMER LAST NAME INPUT
@pytest.mark.unitTest
def test_checkout_step1_has_customer_lastname_input(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_is_editable(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)).to_be_editable()

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_is_text(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)).to_have_attribute("type", "text")

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_id(page: Page, element_id= "last-name"):
    expect(page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)).to_have_id(element_id)

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_is_a_required_field(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.sample_zip)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    
    #DIRTY STATE
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(1)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text(SauceDemoCheckout.orderCheckoutLNameErrorMsg)
    
@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_accepts_mixed_characters(page: Page):
    """Testing that the input accepts mixed characters, no error shown"""
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.mixed_char)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(1)).not_to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_minimum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.short_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(1)).not_to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_maximum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.long_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(1)).not_to_be_visible()

#CUSTOMER ZIP/POSTAL CODE INPUT
@pytest.mark.unitTest
def test_checkout_step1_has_customer_zipcode_input(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)).to_be_visible()
    
@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_is_editable(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)).to_be_editable()

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_is_text(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)).to_have_attribute("type", "text")

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_has_id(page: Page, element_id= "postal-code"):
    expect(page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)).to_have_id(element_id)

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_is_a_required_field(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    
    #DIRTY STATE
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text(SauceDemoCheckout.orderCheckoutZipCodeErrorMsg)
    
@pytest.mark.unitTest
@pytest.mark.xfail(reason="Zip/Postal Code accepts non-numeric characters")
def test_checkout_step1_customer_zipcode_input_accepts_mixed_characters(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    
    """Zipcode throws error when the input accepts mixed characters"""
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.mixed_char)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()

@pytest.mark.unitTest
@pytest.mark.xfail(reason="Zip/Postal Code accepts 3 characters where at minimum 5 is expected")
def test_checkout_step1_customer_zipcode_input_has_minimum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    
    """Zipcode throws error when the input accepts short zipcode,  message says zipcode is invalid"""
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.short_number)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()

@pytest.mark.unitTest
@pytest.mark.xfail(reason="Zip/Postal Code accepts 20 characters where a maximum of 10 is expected")
def test_checkout_step1_customer_firstname_input_has_maximum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    
    """Zipcode throws error when the input accepts short zipcode, message says zipcode is invalid"""
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.long_number)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()
    
@pytest.mark.unitTest
@pytest.mark.xfail(reason="Zip/Postal Code accepts an invalid zipcode")
def test_checkout_step1_customer_firstname_input_has_maximum_characters_threshold_set(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    
    """Zipcode throws error when the input accepts an unrecognized / incorrect zipcode number"""
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.sample_number)
    page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON).click()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()

@pytest.mark.unitTest
def test_checkout_step1_customer_information_inputs_get_cleared_after_refresh(page: Page):
    page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT).fill(SauceDemoData.sample_text)
    page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT).fill(SauceDemoData.sample_zip)
    page.keyboard.press('F5')
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).not_to_have_text(SauceDemoData.sample_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.LNAME_INPUT)).not_to_have_text(SauceDemoData.sample_text)
    expect(page.locator(SwagLabsCheckoutPageLocators.ZIP_INPUT)).not_to_have_text(SauceDemoData.sample_zip)

#ACTIONS
#CONTINUE BUTTON
def test_checkout_step1_has_CONTINUE_button(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON)).to_be_visible()
    
def test_checkout_step1_CONTINUE_button_text_is_consistent(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON)).to_have_text('Continue')

def test_checkout_step1_CONTINUE_is_actionable(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CONTINUE_BUTTON)).not_to_be_disabled()

#CANCEL BUTTON
def test_checkout_step1_has_CANCEL_button(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CANCEL_BUTTON)).to_be_visible()
    
def test_checkout_step1_CANCEL_button_text_is_consistent(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CANCEL_BUTTON)).to_have_text('Cancel')

def test_checkout_step1_CANCEL_is_actionable(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.CANCEL_BUTTON)).not_to_be_disabled()


