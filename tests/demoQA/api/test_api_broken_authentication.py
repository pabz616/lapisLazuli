"""
OWASP API Security Top 10 2023 | API2:2023 Broken Authentication
src: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/
"""

import pytest
import json
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm


client = AccountsClient()


@pytest.mark.critical
@pytest.mark.security
@pytest.mark.api
class TestBrokenAuthentication:
    def test_login_endpoint(self):
        response = client.login_user()
        confirm.ok_response_status(response, 200)
        
    def test_generate_token_is_successful(self):
        response = client.generate_token()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.created_token(data)

    def test_generate_token_is_unsuccessful(self):        
        response = client.generate_token_unsuccessfully()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.created_token_failed(data)
             