from playwright.sync_api import sync_playwright, Page, expect
from sauceUtils.data import SauceDemoData, SauceDemoCheckout
import pytest
import re
from sauceLocators.page_elements import *
from sauceModels.sauceDemo_checkout import CheckoutPage

#checkout-step-one.html
@pytest.fixture(scope="function", autouse=True)
#use --browser-channel "chrome" to run tests in chrome, not chromium

def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoCheckout.orderCheckoutURL)
    yield page

@pytest.mark.integration   
def test_integration_access_customer_information_form(page: Page):
    """Test that after successful login, the page under test is accessible"""
    expect(page).to_have_url(re.compile(SauceDemoCheckout.orderCheckoutURL))
    
@pytest.mark.integration
def test_integration_customer_information_form_is_consistent(page: Page):
    onCheckoutPage = CheckoutPage(page)
    onCheckoutPage.checkUI()
    
@pytest.mark.integration
def test_integration_customer_information_form_valid_data(page: Page):
    onCheckoutPage = CheckoutPage(page)
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, SauceDemoData.LastName, SauceDemoData.ZipCode)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).not_to_be_visible()

@pytest.mark.integration
def test_integration_customer_information_form_required_validation_First_Name(page: Page):
    onCheckoutPage = CheckoutPage(page)
    onCheckoutPage.completeCustomerInfo("", SauceDemoData.LastName, SauceDemoData.ZipCode)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(0)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text("Error: First Name is required")

@pytest.mark.integration
def test_integration_customer_information_form_required_validation_Last_Name(page: Page):
    onCheckoutPage = CheckoutPage(page)
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, "", SauceDemoData.ZipCode)
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(1)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text("Error: Last Name is required")
    
@pytest.mark.integration
def test_integration_customer_information_form_required_validation_ZipCode(page: Page):
    onCheckoutPage = CheckoutPage(page)
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, SauceDemoData.LastName, "")
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_ICON).nth(2)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_be_visible()
    expect(page.locator(SwagLabsCheckoutPageLocators.ERROR_MSG)).to_have_text("Error: Postal Code is required")