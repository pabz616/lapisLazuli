"""
OWASP API Security Top 10 2023 | API3:2023 Broken Object Property Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/
"""

import requests
import pytest
from api.demoQAClient.account_client import AccountsClient
from api.demoQABaseAPI.endpoints import ENDPOINT_ROLES
from demoQAUtils.data import DemoQA

client = AccountsClient()


@pytest.mark.security
@pytest.mark.critical
@pytest.mark.api
@pytest.mark.parametrize("endpoint, roles", ENDPOINT_ROLES.items())
def test_broken_object_property_level_auth(endpoint, roles):
    for role, methods in roles.items():
        for method, expected_status_code in methods.items():
            headers = {"Authorization": f"Bearer {client.get_token(role)}"}
            
            if method == "GET":
                data = {"userId": DemoQA.userId, "isbn": "9578984058653"}
                response = requests.get(endpoint, json=data, headers=headers)
            elif method == "POST":
                data = DemoQA.loginData
                response = requests.post(endpoint, json=data, headers=headers)
            elif method == "PATCH":
                data = {"property": "new_value"}
                response = requests.patch(endpoint, json=data, headers=headers)
            elif method == "PUT":
                data = {"property": "new_value"}
                response = requests.put(endpoint, json=data, headers=headers)
            elif method == "DELETE":
                response = requests.delete(endpoint, headers=headers)
            assert response.status_code == expected_status_code, f"Access to {method} {endpoint} for role {role} is broken"
