from dataclasses import dataclass
# import json
from typing import Any
# import pytest

from src.wavin_sentio_proxy import WavinSentioProxy
from credentials import Credentials

@dataclass
class TestData:
    proxy: WavinSentioProxy
    data = dict[str, Any]()
    credentials: Credentials
    
# @pytest.fixture
# def testdata() -> TestData:
#     credentials = Credentials()
#     proxy = WavinSentioProxy(credentials.username, credentials.password)
#     proxy.login()
#     return TestData(proxy=proxy, credentials=credentials)

def test_login():
    proxy = WavinSentioProxy("192.168.5.125")
    proxy.read_values()

# def test_login_refresh(testdata: TestData):
#     proxy = testdata.proxy
#     assert proxy.logindata is not None
#     assert proxy.logindata.access_token is not None
#     assert proxy.logindata.refresh_token is not None
#     assert proxy.logindata.token_type is not None
    
#     proxy.logindata.expires_in = 0
#     assert proxy.logindata.expires_in == 0
    
#     proxy.refresh_login()
    
#     assert proxy.logindata is not None
#     assert proxy.logindata.expires_in != 0
    
#     strlogindata = json.dumps(proxy.logindata.todict(), default=str)
#     print(f"Login success: {strlogindata}")

# def test_get_locations(testdata: TestData):
#     proxy = testdata.proxy
#     testdata.data["locations"] = locations = proxy.get_locations()
#     assert locations is not None
#     assert len(locations) > 0
#     strlocations = json.dumps(locations, default=str)
#     print(f"Locations: {strlocations}")

# def test_get_location(testdata: TestData):
#     proxy = testdata.proxy
#     location_id: str|None = testdata.credentials.location_id
#     if location_id is None:
#         locations = testdata.data.get("locations")
#         if locations is None: 
#             testdata.data["locations"] = locations = proxy.get_locations()
#             strlocations = json.dumps(locations, default=str)
#             print(f"Locations: {strlocations}")
#         assert locations is not None
#         assert len(locations) > 0
#         location_id = locations[0].location_id
    
#     assert location_id is not None
#     testdata.data["location"] = location = proxy.get_location(location_id)
#     assert location is not None
#     assert location.location_id is not None
#     assert location.name is not None
    
#     strlocation = json.dumps(location, default=str)
#     print(f"Location: {strlocation}")

# def test_get_rooms(testdata: TestData):
#     proxy = testdata.proxy
#     location_id: str|None = testdata.credentials.location_id
#     if location_id is None:
#         locations = testdata.data.get("locations")
#         if locations is None: 
#             testdata.data["locations"] = locations = proxy.get_locations()
#             strlocations = json.dumps(locations, default=str)
#             print(f"Locations: {strlocations}")
#         assert locations is not None
#         assert len(locations) > 0
#         location_id = locations[0].location_id
    
#     assert location_id is not None
#     testdata.data["rooms"] = rooms = proxy.get_rooms(location_id)
#     assert rooms is not None
#     assert len(rooms) > 0
#     room = rooms[0]
#     assert room.room_id is not None
#     assert room.name is not None
    
#     strroom = json.dumps(room, default=str)
#     print(f"Room: {strroom}")
    
