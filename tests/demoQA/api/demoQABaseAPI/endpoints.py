from utils.urls import Accounts, Bookstore
from api.demoQABaseClient.base_client import BaseClient as bc
from utils.book_selection import BookSelection
from utils.data import DemoQA

book_id = BookSelection.select_a_book()


ENDPOINTS = {
    Accounts.AUTHORIZED_USER: bc.user_status('allowed'),
    Accounts.LOGIN_ENDPOINT: bc.user_status('allowed'),
    Accounts.TOKEN_ENDPOINT: bc.user_status('allowed'),
    Accounts.USER_ENDPOINT: bc.user_status('allowed'),
    Accounts.SELECTED_USER: bc.user_status('denied'),  # EXPECTED TO FAIL - A GOOD THING!
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

ENDPOINT_ROLES = {
    Accounts.AUTHORIZED_USER: {
        "user": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        "hacker": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        },
    Accounts.LOGIN_ENDPOINT: {
        "user": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        "hacker": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        },
    Accounts.TOKEN_ENDPOINT: {
        "user": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        "hacker": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        },
    Accounts.USER_ENDPOINT: {
        "user": {
            "GET": 200,
            "POST": 406,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        "hacker": {
            "GET": 200,
            "POST": 406,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        },
    Accounts.SELECTED_USER: {
        "user": {
            "GET": 401,
            "POST": 404,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 401
            },
        "hacker": {
            "GET": 401,
            "POST": 404,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 401
            },
        },
    Bookstore.BOOKS: {
        "user": {
            "GET": 200,
            "POST": 502,
            "PATCH": 502,
            "PUT": 502,
            "DELETE": 502
            },
        "hacker": {
            "GET": 502,
            "POST": 502,
            "PATCH": 502,
            "PUT": 502,
            "DELETE": 502
            },
        },
    Bookstore.SINGLE_BOOK+f"?ISBN={book_id}": {
        "user": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        "hacker": {
            "GET": 200,
            "POST": 404,
            "PATCH": 404,
            "PUT": 404,
            "DELETE": 404
            },
        },
    Bookstore.BOOKS+f"/{book_id}": {
        "user": {
            "GET": 200,
            "POST": 200,
            "PATCH": 404,
            "PUT": 400,
            "DELETE": 400
            },
        "hacker": {
            "GET": 200,
            "POST": 404,
            "PATCH": 404,
            "PUT": 400,
            "DELETE": 400
            },
    }
}
