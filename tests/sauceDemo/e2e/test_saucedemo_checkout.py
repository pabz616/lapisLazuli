from playwright.sync_api import sync_playwright, Page, expect
from sauceUtils.data import SauceDemoData
import pytest
import re
from sauceModels.saucedemo_login import LoginPage
from sauceModels.saucedemo_PLP import ProductListPage
from sauceModels.sauceDemo_cart import CartPage
from sauceModels.sauceDemo_checkout import CheckoutPage
from sauceModels.sauceDemo_overview import OverviewPage
from sauceModels.sauceDemo_success import OrderCompletePage

@pytest.fixture(scope="function", autouse=True)
#use --browser-channel "chrome" to run tests in chrome, not chromium


def before_each(page: Page):
    page.goto(SauceDemoData.sauceURL) #start
    yield

 
@pytest.mark.critical   
def test_purchase_single_item(page: Page):
    #TODO Refactor this .. it needs to be reusable
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_entire_catalog(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.addAllItemsToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_item_filtered_by_name_Z_A(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.sortByProductNameZtoA()
    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_item_filtered_by_price_Low_to_High(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.sortByProductPriceLowToHigh()
    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_item_filtered_by_price_High_to_Low(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.sortByProductPriceHighToLow()
    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_item_then_update_order(page: Page):
    """Add an item, then return back (continue shopping) and add another item"""
    pass

@pytest.mark.critical
def test_purchase_item_then_cancel_order(page: Page):
    """Add an item, then remove it from the cart -- the cancel button is misnamed"""
    pass
   
#TODO More Integration tests for "Your Information" section
#TODO SECURITY TESTS