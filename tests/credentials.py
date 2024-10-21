try:
    #try to import from mysecrets.py, if it exists
    from mysecrets import USERNAME, PASSWORD, ACCESS_TOKEN, REFRESH_TOKEN, TOKEN_TYPE, LOCATION_ID
    U = USERNAME
    P = PASSWORD
    AT = ACCESS_TOKEN
    RT = REFRESH_TOKEN
    TT = TOKEN_TYPE
    LOC_ID = LOCATION_ID
except ModuleNotFoundError:
    pass

class Credentials:
    username: str
    password: str
    access_token: str|None = None
    refresh_token: str|None = None
    token_type: str|None = None
    location_id: str|None = None
    
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
            
        if 'LOCATION_ID' in globals():
            self.location_id = globals()['LOCATION_ID']