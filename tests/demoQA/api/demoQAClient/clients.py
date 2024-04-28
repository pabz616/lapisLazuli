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
        
    def createUserAccount(self):
        payload = dumps({"userName": pd.email, "password": pd.newUser})
        return self.request.post(self.user_url, payload, self.headers)
    
    def authenticateUser(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.authorized, payload, self.headers)
    
    def createUserAccount_BlankPassword(self):
        payload = dumps({"userName": pd.email, "password": ''})
        return self.request.post(self.user_url, payload, self.headers)
    
    def createUserAccount_WeakPassword(self):
        payload = dumps({"userName": pd.email, "password": 'pass'})
        return self.request.post(self.user_url, payload, self.headers)
    
    def createUserAccount_ExistingUser(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.user_url, payload, self.headers)
        
    def generateToken(self):
        payload = dumps(DemoQA.loginData)
        return self.request.post(self.token_url, payload, self.headers)
    
    def getUserAccount_unauthorizedAccess(self):
        return self.request.get(self.user_url+f"/{UUID}")
    
    def getUserAccount(self):
        return self.request.get(self.user_url)
    
    def updateUserAccount(self):
        payload = dumps(x)
        return self.request.put(self.user_url, payload)
    
    def partiallyUserAccount(self):
        payload = dumps(x)
        return self.request.patch(self.user_url, payload)
    
    def deleteUserAccount(self):
        return self.request.delete(self.user_url+f"/{UUID}")