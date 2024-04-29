from assertpy import assert_that
from demoQAUtils.data import ProjectData as pd
import requests


def ok_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.ok), 'Error: {0}'.format(response.status_code)
 
    
def validation_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.bad_request), 'Error: {0}'.format(response.status_code)
    

def not_found_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.codes.not_found), 'Error: {0}'.format(response.status_code)
    
    
def entity_too_large_response_status(response, status_code):
    assert_that(response.status_code).is_equal_to(requests.content_too_large), 'Error: {0}'.format(response.status_code)

# ACCOUNTS


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
 

def created_token_failed(resp_body):
    assert_that(resp_body["status"]).is_equal_to("Failed"), "Not successful"
    assert_that(resp_body["result"]).is_equal_to("User authorization failed.")  

    
def existing_user_error(resp_body):
    assert_that(resp_body["code"]).is_equal_to("1204")
    assert_that(resp_body["message"]).is_equal_to("User exists!")

# BOOKSTORE


def bookstore_catalog_schema(resp_body):
    # KEYS
    assert_that(resp_body).is_not_empty()
    assert_that(resp_body["books"][0]).contains("isbn")
    assert_that(resp_body["books"][0]).contains("title")
    assert_that(resp_body["books"][0]).contains("subTitle")
    assert_that(resp_body["books"][0]).contains("author")
    assert_that(resp_body["books"][0]).contains("publish_date")
    assert_that(resp_body["books"][0]).contains("publisher")
    assert_that(resp_body["books"][0]).contains("pages")
    assert_that(resp_body["books"][0]).contains("description")
    assert_that(resp_body["books"][0]).contains("website")
    
    # VALUES
    assert_that(resp_body["books"][0]["isbn"]).is_not_none(), "ISBN is missing"
    assert_that(resp_body["books"][0]["isbn"]).is_digit(), "ISBN is not all digits"
    assert_that(resp_body["books"][0]["isbn"]).is_length(13), "ISBN is incorrect"
    #
    assert_that(resp_body["books"][0]["title"]).is_not_none(), "Title is missing"
    assert_that(resp_body["books"][0]["subTitle"]).is_not_none(), "SubTitle is missing"
    assert_that(resp_body["books"][0]["author"]).is_not_none(), "Author is missing"
    assert_that(resp_body["books"][0]["publish_date"]).is_not_none(), "Publish Date is missing"
    assert_that(resp_body["books"][0]["publisher"]).is_not_none(), "Publisher is missing"
    assert_that(resp_body["books"][0]["pages"]).is_not_none(), "Page count is missing"
    assert_that(resp_body["books"][0]["pages"]).is_type_of(int), "Page count is improperly formatted"
    assert_that(resp_body["books"][0]["description"]).is_not_none(), "Description is blank or missing"
    assert_that(resp_body["books"][0]["website"]).is_not_none(), "Link to book is blank or missing"


def selected_book_values(resp_body):
    assert_that(resp_body["isbn"]).is_equal_to('9781449337711'), "ISBN is incorrect"
    assert_that(resp_body["title"]).is_equal_to('Designing Evolvable Web APIs with ASP.NET'), "Title is incorrect"
    assert_that(resp_body["subTitle"]).is_equal_to('Harnessing the Power of the Web'), "SubTitle is incorrect"
    assert_that(resp_body["author"]).is_equal_to('Glenn Block et al.'), "Author is incorrect"
    assert_that(resp_body["publish_date"]).is_equal_to('2020-06-04T09:12:43.000Z'), "Publish Date is incorrect"
    assert_that(resp_body["publisher"]).is_equal_to("O'Reilly Media"), "Publisher is incorrect"
    assert_that(resp_body["pages"]).is_equal_to(238), "Page count is incorrect"
    assert_that(resp_body["description"]).is_not_none(), "Description is blank or missing"
    assert_that(resp_body["website"]).is_equal_to('http://chimera.labs.oreilly.com/books/1234000001708/index.html'), "Link is missing"