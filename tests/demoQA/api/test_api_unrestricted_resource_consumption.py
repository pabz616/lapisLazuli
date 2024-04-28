"""
OWASP API Security Top 10 2023 | API4:2023 Unrestricted Resource Consumption
src: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
"""

import requests
import pytest
from demoQAUtils.data import DemoQA, ProjectData as pd
from demoQAUtils.book_selection import BookSelection


book_id = BookSelection.select_a_book()


def status():
    return {"user": 200}


ENDPOINTS = {
    "/Account/v1/Authorized": status(),
    "/Account/v1/generate_token": status(),
    "/Account/v1/User": status(),  
    "/Account/v1/Login": status(), 
    f"/Account/v1/User/{DemoQA.userId}": status(),
    "/BookStore/v1/Books": status(),
    f"/BookStore/v1/Book?ISBN={book_id}": status(),
    f"/BookStore/v1/Books/{book_id}": status(),
}


@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
@pytest.mark.api
def test_broken_object_level_auth(endpoint, roles):
    for role, expected_status_code in roles.items():
        url = DemoQA.baseUrl + endpoint
        
        # Adjust the data sent in the request to simulate a resource-intensive operation
        data = {"input": pd.randomString * 100000}  # Simulate a large input data
        response = requests.post(url, json=data)
        assert response.status_code != 429, "Request was rate-limited"