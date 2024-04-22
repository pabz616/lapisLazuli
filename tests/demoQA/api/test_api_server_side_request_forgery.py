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
    """Test for open redirection vulnerability"""
    
    url = pd.baseUrl + '/ssrf'
    data = {"url": "&path=http://evil-user.net"}
    response = requests.post(url, json=data)
    assert response.status_code == 404, "SSRF vulnerability detected"