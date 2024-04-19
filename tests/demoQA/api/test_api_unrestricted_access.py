"""
OWASP API Security Top 10 2023 | API6:2023 Unrestricted Access to Sensitive Business Flows
src: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/
"""

import requests
import pytest
import random
from demoQAUtils.data import ProjectData as pd


book_catalog = [
    '9781449325862', '9781449331818', '9781449337711', '9781449365035',
    '9781491904244', '9781491950296', '9781593275846', '9781593277574'
    ]

book_id = random.choice(book_catalog)

ENDPOINTS = {
    "/Account/v1/Authorized",
    "/Account/v1/GenerateToken",
    "/Account/v1/User",  
    "/Account/v1/Login", 
    f"/Account/v1/User/{pd.demoQAUserId}",
    "/BookStore/v1/Books",
    "/BookStore/v1/Book",
    f"/books?book={book_id}"
}


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_sensitive_business_flows(endpoint):
    url = pd.baseUrl + endpoint

    headers = {"Authorization": f"Bearer {pd.demoQAToken}"}
    response = requests.get(url, headers=headers)
    assert response.status_code != 401, f"Unauthorized access to {endpoint}"