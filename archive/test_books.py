import pytest
from typing import Generator
from playwright.sync_api import Playwright, sync_playwright, Page, APIRequestContext, expect
from sauceUtils.data import SauceDemoData

"""TESTING WITH MOCK API"""
booksURL = 'https://demoqa.com/books'
def test_select_single_book(page):
    """Using a mock, select a single book in the application."""
    book_title = "Designing Evolvable Web APIs with ASP.NET"
    page.route(
        "**/BookStore/v1/Books",
        lambda route: route.fulfill(path="./data/books.json")
    )
    page.goto(booksURL)
    book = page.wait_for_selector(
        f"a >> text={book_title}"
    )
    book.click()
    visible = page.wait_for_selector(
        f"label >> text={book_title}"
    ).is_visible()

    assert visible

    with page.expect_response("**/BookStore/v1/Books") as response:
        page.goto(booksURL)
    assert response.value.ok