"""
OWASP API Security Top 10 2023 | API4:2023 Unrestricted Resource Consumption
src: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
"""

import requests
import pytest
from utils.data import ProjectData as pd
from api.demoQABaseAPI.endpoints import ENDPOINTS


@pytest.mark.security
@pytest.mark.high
@pytest.mark.api
class TestUnrestrictedResourceConsumption:    
    @pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
    def test_rate_limit_exceeded_for_operation(self, endpoint, roles):
        for role, expected_status_code in roles.items():
             
            # Adjust the data sent in the request to simulate a resource-intensive operation
            data = {"input": pd.randomString * 100000}  # Simulate a large input data
            response = requests.post(endpoint, json=data)
            assert response.status_code == 413, 'Error: {0}'.format(response.status_code)