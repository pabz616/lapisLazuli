"""
TEST ACCOUNT ENDPOINT
"""

import pytest
import json
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm

client = AccountsClient()


@pytest.mark.critical
@pytest.mark.api
class TestCriticalAccountEndpoints:
    def test_demoQA_login(self):
        response = client.authenticate_user()
        confirm.ok_response_status(response, 200)
        confirm.api_response_time

    def test_demoQA_generate_token(self):
        response = client.generate_token()
        data = json.loads(response.text)
        confirm.ok_response_status(response, 200)
        confirm.created_token(data)
        confirm.api_response_time
        
    def test_demoQA_create_user_validation_for_blank_password(self):
        response = client.create_user_account_blank_password()
        confirm.validation_response_status(response, 400)
        confirm.api_response_time


@pytest.mark.high
@pytest.mark.api
class TestHighAccountEndpoints: 
    def test_demoQA_create_user_is_successful(self):
        response = client.create_user_account()
        data = json.loads(response.text)
        confirm.created_status(response, 201)
        confirm.created_account(data)
        confirm.api_response_time
                             
    def test_demoQA_get_new_user_is_unsuccessful(self):
        response = client.get_user_account_unauthorized_access()
        confirm.unauthorized_status(response, 401)
     
    def test_demoQA_delete_user_is_not_successful(self):
        response = client.delete_user_account()
        confirm.unauthorized_status(response, 401)
        confirm.api_response_time
        
    def test_demoQA_create_user_validation_for_weak_password(self):
        response = client.create_user_account_weak_password()
        confirm.validation_response_status(response, 400)
        confirm.api_response_time
         
    def test_demoQA_create_user_validation_for_existing_user(self):
        response = client.create_user_account_existing_user()
        data = json.loads(response.text)
        confirm.not_acceptable_status(response, 406)
        confirm.existing_user_error(data)
        confirm.api_response_time
