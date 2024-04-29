from demoQAUtils.urls import Accounts, Bookstore
from api.demoQABaseClient.base_client import BaseClient as bc
from demoQAUtils.book_selection import BookSelection
from demoQAUtils.data import DemoQA

book_id = BookSelection.select_a_book()


ENDPOINTS = {
    Accounts.AUTHORIZED_USER: bc.user_status('allowed'),
    Accounts.LOGIN_ENDPOINT: bc.user_status('allowed'),
    Accounts.TOKEN_ENDPOINT: bc.user_status('allowed'),
    Accounts.USER_ENDPOINT: bc.user_status('allowed'),
    Accounts.SELECTED_USER: bc.user_status('denied'),
    Bookstore.BOOKS: bc.user_status('allowed'),
    Bookstore.SINGLE_BOOK+f"?ISBN={book_id}": bc.user_status('allowed'),
    Bookstore.BOOKS+f"/{book_id}": bc.user_status('allowed')
}

PUBLIC_ENDPOINTS = [
    Accounts.AUTHORIZED_USER,
    Accounts.LOGIN_ENDPOINT,
    Accounts.TOKEN_ENDPOINT,
    Accounts.USER_ENDPOINT,
    Bookstore.BOOKS,
    Bookstore.SINGLE_BOOK+f"?ISBN={book_id}",
    Bookstore.BOOKS+f"/{book_id}"
    ]

PRIVATE_ENDPOINTS = [
    Accounts.USER_ENDPOINT+f"/{DemoQA.userId}"
]