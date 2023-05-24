from playwright.sync_api import sync_playwright, Page, expect
from utils.data import SauceDemoData
import pytest
import re
from models.saucedemo_login import LoginPage
from models.saucedemo_PLP import ProductListPage

@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto(SauceDemoData.sauceURL)
    yield

def test_title(page: Page):
    expect(page).to_have_title(re.compile("Swag Labs"))
    
def test_login_UI(page: Page):
    onLoginPage = LoginPage(page)
    onLoginPage.checkUI()

def test_account_is_valid(page: Page):    
    onLoginPage = LoginPage(page)
    onProductListPage = ProductListPage(page)
    onLoginPage.submitLogin(SauceDemoData.validUSN, SauceDemoData.password)
    
    #REDIRECT TO PRODUCT_LIST
    expect(page).to_have_url(re.compile(".*inventory"))
    onProductListPage.checkUI()

def test_account_is_locked_out(page: Page):
    error = page.locator('[data-test="error"]')
    errorMsg = "Epic sadface: Sorry, this user has been locked out."
    
    onLoginPage = LoginPage(page)
    onLoginPage.submitLogin(SauceDemoData.lockedOutUSN, SauceDemoData.password)
    expect(error).to_be_visible()
    expect(error).to_contain_text(errorMsg)
    
def test_account_is_nerfed(page: Page):
    pass

def test_account_is_slow(page: Page):
    pass