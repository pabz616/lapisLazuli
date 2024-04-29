"""
OWASP API Security Top 10 2023 | API5:2023 Broken Function Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/
"""

import pytest
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm

client = AccountsClient()


@pytest.mark.high
@pytest.mark.security
@pytest.mark.api
class TestBrokenFunctionLevelAuthorization:
    def test_generate_token_with_improper_update_function(self):
        response = client.generate_token_with_PUT()
        confirm.not_found_response_status(response, 404), "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"
    
    def test_generate_token_with_improper_partial_update_function(self):
        response = client.generate_token_with_PATCH()
        confirm.not_found_response_status(response, 404), "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"
        
    def test_generate_token_with_improper_options_function(self):
        response = client.generate_token_with_OPTIONS()
        confirm.ok_response_status(response, 200), "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"