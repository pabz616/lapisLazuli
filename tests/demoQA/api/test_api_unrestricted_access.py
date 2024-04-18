"""
OWASP API Security Top 10 2023 | API6:2023 Unrestricted Access to Sensitive Business Flows
src: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


ENDPOINTS = [
    "/Account/v1/Login",
    "/Account/v1/GenerateToken",
    "/Account/v1/User",
    "/BookStore/v1/Books"
    # f"/Account/v1/User/{pd.demoQAUserId}"  # REQUIRES USER LOGIN
    ]


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_sensitive_business_flows(endpoint):
    url = pd.baseUrl + endpoint

    headers = {"Authorization": f"Bearer {pd.demoQAToken}"}
    response = requests.get(url, headers=headers)
    assert response.status_code != 401, f"Unauthorized access to {endpoint}"