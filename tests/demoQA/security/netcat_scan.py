import os
import pytest


"""
RECON STEP: NETWORK SCANNER w. NET CAT
"""


@pytest.mark.security
def scan_ip(ip):
    os.system(f"nc -nv -w 1 -z {ip} 80")
    
    
scan_ip(input("Please enter the target IP address: "))