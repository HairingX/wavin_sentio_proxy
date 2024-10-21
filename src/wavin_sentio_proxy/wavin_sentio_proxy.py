from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict
import logging

from pyModbusTCP.client import ModbusClient # type: ignore

# from .const import ( API, API_VERSION)
# from .model_parser import ModelParser
from .models import *
from .proxy_modeladapter import ProxyModelAdapter
from .responses import *

_LOGGER = logging.getLogger(__name__)

class NilanProxyConnectionErrorType(Enum):
    TIMEOUT = "timeout"
    AUTHENTICATION_ERROR = "authentication_error"
    UNSUPPORTED_MODEL = "unsupported_model"

class LoginData:
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    # scope: str
    token_expires_datetime: datetime
    
    def __init__(self, data: Dict[str, Any]):
        self.access_token = str(data["access_token"])
        self.refresh_token = str(data["refresh_token"])
        self.token_type = str(data["token_type"])
        self.expires_in = int(data["expires_in"])
        # self.scope = str(data["scope"])
        self.token_expires_datetime = datetime.now() + timedelta(seconds=self.expires_in)
        
    def todict(self) -> Dict[str, str|int|datetime]:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "token_type": self.token_type,
            "expires_in": self.expires_in,
            # "scope": self.scope,
            "token_expires_datetime": self.token_expires_datetime,
        }

class WavinSentioProxy():
    
    # _parser = ModelParser()
    _client: ModbusClient
    _model_adapter:ProxyModelAdapter|None = None
    
    def __init__(self, host: str, port: int = 502, unit_id: int = 1, auto_open: bool = True, auto_close: bool = False):
        self._client = ModbusClient(host=host, port=port, unit_id=unit_id, auto_open=auto_open, auto_close=auto_close)
        self._model_adapter = ProxyModelAdapter(0, 0, 0, 0)
        
    def read_values(self):
        id = self._client.read_device_identification()
        registers = self._client.read_input_registers(5,1) # type: ignore
        _LOGGER.debug(f"Device identification: {id}")
        _LOGGER.debug(f"Registers: {registers}")

    # def get_modbus_model(self):
    #     return self._model_adapter.
    
    # def get_location(self, locationid: str) -> WavinSentioLocation:
    #     response = self._request("locations", locationid)
        
    #     _LOGGER.debug(f"Location response (locationid={locationid}): {response}")
    #     responsedata:WavinSentioLocationData=response.json()
    #     _LOGGER.debug(f"Location response (locationid={locationid}) data: {responsedata}")
    #     result = self._parser.parse_location(responsedata)
    #     return result
    
    # def get_locations(self) -> List[WavinSentioLocation]:           
    #     response = self._request("locations")
    #     _LOGGER.debug(f"Locations response: {response}")
    #     responsedata:List[WavinSentioLocationData]=response.json()
    #     _LOGGER.debug(f"Locations response data: {responsedata}")
    #     result = self._parser.parse_locations(responsedata)
    #     return result

    # def get_rooms(self, locationid: str):
    #     params = { 'location': locationid }
    #     response = self._request("rooms", params=params)
    #     _LOGGER.debug(f"Rooms response: {response}")
    #     responsedata=response.json()
    #     _LOGGER.debug(f"Rooms response data: {responsedata}")
    #     result = self._parser.parse_rooms(responsedata)
    #     return result

    # def set_profile(self, locationid:str, profile:str):
    #     payload: Any = {
    #         "returnField": ["code"], 
    #         "room": {"profile": profile}
    #     }
    #     response = self._patch("rooms", locationid, payload)
    #     _LOGGER.debug(f"Set profile response (locationid={locationid}, profile={profile}): {response}")
    #     responsedata=response.json()
    #     _LOGGER.debug(f"Set profile response (locationid={locationid}, profile={profile}) data: {responsedata}")

    # def set_temperature(self, locationid:str, temperature: int):
    #     payload: Any = {
    #         "returnField": ["code"],
    #         "room": {
    #             "profile": "manual", 
    #             "tempManual": temperature}
    #     }
    #     response = self._patch("rooms", locationid, payload)
    #     return response.json()
    
    # def _request(self, method:str, id:str|None = None, params: Dict[str, Any]|None = None) -> requests.Response:
    #     headers: Dict[str,str] = {
    #         "Authorization": self._get_authorization_token(),
    #     }
    #     url = self._build_method_url(method, id)
    #     return requests.get(url, params, headers=headers)
    
    # def _patch(self, method:str, id:str|None = None, payload: Any|None = None) -> requests.Response:
    #     headers: Dict[str,str] = {
    #         "Authorization": self._get_authorization_token(),
    #         "Content-Type": "application/json",
    #     }
    #     url = self._build_method_url(method, id)
    #     return requests.patch(url, json=payload, headers=headers)
        
    # def _build_method_url(self, method:str, locationid:str|None) -> str:
    #     method = method.strip('/ ')
    #     locationid = locationid.strip('/ ') if locationid is not None else ''
    #     return f"{API}{API_VERSION}/{method}/{locationid}"
        
    # def _get_authorization_token(self):
    #     logindata = self.logindata
    #     if logindata is None or datetime.now() >= logindata.token_expires_datetime:
    #         logindata = self.refresh_login()
    #     return f"{logindata.token_type} {logindata.access_token}"
    

class UnauthorizedError(Exception):
    pass
