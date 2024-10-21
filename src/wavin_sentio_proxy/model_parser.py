# import logging 
# from typing import Any, List

# from .models import *
# from .parser_base import ParserBase
# from .responses import *

# _LOGGER = logging.getLogger(__name__)

# class ModelParser(ParserBase):
    
    # def _parse_location_mode(self, value: Any) -> WavinSentioLocationMode:
    #     if value is None: return WavinSentioLocationMode.UNKNOWN
    #     match value.lower():
    #         case "ready": return WavinSentioLocationMode.READY
    #         case _: 
    #             _LOGGER.warning(f"Unknown location mode: {value}. Please report this to the developer.")
    #             return WavinSentioLocationMode.UNKNOWN
    
    # def parse_location(self, data: WavinSentioLocationData) -> WavinSentioLocation:
    #     """parse a location from the data."""
    #     location = WavinSentioLocation(
    #         location_id = self._parse_str(data.get("ulc")),
    #         name = self._parse_str(data.get("name")),
    #         serial_number = self._parse_str(data.get("serialNumber")),
    #         mode = self._parse_location_mode(data.get("mode")),
    #         season = self._parse_str(data.get("season")),
    #         vacation_on = self._parse_bool(data.get("vacationOn")),
    #         vacation_until = self._parse_nullable_datetime(data.get("vacationUntil")),
    #         temp_outdoor = self._parse_nullable_float(data.get("outdoor")),
    #     )
    #     return location
    
    # def parse_locations(self, data: List[WavinSentioLocationData]|None) -> List[WavinSentioLocation]:
    #     """Parse a list of locations from the data."""
    #     if data is None: return []
    #     result = list[WavinSentioLocation]()
    #     for locdata in data:
    #         location = self.parse_location(locdata)
    #         result.append(location)
    #     return result
    
    # def parse_room(self, data: WavinSentioRoomData) -> WavinSentioRoom:
    #     room = WavinSentioRoom(
    #         adaptiveMode=self._parse_bool(data.get("adaptiveMode")),
    #         room_id=self._parse_str(data.get("code")),
    #         name=self._parse_str(data.get("name")),
    #     )
    #     return room
    
    # def parse_rooms(self, data: List[WavinSentioRoomData]|None) -> List[WavinSentioRoom]:
    #     if data is None: return []
    #     result = list[WavinSentioRoom]()
    #     for roomdata in data:
    #         room = self.parse_room(roomdata)
    #         result.append(room)
    #     return result