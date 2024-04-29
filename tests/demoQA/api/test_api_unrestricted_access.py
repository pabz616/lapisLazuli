"""
OWASP API Security Top 10 2023 | API6:2023 Unrestricted Access to Sensitive Business Flows
src: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/
"""

import requests
import pytest
from api.demoQABaseAPI.endpoints import PRIVATE_ENDPOINTS
from api.demoQAAssertions import assertions as confirm


@pytest.mark.security
@pytest.mark.high
@pytest.mark.api
class TestUnrestrictedAccess:
    @pytest.mark.parametrize("endpoint", PRIVATE_ENDPOINTS)
    def test_sensitive_business_flows(self, endpoint):
        headers = {"Authorization": "Bearer foo123"}
        response = requests.get(endpoint, headers=headers)
        confirm.unauthorized_status(response, 401)
