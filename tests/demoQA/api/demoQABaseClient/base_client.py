class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        self.auth_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }
        
    def user_status(status):
        if status == 'allowed':
            return {"user": 200}
        elif status == 'denied':
            return {"user": 401}
        else:
            return {"user": 404}