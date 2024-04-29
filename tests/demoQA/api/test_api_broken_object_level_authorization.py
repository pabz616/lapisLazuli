"""
OWASP API Security Top 10 2023 | API1:2023 Broken Object Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
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
class TestBrokenObjectLevelAuthorization:
    @pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
    def test_broken_object_level_auth(self, endpoint, roles):
        for role, expected_status_code in roles.items():
            headers = {"Authorization": f"Bearer {client.get_token()}"}
            response = requests.get(endpoint, headers=headers)
            confirm.ok_response_status(response, 200), f"Access to {endpoint} for role {role} is broken"