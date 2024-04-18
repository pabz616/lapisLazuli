"""
OWASP API Security Top 10 2023 | API1:2023 Broken Object Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


ENDPOINTS = {
    "/Account/v1/Login": {
        "user": 200
    },
    "/Account/v1/GenerateToken": {
        "user": 200
    },
    "/Account/v1/User": {
        "user": 200
    },
    f"/Account/v1/User/{pd.demoQAUserId}": {
        "user": 401  # USER IS NOT LOGGED IN, ENDPOINT SHOULD NOT BE ACCESSIBLE
    },
    
    "/BookStore/v1/Books": {
        "user": 200
    },
    "/books?book=9781449325862": {
        "user": 200
    }
}


@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
@pytest.mark.api
def test_broken_object_level_auth(endpoint, roles):
    for role, expected_status_code in roles.items():
        url = pd.baseUrl + endpoint
        headers = {"Authorization": f"Bearer {get_token(role)}"}
        response = requests.get(url, headers=headers)
        assert response.status_code == expected_status_code, f"Access to {endpoint} for role {role} is broken"
        
        
def get_token(role):
    if role == "user":
        return pd.demoQAToken
    elif role == "hacker":
        return pd.demoQATokenHacker
    else:
        return ""