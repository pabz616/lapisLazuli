"""
OWASP API Security Top 10 2023 | API5:2023 Broken Function Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/
"""

import requests
import pytest
from demoQAUtils.data import DemoQA
from demoQAUtils.urls import Accounts


@pytest.mark.high
@pytest.mark.api
class TestBrokenFunctionLevelAuthorization:
    def test_generate_token_with_improper_function_PUT(self):
        response = requests.put(Accounts.TOKEN_ENDPOINT, json=DemoQA.loginData)
        assert response.status_code == 404, 'Error: {0}'.format(response.status_code)

    def test_modify_user_with_improper_function_DELETE(self):
        response = requests.delete(f"{Accounts.USER_ENDPOINT}/{DemoQA.userId}", json=DemoQA.adminData)
        assert response.status_code == 401, 'Error: {0}'.format(response.status_code)
        
    def test_generate_token_with_improper_function_PATCH(self):
        response = requests.patch(Accounts.TOKEN_ENDPOINT, json=DemoQA.loginData)
        assert response.status_code == 404, 'Error: {0}'.format(response.status_code)

    def test_generate_token_with_improper_function_OPTIONS(self):
        response = requests.options(Accounts.TOKEN_ENDPOINT, json=DemoQA.loginData)        
        assert response.status_code == 200,  'Error: {0}'.format(response.status_code)