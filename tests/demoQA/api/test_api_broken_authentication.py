"""
OWASP API Security Top 10 2023 | API2:2023 Broken Authentication
src: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/
"""

import requests
import pytest
from demoQAUtils.data import DemoQA
from demoQAUtils.urls import Accounts


@pytest.mark.critical
@pytest.mark.api
class TestBrokenAuthentication:
    def test_login_endpoint(self):
        response = requests.post(Accounts.LOGIN_ENDPOINT, json=DemoQA.loginData)
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)

    def test_generate_token_is_successful(self):
        response = requests.post(Accounts.TOKEN_ENDPOINT, json=DemoQA.loginData)
        resp = response.json()
        
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)        
        assert resp["token"] is not None, "Token was not generated"
        assert resp["expires"] != "2024-04-23", "Token expired"
        assert resp["status"] == "Success", "Unsuccessful token"
        assert resp["result"] == "User authorized successfully.", "Unsuccessful authorization"

    def test_generate_token_is_unsuccessful(self):
        response = requests.post(Accounts.TOKEN_ENDPOINT, json=DemoQA.newUserData)
        
        resp = response.json()
        assert response.status_code == 200, 'Error: {0}'.format(response.status_code)        
        assert resp["status"] == "Failed"
        assert resp["result"] == "User authorization failed."
        
    # BROKEN FUNCTION LEVEL AUTHORIZATION
    def test_generate_token_with_improper_function(self):
        response = requests.put(Accounts.TOKEN_ENDPOINT, json=DemoQA.newUserData)
        assert response.status_code == 404, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"