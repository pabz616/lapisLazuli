"""
OWASP API Security Top 10 2023 | API1:2023 Broken Object Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
"""

import requests
import pytest
from demoQAUtils.data import APIDemoData


ENDPOINTS = {
    "/booking": {
        "admin": 200,
        "user": 200
    },
    
    "/auth": {
        "admin": 200,
        "user": 403
    }
}


@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
@pytest.mark.api
def test_broken_object_level_auth(endpoint, roles):
    for role, expected_status_code in roles.items():
        url = APIDemoData.BOOKER_URL + endpoint
        headers = {"Authorization": f"Bearer {get_token(role)}"}
        response = requests.get(url, headers=headers)
        assert response.status_code == expected_status_code, f"Access to {endpoint} for role {role} is broken"


def get_token(role):
    if role == "admin":
        return APIDemoData.BEARER_TOKEN
    else:
        return ""