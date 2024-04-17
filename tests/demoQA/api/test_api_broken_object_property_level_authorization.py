"""
OWASP API Security Top 10 2023 | API3:2023 Broken Object Property Level Authorization
src: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/
"""

import requests
import pytest
from demoQAUtils.data import ProjectData as pd


@pytest.mark.high_priority
@pytest.mark.api

# Test for Broken Object Property Level Authorization
@pytest.mark.parametrize("endpoint, roles", ENDPOINTS.items())
def test_broken_object_property_level_auth(endpoint, roles):
    pass