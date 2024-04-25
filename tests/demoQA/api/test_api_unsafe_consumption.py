"""
OWASP API Security Top 10 2023 | API10:2023 Unsafe Consumption of APIs
src: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/
"""

import requests
import pytest
from demoQAUtils.data import DemoQA
from demoQAUtils.book_selection import BookSelection


book_id = BookSelection.select_a_book()


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
