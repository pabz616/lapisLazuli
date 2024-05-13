"""
TEST SQL INJECTION VULNERABILITY AT BOOKS ENDPOINT
"""

import pytest
import requests
from demoQAUtils.urls import Bookstore
from api.demoQAClient.account_client import AccountsClient
from api.demoQAAssertions import assertions as confirm
from demoQAUtils.data import DemoQA
        

client = AccountsClient()

payload = "' OR '1'='1"


@pytest.mark.security
@pytest.mark.api
class TestAPISQLInjection:      
    def test_SQL_Injection_at_GET_endpoint(self):
        malicious_url = Bookstore.SINGLE_BOOK+f"?ISBN={payload}"
        response = requests.get(malicious_url)
        confirm.bad_request_status(response, 400)
        
    def test_SQL_Injection_at_POST_endpoint(self):
        data = {
                "userId": DemoQA.userId,
                "collectionOfIsbns": [{
                    "isbn": f"{payload}",
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
        cookies['token'] = payload
        response = requests.get(Bookstore.BOOKS, cookies=cookies)
        
    @pytest.mark.skip(reason="customize this")
    def test_SQL_Injection_using_Auth_Header(self):
        headers = {
            'Content-Type': payload,
            'Accept': payload,
            'Authorization': payload
        }
        response = requests.get(Bookstore.BOOKS, headers=headers)
        confirm.ok_response_status(response, 200)

    def test_SQL_Injection_with_NULL_BYTE_In_GET(self):
        response = requests.get(Bookstore.SINGLE_BOOK+f"?ISBN=\x00{payload}")
        confirm.bad_request_status(response, 400)
    
    def test_SQL_Injection_with_NULL_BYTE_In_POST(self):
        data = {
            "userId": "DemoQA.userId",
            "collectionOfIsbns": [{
                "isbn": f"%00{payload}",
                }]
        }
        
        response = requests.post(Bookstore.BOOKS, json=data)     
        confirm.unauthorized_status(response, 401)



        
        
