"""
TEST ACCOUNT ENDPOINT
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd, DemoQA
from demoQAUtils.urls import Accounts

@pytest.mark.critical
@pytest.mark.api
class TestCriticalAccountEndpoints:
    def test_demoQA_login(self):
        response = requests.post(Accounts.LOGIN_ENDPOINT, json=DemoQA.data)
        assert response.status_code == 200, "Login endpoint is broken"
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)

    def test_demoQA_generate_token(self):
        response = requests.post(Accounts.TOKEN_ENDPOINT, json=DemoQA.data)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
        # TEST RESPONSE
        resp = response.json()
        assert resp["token"] is not None, "Token was not generated"
        assert resp["expires"] != "2024-04-23", "Token expired"
        assert resp["status"] == "Success", "Unsuccessful token"
        assert resp["result"] == "User authorized successfully.", "Unsuccessful authorization"
    
    def test_demoQA_create_user_validation_for_blank_password(self):
        data = {"userName": pd.email, "password": ''}
        response = requests.post(Accounts.USER_ENDPOINT, json=data)
        assert response.status_code == 400, "Bug! Blank password was allowed"


@pytest.mark.high
@pytest.mark.api
class TestHighAccountEndpoints:
    def test_demoQA_create_user_is_successful(self):
        response = requests.post(Accounts.USER_ENDPOINT, json=DemoQA.newUserData)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
        # TEST RESPONSE
        resp = response.json()
        assert response.status_code == 201, "Bug! New User was not created"
        assert resp["userID"] is not None, "UserID is null"
        assert resp["username"] is not None, "Username is null"
        assert resp["books"] == []
        
    def test_demoQA_get_new_user_is_unsuccessful(self):
        response = requests.post(Accounts.USER_ENDPOINT, json=DemoQA.newUserData)
        assert response.status_code == 201, 'Error: {0}'.format(response.status_code)
        
        resp = response.json()
        UUID = resp["userID"]
        new_user_response = requests.get(f"{Accounts.USER_ENDPOINT}/{UUID}")
        assert new_user_response.status_code == 401, 'Error: {0}'.format(response.status_code)
  
    def test_demoQA_delete_user_is_not_successful(self):
        response = requests.post(Accounts.USER_ENDPOINT,  json=DemoQA.newUserData)
        assert response.status_code == 201, "Bug! New User was not created"
        
        resp = response.json()
        UUID = resp["userID"]
        delete_response = requests.delete(f"{Accounts.USER_ENDPOINT}/{UUID}")
        assert delete_response.status_code == 401, 'Error: {0}'.format(response.status_code)

    def test_demoQA_create_user_validation_for_weak_password(self):
        response = requests.post(Accounts.USER_ENDPOINT,  json=DemoQA.newUserData)
        assert response.status_code != 200, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
        
    def test_demoQA_create_user_validation_for_existing_user(self):
        response = requests.post(Accounts.USER_ENDPOINT,  json=DemoQA.newUserData)
        assert response.status_code == 406, 'Error: {0}'.format(response.status_code)
        assert response.elapsed.total_seconds() < pd.response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
