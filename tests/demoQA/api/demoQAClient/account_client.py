from json import dumps
from api.demoQABaseClient.base_client import BaseClient
from demoQAUtils.data import DemoQA, ProjectData as pd
from demoQAUtils.urls import Accounts
from api.demoQABaseAPI.request import APIRequest

UUID = 'c8b459a2-eb0c-4499-bafa-4e38e946c33c'

        
class AccountsClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = DemoQA.baseUrl
        self.login_url = Accounts.LOGIN_ENDPOINT
        self.token_url = Accounts.TOKEN_ENDPOINT
        self.user_url = Accounts.USER_ENDPOINT
        self.authorized = Accounts.AUTHORIZED_USER
        self.selected_user_url = Accounts.SELECTED_USER
        self.request = APIRequest()
        
    def create_user_account(self):
        payload = dumps({"userName": pd.email, "password": pd.newUser})
        return self.request.post(self.user_url, payload, self.headers)
    
    def authenticate_user(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.authorized, payload, self.headers)
    
    def create_user_account_blank_password(self):
        payload = dumps({"userName": pd.email, "password": ''})
        return self.request.post(self.user_url, payload, self.headers)
    
    def create_user_account_weak_password(self):
        payload = dumps({"userName": pd.email, "password": 'pass'})
        return self.request.post(self.user_url, payload, self.headers)
    
    def create_user_account_existing_user(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.user_url, payload, self.headers)
        
    def generate_token(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.token_url, payload, self.headers)
    
    def get_user_account_unauthorized_access(self):
        return self.request.get(self.user_url+f"/{UUID}")
    
    def get_user_account(self):
        return self.request.get(self.user_url)
        
    def delete_user_account(self):
        payload = ''
        return self.request.delete(self.user_url+f"/{UUID}", payload, self.headers)