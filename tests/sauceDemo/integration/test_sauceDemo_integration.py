from playwright.sync_api import sync_playwright, Page, expect
from sauceUtils.data import *
import pytest
import re
from sauceLocators.page_elements import *
from sauceModels.saucedemo_login import LoginPage
from sauceModels.saucedemo_PLP import ProductListPage
from sauceModels.sauceDemo_cart import CartPage
from sauceModels.sauceDemo_checkout import CheckoutPage
from sauceModels.sauceDemo_overview import OverviewPage
from sauceModels.sauceDemo_success import OrderCompletePage


@pytest.fixture(scope="function", autouse=True)
#use --browser-channel "chrome" to run tests in chrome, not chromium

def before_each(create_browser_context, page: Page):
    page.goto(SauceDemoProducts.productsURL)
    yield page
    
@pytest.mark.integration   
def test_integration_between_login_and_product_list(page: Page):
    """Test that successful login yields navigation to the product list"""
    expect(page).to_have_url(re.compile(SauceDemoProducts.productsURL))
    
@pytest.mark.integration   
def test_integration_between_product_list_and_product_details(page: Page):
    """Test from product list navigation occurs to product details"""
    pdpURL = 'https://www.saucedemo.com/inventory-item.html?id=4'
    onProductList = ProductListPage(page)
    onProductList.selectItem()
    expect(page).to_have_url(pdpURL)
    
@pytest.mark.integration   
def test_integration_between_product_list_and_global_header_badge(page: Page):
    """Test selection of product from product list, header item badge is shown when items are added to cart"""
       
    #NOTHING ADDED TO CART
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_be_visible()
    
    #ADDING ALL ITEMS TO CART
    page.locator(SwagLabsPLPLocators.ADD_TO_CART).first.click()
        
    #AFTER ALL ITEMS ARE ADDED TO CART
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).to_be_visible()
    expect(page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)).not_to_have_text('0')
    
@pytest.mark.integration   
def test_integration_between_product_list_and_cart(page: Page):
    """Test from product list navigation occurs to cart page"""   
    page.locator(SwagLabsPLPLocators.ADD_TO_CART).first.click()
    page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE).click()
    expect(page).to_have_url(re.compile(SauceDemoCart.cartURL))
    
@pytest.mark.integration   
def test_integration_between_product_list_and_cart_after_update(page: Page):
    """Test badge on header gets updated when removing a product from cart"""
    itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
    
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    expect(itemAddedBadge).not_to_be_visible()
    
    #ADDING TWO ITEMS TO CART
    onProductListPage.add_two_items_to_cart()
    itemAddedBadge.click()
    expect(itemAddedBadge).to_have_text('2')
    
    #REMOVE 1 ITEM FROM CART
    onCartPage.removeItem()
    expect(itemAddedBadge).to_have_text('1')
    
@pytest.mark.integration   
def test_integration_from_cart_to_checkout_step1(page: Page):
    """Test that user can move forward through checkout"""
    itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
    
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)

    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    expect(page).to_have_url(re.compile(SauceDemoCheckout.orderCheckoutURL))
    
@pytest.mark.integration   
def test_navigation_away_from_checkout_step1(page: Page):
    """Test that user can cancel checkout"""
    itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
    
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)

    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.cancelCustomerInfo()
    
    #ITEMS HAVE NOT BEEN REMOVED FROM CART WHEN NAVIGATING BACK
    expect(page).to_have_url(re.compile(SauceDemoCart.cartURL))
    expect(itemAddedBadge).not_to_have_text('0')

@pytest.mark.integration   
def test_integration_from_checkout_step1_to_checkout_step2(page: Page):
    """Test that user can get to overview of checkout"""
    itemAddedBadge = page.locator(SwagLabsHeaderLocators.ITEM_ADDED_BADGE)
    itemAdded = page.locator('[class="cart_item"]')
    purchaseSummary = page.locator('[class="summary_info"]')
    
    onProductListPage = ProductListPage(page)
    onCartPage = CartPage(page)
    onCheckoutPage = CheckoutPage(page)

    onProductListPage.addToCart()
    onProductListPage.navigateToCartPage()
    onCartPage.proceedToCheckout()
    onCheckoutPage.completeCustomerInfo()
    
    expect(page).to_have_url(re.compile(SauceDemoOverview.orderOverviewURL))
    expect(itemAddedBadge).to_have_text('1')
    expect(itemAdded).to_be_visible()
    expect(purchaseSummary).to_be_visible()    