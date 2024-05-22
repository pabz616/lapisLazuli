"""
TEST SQL INJECTION VULNERABILITY AT BOOKS ENDPOINT
"""

import pytest
import requests
from utils.urls import Bookstore
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm
from utils.data import DemoQA, ProjectData as pd
        

client = AccountsClient()


@pytest.mark.security
@pytest.mark.api
class TestAPISQLInjection:      
    def test_SQL_Injection_at_GET_endpoint(self):
        malicious_url = Bookstore.SINGLE_BOOK+f"?ISBN={pd.sqlInjection2}"
        response = requests.get(malicious_url)
        confirm.bad_request_status(response, 400)
        
    def test_SQL_Injection_at_POST_endpoint(self):
        data = {
                "userId": DemoQA.userId,
                "collectionOfIsbns": [{
                    "isbn": f"{pd.sqlInjection2}",
                    }]
                }
        
        response = requests.post(Bookstore.BOOKS, json=data)     
        confirm.unauthorized_status(response, 401)
    
    @pytest.mark.skip(reason="Site doesn't use cookies")    
    def test_SQL_Injection_using_COOKIE(self):
        """Customize this if cookies are used"""
        
        response = client.login_user()
        confirm.ok_response_status(response, 200)
        
        session = requests.Session()
        response = session.get(Bookstore.BOOKS)
        cookies = response.cookies
        cookies['token'] = pd.sqlInjection
        response = requests.get(Bookstore.BOOKS, cookies=cookies)
        
    @pytest.mark.skip(reason="customize this")
    def test_SQL_Injection_using_Auth_Header(self):
        headers = {
            'Content-Type': pd.sqlInjection,
            'Accept': pd.sqlInjection,
            'Authorization': pd.sqlInjection
        }
        response = requests.get(Bookstore.BOOKS, headers=headers)
        confirm.ok_response_status(response, 200)

    def test_SQL_Injection_with_NULL_BYTE_In_GET(self):
        response = requests.get(Bookstore.SINGLE_BOOK+f"?ISBN=\x00{pd.sqlInjection2}")
        confirm.bad_request_status(response, 400)
    
    def test_SQL_Injection_with_NULL_BYTE_In_POST(self):
        data = {
            "userId": "DemoQA.userId",
            "collectionOfIsbns": [{
                "isbn": f"%00{pd.sqlInjection2}",
                }]
        }
        
        response = requests.post(Bookstore.BOOKS, json=data)     
        confirm.unauthorized_status(response, 401)

    def test_SQL_Injection_with_URL_ENCODED_STRING_In_GET(self):
        response = requests.get(Bookstore.SINGLE_BOOK+f"?ISBN={pd.sqlInjection_encoded}")
        confirm.bad_request_status(response, 400)
    
    def test_SQL_Injection_with_URL_ENCODED_STRING_In_POST(self):
        data = {
            "userId": "DemoQA.userId",
            "collectionOfIsbns": [{
                "isbn": f"%00{pd.sqlInjection_encoded}",
                }]
        }
        
        response = requests.post(Bookstore.BOOKS, json=data)     
        confirm.unauthorized_status(response, 401)
     
    def test_SQL_Injection_with_LOWERCASE_PAYLOAD_In_GET(self):
        response = requests.get(Bookstore.SINGLE_BOOK+f"?ISBN={pd.sqlInjection_lowercase}")
        confirm.bad_request_status(response, 400)
        
    def test_SQL_Injection_with_LOWERCASE_PAYLOAD_In_POST(self):
        data = {
            "userId": "DemoQA.userId",
            "collectionOfIsbns": [{
                "isbn": f"%00{pd.sqlInjection_lowercase}"
                }]
        }
        
        response = requests.post(Bookstore.BOOKS, json=data)     
        confirm.unauthorized_status(response, 401)