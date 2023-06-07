from playwright.sync_api import sync_playwright, Page, expect
import pytest
import re
from sauceLocators.page_elements import *
from sauceUtils.data import SauceDemoData


@pytest.mark.unit_test
@pytest.fixture(scope="function", autouse=True)
#use --browser-channel "chrome" to run tests in chrome, not chromium

def before_each(page: Page):
    page.goto(SauceDemoData.sauceURL) #start
    yield

#LOGIN PAGE    
def test_loginForm_has_url(page: Page):
    expect(page).to_have_url(re.compile(SauceDemoData.sauceURL))
    
def test_loginForm_has_title(page: Page):
    expect(page).to_have_title(re.compile(SauceDemoData.pageTitle))
    
def test_loginForm_has_logo(page: Page):
    expect(page.locator(SauceDemoPageLocators.SAUCE_LOGO)).to_be_visible()      

#USERNAME INPUT
def test_loginForm_username_input_is_visible(page: Page):
    expect(page.locator(SauceDemoPageLocators.USN_INPUT)).to_be_visible()

def test_loginForm_username_input_is_not_populated(page: Page):
    expect(page.locator(SauceDemoPageLocators.USN_INPUT)).to_be_empty()
    
def test_loginForm_username_input_is_editable(page: Page):
    expect(page.locator(SauceDemoPageLocators.USN_INPUT)).to_be_editable()
    
def test_loginForm_username_input_has_id(page: Page, element_id="user-name"):
    expect(page.locator(SauceDemoPageLocators.USN_INPUT)).to_have_id(element_id)

def test_loginForm_username_input_has_hint_text(page: Page):
    expect(page.locator(SauceDemoPageLocators.USN_INPUT)).to_have_attribute("placeholder", "Username")

#PASSWORD INPUT
def test_loginForm_password_input_is_visible(page: Page):
    expect(page.locator(SauceDemoPageLocators.PWD_INPUT)).to_be_visible()

def test_loginForm_password_input_is_not_populated(page: Page):
    expect(page.locator(SauceDemoPageLocators.PWD_INPUT)).to_be_empty()
    
def test_loginForm_password_input_is_editable(page: Page):
    expect(page.locator(SauceDemoPageLocators.PWD_INPUT)).to_be_editable()
    
def test_loginForm_password_input_has_id(page: Page, element_id="password"):
    expect(page.locator(SauceDemoPageLocators.PWD_INPUT)).to_have_id(element_id)

def test_loginForm_password_input_has_hint_text(page: Page):
    expect(page.locator(SauceDemoPageLocators.PWD_INPUT)).to_have_attribute("placeholder", "Password")
    
#LOGIN BUTTON
def test_loginForm_submit_button_is_displayed(page: Page):
    expect(page.locator(SauceDemoPageLocators.SUBMIT_BTN)).to_be_visible()

def test_loginForm_submit_button_is_actionable(page: Page):
    expect(page.locator(SauceDemoPageLocators.SUBMIT_BTN)).not_to_be_disabled()     

def test_loginForm_submit_button_has_value(page: Page):
    expect(page.locator(SauceDemoPageLocators.SUBMIT_BTN)).to_have_value("Login")