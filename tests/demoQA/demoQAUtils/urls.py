import os
from demoQAUtils.data import APIDemoData, DemoQA


class RestFulBookerEndpoints(object):
    RFB_URL = os.getenv("BASE_URL", APIDemoData.restful_booker)
    BOOKINGS = f"{RFB_URL}/booking"
    RANDOM_BOOKING_ID = f"{RFB_URL}/booking/{APIDemoData.booking_id}"
    SINGLE_BOOKING_ID = f"{RFB_URL}/booking/2"
    AUTH_URL = f"{RFB_URL}/auth"
    
    
class DemoQAEndpoints(object):
    DQA_URL = os.getenv("BASE_URL", DemoQA.baseUrl)
    ACCOUNT_URL = f"{DQA_URL}/Account/v1"
    
    LOGIN_ENDPOINT = f"{ACCOUNT_URL}/login"
    TOKEN_ENDPOINT = f"{ACCOUNT_URL}/GenerateToken"
    USER_ENDPOINT = f"{ACCOUNT_URL}/User"
    