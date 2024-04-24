"""
OWASP API Security Top 10 2023 | API10:2023 Unsafe Consumption of APIs
src: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/
"""

import requests
import pytest
import random
from demoQAUtils.data import DemoQA


book_catalog = [
    '9781449325862', '9781449331818', '9781449337711', '9781449365035',
    '9781491904244', '9781491950296', '9781593275846', '9781593277574'
    ]

book_id = random.choice(book_catalog)


PUBLIC_ENDPOINTS = [
    "/Account/v1/Authorized",
    "/Account/v1/GenerateToken",
    "/Account/v1/Login",
    "/Account/v1/User",
    f"/Account/v1/User/{DemoQA.userId}"
    "/BookStore/v1/Books"
    f"/BookStore/v1/Book?ISBN={book_id}",
    f"/BookStore/v1/Books/{book_id}",
    ]


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", PUBLIC_ENDPOINTS)
def test_unsafe_consumption(endpoint):
    url = DemoQA.baseUrl + endpoint

    # Replace with valid data for unsafe consumption ... this should not work
    data = {"input": "user_input"}
    response = requests.post(url, json=data)
    assert response.status_code != 200, "Unsafe consumption vulnerability detected"