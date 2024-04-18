"""
OWASP API Security Top 10 2023 | API4:2023 Unrestricted Resource Consumption
src: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd
import random


book_catalog = [
    '9781449325862', '9781449331818', '9781449337711', '9781449365035',
    '9781491904244', '9781491950296', '9781593275846', '9781593277574'
    ]

book_id = random.choice(book_catalog)
print(book_id)


def status():
    return {
            "user": 200
        }


ENDPOINTS = {
    "/Account/v1/Login": status(),
    "/Account/v1/GenerateToken": status(),
    "/Account/v1/User": status(),
    "/BookStore/v1/Books": status(),
    f"/books?book={book_id}": status()
}


@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
@pytest.mark.api
def test_broken_object_level_auth(endpoint, roles):
    for role, expected_status_code in roles.items():
        url = pd.baseUrl + endpoint
        
        # Adjust the data sent in the request to simulate a resource-intensive operation
        data = {"input": pd.randomString * 100000}  # Simulate a large input data
        response = requests.post(url, json=data)
        assert response.status_code != 429, "Request was rate-limited"
