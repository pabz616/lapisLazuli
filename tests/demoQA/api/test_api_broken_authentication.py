"""
OWASP API Security Top 10 2023 | API2:2023 Broken Authentication
src: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


loginEndpoint = pd.baseUrl+'/Account/v1/Login'
tokenEndpoint = pd.baseUrl+'/Account/v1/GenerateToken'


@pytest.mark.high_priority
@pytest.mark.api
def test_login_endpoint():
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(loginEndpoint, json=data)
    assert response.status_code == 200, "Login endpoint is broken"


@pytest.mark.high_priority
@pytest.mark.api
def test_generate_token():
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(tokenEndpoint, json=data)
    
    resp = response.json()
    assert response.status_code == 200, "Token was not generated"
    assert resp["token"] is not None, "Token was not generated"
    assert resp["expires"] != "2024-04-23", "Token expired"
    assert resp["status"] == "Success", "Unsuccessful token"
    assert resp["result"] == "User authorized successfully.", "Unsuccessful authorization"
    
# Add more tests as needed for specific broken authentication scenarios