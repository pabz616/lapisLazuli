"""
OWASP API Security Top 10 2023 | API3:2023 Broken Object Property Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/
"""

import requests
import pytest
from api.demoQAClient.account_client import AccountsClient
from api.demoQABaseAPI.endpoints import ENDPOINTS
from api.demoQAAssertions import assertions as confirm

client = AccountsClient()


@pytest.mark.security
@pytest.mark.critical
@pytest.mark.api
class TestBrokenObjectPropertyLevelAuthorization:
    @pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
    def test_broken_object_property_level_auth(self, endpoint, roles):
        for role, methods in roles.items():
            for method, expected_status_code in methods.items():
                headers = {"Authorization": f"Bearer {client.get_token()}"}
                if method == "GET":
                    response = requests.get(endpoint, headers=headers)
                elif method == "PUT":
                    # Assuming we are sending some JSON data in the PUT request
                    data = {"property": "new_value"}
                    response = requests.put(endpoint, json=data, headers=headers)
                confirm.ok_response_status(response, 200), f"Access to {method} {endpoint} for role {role} is broken"