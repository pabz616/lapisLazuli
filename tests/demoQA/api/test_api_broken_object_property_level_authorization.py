"""
OWASP API Security Top 10 2023 | API3:2023 Broken Object Property Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/
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
        "user": 200
    }
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


def get_token(role):
    if role == "user":
        return pd.demoQAToken
    else:
        return ""