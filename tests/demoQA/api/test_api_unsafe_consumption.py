"""
OWASP API Security Top 10 2023 | API10:2023 Unsafe Consumption of APIs
src: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/
"""

import requests
import pytest
from api.demoQABaseAPI.endpoints import PUBLIC_ENDPOINTS, PRIVATE_ENDPOINTS
from api.demoQAAssertions import assertions as confirm


@pytest.mark.security
@pytest.mark.high
@pytest.mark.api
class TestUnsafeConsumption:
    @pytest.mark.parametrize("endpoint", PUBLIC_ENDPOINTS)
    def test_api_security_posture_public_endpoints(self, endpoint):
        
        # Replace with valid data for unsafe consumption ... this should not work
        data = {"genome": "ACTAGTAG__TTGADDAAIICCTT…"}
        response = requests.post(endpoint, json=data)
        
        # TODO - Needs a better assertion. Not all APIs yield the same error
        assert response.status_code != 200, 'Error: {0}'.format(response.status_code) 
    
    @pytest.mark.parametrize("endpoint", PRIVATE_ENDPOINTS)
    def test_api_security_posture_for_private_endpoints(self, endpoint):
        
        # Replace with valid data for unsafe consumption ... this should not work
        data = {"genome": "ACTAGTAG__TTGADDAAIICCTT…"}
        response = requests.post(endpoint, json=data)
        assert response.status_code == 502, 'Error: {0}'.format(response.status_code) 
