from assertpy import assert_that
from demoQAUtils.data import ProjectData as pd
import requests


def ok_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.ok), 'Error: {0}'.format(response.status_code)
 
    
def validation_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.bad_request), 'Error: {0}'.format(response.status_code)
    
    
def created_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.created), 'Error: {0}'.format(response.status_code)


def unauthorized_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.unauthorized), 'Error: {0}'.format(response.status_code)
  
    
def not_acceptable_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.not_acceptable), 'Error: {0}'.format(response.status_code)

    
def api_response_time(response):
    assert_that(response.elapsed.total_seconds()).is_less_than(pd.response_limit), "API Response: {0}".format(response.elapsed.total_seconds)
    
    
def created_account(resp_body):
    assert_that(resp_body["userID"]).is_not_none(), "UserID is null"
    assert_that(resp_body["username"]).is_not_none(), "Username is null"
    assert_that(resp_body["books"]).is_empty()
    
    
def created_token(resp_body):
    assert_that(resp_body["token"]).is_not_none(), "Token was not generated"
    assert_that(resp_body["expires"]).is_not_equal_to("2024-04-23"), "Token expired"
    assert_that(resp_body["status"]).is_equal_to("Success"), "Not successful"
    assert_that(resp_body["result"]).is_equal_to("User authorized successfully."), "User not authorized."
    
    
def existing_user_error(resp_body):
    assert_that(resp_body["code"]).is_equal_to("1204")
    assert_that(resp_body["message"]).is_equal_to("User exists!")

 