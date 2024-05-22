"""
OWASP API Security Top 10 2023 | API7:2023 Server Side Request Forgery
src: https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/
"""

import requests
import pytest
from utils.data import DemoQA
from api.demoQAAssertions import assertions as confirm


@pytest.mark.security
@pytest.mark.high
@pytest.mark.api
class TestServerSideRequestForgery:
    def test_open_redirect_vulnerability(self): 
        url = DemoQA.baseUrl + '/ssrf'
        data = {"url": "&path=http://evil-user.net"}
        response = requests.post(url, json=data)
        confirm.not_found_response_status(response, 404), "SSRF vulnerability detected"