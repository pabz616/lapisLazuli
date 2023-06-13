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
def test_checkout_step1_customer_firstname_input_has_placeholder_text(page: Page):
    expect(page.locator(SwagLabsCheckoutPageLocators.FNAME_INPUT)).to_have_attribute("placeholder", SauceDemoCheckout.orderCheckoutFNameInputPlaceholder)

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_is_a_required_field(page: Page):
    # test dirty state
    # check message is shown - Error: First Name is required
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_accepts_alpha_numeric_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_does_not_accept_NAN_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_has_minimum_characters_threshold_set(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_firstname_input_has_maximum_characters_threshold_set(page: Page):
    pass


#CUSTOMER LAST NAME INPUT
@pytest.mark.unitTest
def test_checkout_step1_has_customer_lastname_input(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_placeholder_text(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_is_a_required_field(page: Page):
    # test dirty state
    # check message is shown - Error: Last Name is required
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_accepts_alpha_numeric_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_does_not_accept_NAN_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_minimum_characters_threshold_set(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_lastname_input_has_maximum_characters_threshold_set(page: Page):
    pass

#CUSTOMER ZIP/POSTAL CODE INPUT
@pytest.mark.unitTest
def test_checkout_step1_has_customer_zipcode_input(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_has_placeholder_text(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_is_a_required_field(page: Page):
    # test dirty state
    # check message is shown - Error: Postal Code is required
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_accepts_alpha_numeric_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_does_not_accept_NAN_characters(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_has_minimum_characters_threshold_set(page: Page):
    pass

@pytest.mark.unitTest
def test_checkout_step1_customer_zipcode_input_has_maximum_characters_threshold_set(page: Page):
    pass

