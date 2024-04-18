"""
OWASP API Security Top 10 2023 | API8:2023 Security Misconfiguration
src: https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/
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

PUBLIC_ENDPOINTS = [
    "/Account/v1/Authorized",
    "/Account/v1/Login",
    "/Account/v1/GenerateToken",
    "/Account/v1/User",
    "/BookStore/v1/Books",
    f"/books?book={book_id}"
    ]

PRIVATE_ENDPOINTS = [
    f"/Account/v1/User/{pd.demoQAUserId}"
]


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("endpoint", PUBLIC_ENDPOINTS)
def test_unprotected_endpoints(endpoint):
    url = pd.baseUrl + endpoint
    response = requests.get(url)
    assert response.status_code == 200, f"Endpoint {endpoint} is unprotected."


# Test for missing authentication/authorization mechanisms
@pytest.mark.parametrize("endpoint", PRIVATE_ENDPOINTS)
def test_authentication_mechanism(endpoint):
    url = pd.baseUrl + endpoint
    response = requests.get(url)
    assert response.status_code == 401, "Authentication mechanism is missing."


# Test for exposure of sensitive data
def test_sensitive_data_exposure():
    url = pd.baseUrl + f"/Account/v1/User/{pd.demoQAUserId}"
    response = requests.get(url)
    assert response.status_code != 200, "Sensitive data should not be exposed."
