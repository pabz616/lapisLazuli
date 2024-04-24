import os
from demoQAUtils.data import APIDemoData, DemoQA


class RestFulBookerEndpoints(object):
    RFB_URL = os.getenv("BASE_URL", APIDemoData.restful_booker)
    BOOKINGS = f"{RFB_URL}/booking"
    RANDOM_BOOKING_ID = f"{RFB_URL}/booking/{APIDemoData.booking_id}"
    SINGLE_BOOKING_ID = f"{RFB_URL}/booking/2"
    AUTH_URL = f"{RFB_URL}/auth"
    
    
DQA_URL = os.getenv("BASE_URL", DemoQA.baseUrl)
ACCOUNT_URL = f"{DQA_URL}/Account/v1"
BOOKS_URL = f"{DQA_URL}/BookStore/v1"


class Accounts(object):
    LOGIN_ENDPOINT = f"{ACCOUNT_URL}/login"
    TOKEN_ENDPOINT = f"{ACCOUNT_URL}/GenerateToken"
    USER_ENDPOINT = f"{ACCOUNT_URL}/User"
    AUTHORIZED_USER = f"{ACCOUNT_URL}/Authorized"
    SELECTED_USER = f"{USER_ENDPOINT}/{DemoQA.userId}"


class Bookstore(object):
    BOOKS = f"{BOOKS_URL}/Books"
    SINGLE_BOOK = f"{BOOKS_URL}/Book"
    SELECTED_BOOK = f"{BOOKS_URL}/Book?ISBN=9781449337711"
    
    