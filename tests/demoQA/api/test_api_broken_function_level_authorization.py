"""
OWASP API Security Top 10 2023 | API5:2023 Broken Function Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


tokenEndpoint = pd.baseUrl+'/Account/v1/GenerateToken'
accountEndpoint = pd.baseUrl+f"/Account/v1/User/{pd.demoQAUserId}"


@pytest.mark.high
@pytest.mark.api
def test_generate_token_with_improper_function_delete():
    data = {"userName": pd.demoQANewUser, "password": pd.demoQANewUser}
    response = requests.delete(tokenEndpoint, json=data)
    assert response.status_code == 404, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"


@pytest.mark.high
@pytest.mark.api
def test_modify_user_with_improper_function_delete():
    data = {"userName": "admin", "password": pd.demoQAPwd}
    response = requests.delete(accountEndpoint, json=data)
    assert response.status_code == 401, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"


@pytest.mark.high
@pytest.mark.api    
def test_generate_token_with_improper_function_patch():
    data = {"userName": pd.demoQANewUser, "password": pd.demoQANewUser}
    response = requests.patch(tokenEndpoint, json=data)
    assert response.status_code == 404, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"
    

@pytest.mark.high
@pytest.mark.api    
def test_generate_token_with_improper_function_put():
    data = {"userName": pd.demoQANewUser, "password": pd.demoQANewUser}
    response = requests.put(tokenEndpoint, json=data)
    assert response.status_code == 404, "BROKEN FUNCTION LEVEL AUTHORIZATION VULNERABILITY FOUND!"