from playwright.sync_api import sync_playwright, Page
from utils.data import * 
import pytest
import re


def test_title(page: Page):
    page.goto(sauceURL)
    assert page.title() == 'Swag Labs'
    