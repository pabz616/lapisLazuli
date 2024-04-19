import pytest
from typing import Generator
from playwright.sync_api import Playwright, sync_playwright, Page, APIRequestContext, expect
from sauceUtils.data import SauceDemoData
import sys
  

def test_network_response(page: Page) -> None:
    """Pulls in all requests from a given url"""
    
    DemoURL = 'https://demoqa.com/books'
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    
    #RESPONSE CLEAN-UP
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.js", lambda route: route.abort())
    page.route("**/*.png", lambda route: route.abort())
    page.route("**/*.css", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/*.min.css", lambda route: route.abort())
    page.goto(DemoURL)