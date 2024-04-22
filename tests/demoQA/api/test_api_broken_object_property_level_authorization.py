"""
OWASP API Security Top 10 2023 | API3:2023 Broken Object Property Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/
"""

import requests
import pytest
import random
from demoQAUtils.data import ProjectData as pd

response_limit = float(1.0)  # seconds

book_catalog = [
    '9781449325862', '9781449331818', '9781449337711', '9781449365035',
    '9781491904244', '9781491950296', '9781593275846', '9781593277574'
    ]

book_id = random.choice(book_catalog)


def status():
    return {"user": 200}


ENDPOINTS = {
    "/Account/v1/Authorized": status(),
    "/Account/v1/GenerateToken": status(),
    "/Account/v1/User": status(),  
    f"/Account/v1/User/{pd.demoQAUserId}": status(),
    "/Account/v1/Login": status(), 
    "/BookStore/v1/Books": status(),
    "/BookStore/v1/Book": status(),
    f"/books?book={book_id}": status()
}


@pytest.mark.high
@pytest.mark.api
# Test for Broken Object Property Level Authorization
@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
def test_broken_object_property_level_auth(endpoint, roles):
    def test_broken_object_property_level_auth(endpoint, roles):
        for role, methods in roles.items():
            for method, expected_status_code in methods.items():
                url = pd.baseUrl + endpoint
                headers = {"Authorization": f"Bearer {get_token(role)}"}
                if method == "GET":
                    response = requests.get(url, headers=headers)
                elif method == "PUT":
                    # Assuming we are sending some JSON data in the PUT request
                    data = {"property": "new_value"}
                    response = requests.put(url, json=data, headers=headers)
                assert response.status_code == expected_status_code, f"Access to {method} {endpoint} for role {role} is broken"
                assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)


def get_token(role):
    if role == "user":
        return pd.demoQAToken
    else:
        return ""