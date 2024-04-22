"""
TEST ACCOUNT ENDPOINT
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd

response_limit = float(1.0)  # seconds


@pytest.mark.critical
@pytest.mark.api
def test_demoQA_login():
    loginEndpoint = pd.baseUrl+'/Account/v1/Login'
    
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(loginEndpoint, json=data)
    assert response.status_code == 200, "Login endpoint is broken"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)


@pytest.mark.critical
@pytest.mark.api
def test_demoQA_generate_token():
    tokenEndpoint = pd.baseUrl+'/Account/v1/GenerateToken'
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(tokenEndpoint, json=data)
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    # TEST RESPONSE
    resp = response.json()
    assert response.status_code == 200, "Token was not generated"
    assert resp["token"] is not None, "Token was not generated"
    assert resp["expires"] != "2024-04-23", "Token expired"
    assert resp["status"] == "Success", "Unsuccessful token"
    assert resp["result"] == "User authorized successfully.", "Unsuccessful authorization"
    

@pytest.mark.high
@pytest.mark.api
def test_demoQA_create_user_is_successful():
    userEndpoint = pd.baseUrl+'/Account/v1/User'
    data = {"userName": pd.email, "password": pd.demoQANewUser}
    response = requests.post(userEndpoint, json=data)
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    # TEST RESPONSE
    resp = response.json()
    assert response.status_code == 201, "Bug! New User was not created"
    assert resp["userID"] is not None, "UserID is null"
    assert resp["username"] is not None, "Username is null"
    assert resp["books"] == []
    
    
@pytest.mark.high
@pytest.mark.api
def test_demoQA_get_new_user_is_unsuccessful():
    data = {"userName": pd.email, "password": pd.demoQANewUser}
    response = requests.post(pd.baseUrl+'/Account/v1/User', json=data)
    resp = response.json()
    assert response.status_code == 201, "Bug! New User was not created"
    
    UUID = resp["userID"]
    new_user_response = requests.get(pd.baseUrl+f"/Account/v1/User/{UUID}")
    assert new_user_response.status_code == 406, "Bug! Able to retrieve user details"
    assert new_user_response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    

@pytest.mark.high
@pytest.mark.api
def test_demoQA_delete_user_is_not_successful():
    data = {"userName": pd.email, "password": pd.demoQANewUser}
    create_response = requests.post(pd.baseUrl+'/Account/v1/User', json=data)
    assert create_response.status_code == 201, "Bug! New User was not created"
    
    resp = create_response.json()
    UUID = resp["userID"]

    delete_response = requests.delete(pd.baseUrl+f"/Account/v1/User/{UUID}")
    assert delete_response.status_code == 401, "Bug! New User can be deleted"
    assert delete_response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    
@pytest.mark.critical
@pytest.mark.api
def test_demoQA_create_user_validation_for_blank_password():
    data = {"userName": pd.email, "password": ''}
    response = requests.post(pd.baseUrl+'/Account/v1/User', json=data)
    assert response.status_code == 400, "Bug! Blank password was allowed"


@pytest.mark.high
@pytest.mark.api
def test_demoQA_create_user_validation_for_weak_password():
    data = {"userName": pd.email, "password": pd.demoQANewUser}
    response = requests.post(pd.baseUrl+'/Account/v1/User', json=data)
    assert response.status_code != 200, "Bug! Weak password was allowed"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)
    
    
@pytest.mark.high
@pytest.mark.api
def test_demoQA_create_user_validation_for_existing_user():
    data = {"userName": pd.demoQAUsn, "password": pd.demoQAPwd}
    response = requests.post(pd.baseUrl+'/Account/v1/User', json=data)
    assert response.status_code == 406, "Bug! No check for duplicate user"
    assert response.elapsed.total_seconds() < response_limit, "API Response: {0}".format(response.elapsed.total_seconds)