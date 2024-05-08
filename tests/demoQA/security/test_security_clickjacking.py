"""
    Testing Clickjacking Vulnerability
    Scope: Script opens https://clickjacker.io/ and displays vulnerabilty report
"""

import pytest
import webbrowser


@pytest.mark.security
@pytest.mark.high
class TestClickjackingVulnerability:  
    def test_run_check_for_clickjacking(self):
        """ Portable test to check for clickjacking vulnerabilities. Can be modified to accept a larger number of urls. """
        url = input('Please enter the target URL: ')
        webbrowser.open_new_tab(f"https://clickjacker.io/test?url=https://{url}")