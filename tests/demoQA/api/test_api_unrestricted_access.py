"""
OWASP API Security Top 10 2023 | API6:2023 Unrestricted Access to Sensitive Business Flows
src: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/
"""

import requests
import pytest
from demoQAUtils.data import DemoQA


USER_INFO = {
    f"/Account/v1/User/{DemoQA.userId}"
}


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", USER_INFO)
def test_sensitive_business_flows(endpoint):
    url = DemoQA.baseUrl + endpoint

    headers = {"Authorization": "Bearer foo123"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
