try:
    #try to import from secrets.py, if it exists
    from mysecrets import USERNAME, PASSWORD, ACCESS_TOKEN, REFRESH_TOKEN, TOKEN_TYPE
    U = USERNAME
    P = PASSWORD
    AT = ACCESS_TOKEN
    RT = REFRESH_TOKEN
    TT = TOKEN_TYPE
except ModuleNotFoundError:
    pass

class Credentials:
    username: str
    password: str
    access_token: str|None = None
    refresh_token: str|None = None
    token_type: str|None = None
    
    def __init__(self) -> None:
        if not 'USERNAME' in globals():
            raise ValueError("USERNAME not found in secrets.py")
        if not 'PASSWORD' in globals():
            raise ValueError("PASSWORD not found in secrets.py")
        self.username = globals()['USERNAME']
        self.password = globals()['PASSWORD']
        
        if 'ACCESS_TOKEN' in globals() and 'REFRESH_TOKEN' in globals() and 'TOKEN_TYPE' in globals():
            self.access_token = globals()['ACCESS_TOKEN'] 
            self.refresh_token = globals()['REFRESH_TOKEN']
            self.token_type = globals()['TOKEN_TYPE']