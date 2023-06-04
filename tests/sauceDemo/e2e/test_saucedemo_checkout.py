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
def test_checkout(page: Page):
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
    
    #TODO Add all items to cart
    #TODO Update item count
    #TODO Remove an item from cart
    #TODO Remove all items from cart
    #TODO Cancel Order
    
    #TODO UNIT TESTS
    #TODO API TESTS
    #TODO INTEGRATION TESTS
    #TODO SECURITY TESTS