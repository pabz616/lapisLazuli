"""
OWASP API Security Top 10 2023 | API2:2023 Broken Authentication
src: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd

response_limit = float(1.0)


loginEndpoint = pd.baseUrl+'/Account/v1/Login'
tokenEndpoint = pd.baseUrl+'/Account/v1/GenerateToken'


@pytest.mark.critical
@pytest.mark.api
def test_login_endpoint():
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(loginEndpoint, json=data)
    assert response.status_code == 200, "Login endpoint is broken"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)


@pytest.mark.critical
@pytest.mark.api
def test_generate_token_is_successful():
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(tokenEndpoint, json=data)
    resp = response.json()
    
    assert response.status_code == 200, "Token was not generated"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    assert resp["token"] is not None, "Token was not generated"
    assert resp["expires"] != "2024-04-23", "Token expired"
    assert resp["status"] == "Success", "Unsuccessful token"
    assert resp["result"] == "User authorized successfully.", "Unsuccessful authorization"

    
def test_generate_token_is_unsuccessful():
    data = {"userName": pd.demoQANewUser, "password": pd.demoQANewUser}
    response = requests.post(tokenEndpoint, json=data)
    
    resp = response.json()
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    assert resp["status"] == "Failed"
    assert resp["result"] == "User authorization failed."
    

# BROKEN FUNCTION LEVEL AUTHORIZATION
def test_generate_token_with_improper_function():
    data = {"userName": pd.demoQANewUser, "password": pd.demoQANewUser}
    response = requests.delete(tokenEndpoint, json=data)
    assert response.status_code == 404, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)