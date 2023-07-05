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
    """Test entire checkout flow with a single item"""
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
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.critical
def test_purchase_entire_catalog(page: Page):
    """Test entire checkout flow, purchasing all items shown in catalog"""
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
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.high
def test_purchase_item_filtered_by_name_Z_A(page: Page):
    """Test that a purchase can be made when the product is filtered by name, alphabetically descending Z to A"""
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)
    onOverviewPage = OverviewPage(page)
    onOrderCompletePage = OrderCompletePage(page)
    #
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    onProductListPage.sortByProductNameZToA()
    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.high
def test_purchase_item_filtered_by_price_Low_to_High(page: Page):
    """Test that a purchase can be made when the product is filtered by lowest price"""
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
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.high
def test_purchase_item_filtered_by_price_High_to_Low(page: Page):
    """Test that a purchase can be made when the product is filtered by highest price"""
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
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.normal
def test_purchase_item_then_update_order(page: Page):
    """Add an item, then return back (continue shopping) and add another item"""
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
    onCartPage.continueShopping()
    onProductListPage.addAnotherItemToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()     
    onCheckoutPage.completeCustomerInfo(SauceDemoData.FirstName, sauceDemoData.LastName, sauceDemoData.ZipCode)
    onOverviewPage.confirmPurchaseDetails()
    onOrderCompletePage.confirmOrderSuccessDetails()

@pytest.mark.skip(reason="BUG! Checkout button is still active when cart is empty allowing user to proceed through checkout")
@pytest.mark.normal
def test_purchase_item_then_cancel_order(page: Page):
    """Add a single item, then remove it from the cart"""
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
    onCartPage.removeItem()   
