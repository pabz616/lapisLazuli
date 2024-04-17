from playwright.sync_api import sync_playwright, Page, expect
from sauceUtils.data import SauceDemoData
import pytest
import re
from sauceModels.saucedemo_login import LoginPage
from sauceModels.saucedemo_PLP import ProductListPage

@pytest.fixture(scope="function", autouse=True)
#use --browser-channel "chrome" to run tests in chrome, not chromium

def before_each(page: Page):
    page.goto(SauceDemoData.sauceURL) #start
    yield

def test_title(page: Page):
    expect(page).to_have_title(re.compile("Swag Labs"))
    
def test_login_UI(page: Page):
    onLoginPage = LoginPage(page)
    onLoginPage.checkUI()

@pytest.mark.critical
def test_account_is_valid(page: Page):    
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    
    #REDIRECT TO PRODUCT_LIST
    expect(page).to_have_url(re.compile(".*inventory"))
    onProductListPage.checkUI()

@pytest.mark.critical    
def test_account_is_locked_out(page: Page):
    error = page.locator('[data-test="error"]')
    errorMsg = "Epic sadface: Sorry, this user has been locked out."
    
    onLoginPage = LoginPage(page)
    onLoginPage.submitLogin(SauceDemoData.lockedOutUSN, SauceDemoData.password)
    expect(error).to_be_visible()
    expect(error).to_contain_text(errorMsg)

@pytest.mark.integration
@pytest.mark.xfail(reason="assertion fails due to incorrect image")  
def test_account_is_nerfed(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    
    onLoginPage.submitLogin(SauceDemoData.problemUSN, SauceDemoData.password)
    expect(onProductListPage.product_image).to_have_attribute("src", SauceDemoData.PRD1_IMG_URL)

@pytest.mark.integration
def test_account_is_slow(page: Page):
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    
    onLoginPage.submitLogin(SauceDemoData.glitchedUSN, SauceDemoData.password)
    expect(onProductListPage.product_image).to_have_attribute("src", SauceDemoData.PRD1_IMG_URL)