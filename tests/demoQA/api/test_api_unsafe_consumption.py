"""
OWASP API Security Top 10 2023 | API10:2023 Unsafe Consumption of APIs
src: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


PUBLIC_ENDPOINTS = [
    "/Account/v1/Login",
    "/Account/v1/GenerateToken",
    "/Account/v1/User",
    "/BookStore/v1/Books"
    ]


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", PUBLIC_ENDPOINTS)
def test_unsafe_consumption(endpoint):
    url = pd.baseUrl + endpoint

    # Replace with valid data for unsafe consumption ... this should not work
    data = {"input": "user_input"}
    response = requests.post(url, json=data)
    assert response.status_code != 200, "Unsafe consumption vulnerability detected"