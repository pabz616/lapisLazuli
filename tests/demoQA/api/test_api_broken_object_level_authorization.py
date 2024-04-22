"""
OWASP API Security Top 10 2023 | API1:2023 Broken Object Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
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
    "/Account/v1/Login": status(),
    "/Account/v1/GenerateToken": status(),
    "/Account/v1/User": status(),
    f"/Account/v1/User/{pd.demoQAUserId}": { 
        "user": 401  # USER IS NOT LOGGED IN, ENDPOINT SHOULD NOT BE ACCESSIBLE
    },
    "/BookStore/v1/Books": status(),
    "/BookStore/v1/Book": status(),
    f"/books?book={book_id}": status()
}


@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
@pytest.mark.api
def test_broken_object_level_auth(endpoint, roles):
    for role, expected_status_code in roles.items():
        url = pd.baseUrl + endpoint
        headers = {"Authorization": f"Bearer {get_token(role)}"}
        response = requests.get(url, headers=headers)
        assert response.status_code == expected_status_code, f"Access to {endpoint} for role {role} is broken"
        assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
        
def get_token(role):
    if role == "user":
        return pd.demoQAToken
    elif role == "hacker":
        return pd.demoQATokenHacker
    else:
        return ""