"""
OWASP API Security Top 10 2023 | API7:2023 Server Side Request Forgery
src: https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


@pytest.mark.high
@pytest.mark.api
def test_server_side_request_forgery():
    url = pd.baseUrl + '/ssrf'
    
    # Replace with a URL to test SSRF vulnerability
    data = {"url": "http://malicious-website.com"}
    response = requests.post(url, json=data)
    assert response.status_code != 200, "SSRF vulnerability detected"