"""
OWASP API Security Top 10 2023 | API8:2023 Security Misconfiguration
src: https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/
"""
import requests
import pytest
from api.demoQABaseAPI.endpoints import PUBLIC_ENDPOINTS, PRIVATE_ENDPOINTS
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm

client = AccountsClient()


@pytest.mark.security
@pytest.mark.high
@pytest.mark.api
class TestSecurityMisconfiguration:
    @pytest.mark.parametrize("endpoint", PUBLIC_ENDPOINTS)
    def test_unprotected_endpoints(self, endpoint):
        response = requests.get(endpoint)
        confirm.ok_response_status(response, 200), f"Endpoint {endpoint} is unprotected."

    # Test for missing authentication/authorization mechanisms
    @pytest.mark.parametrize("endpoint", PRIVATE_ENDPOINTS)
    def test_authentication_mechanism(self, endpoint):
        response = requests.get(endpoint)
        confirm.unauthorized_status(response, 401),  f"Authentication mechanism for {endpoint} is missing."
    
    # Test for exposure of sensitive data
    def test_sensitive_data_exposure(self):
        response = client.get_user_account_unauthorized_access()
        confirm.unauthorized_status(response, 401), "Sensitive data should not be exposed."
