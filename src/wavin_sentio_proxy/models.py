from datetime import datetime
from dataclasses import dataclass
from enum import StrEnum

class WavinSentioLocationMode(StrEnum):
    READY = "ready"
    UNKNOWN = "unknown"
    
class WavinSentioRoomMode(StrEnum):
    READY = "ready"
    UNKNOWN = "unknown"
    
class WavinSentioRoomStatus(StrEnum):
    IDLE = "idle"
    HEATING = "heating"
    DRYING = "drying"
    BLOCKED_HEATING = "blocked_heating"
    BLOCKED_DRYING = "blocked_drying"
    UNKNOWN = "unknown"
    
class WavinSentioRoomSensorFunction(StrEnum):
    DISPLAY = "display"
    LIMIT = "limit"
    UNKNOWN = "unknown"

@dataclass
class WavinSentioLocation:
    location_id: str
    name: str
    serial_number: str
    temp_outdoor: float|None = None
    """None if not available"""
    mode: WavinSentioLocationMode = WavinSentioLocationMode.UNKNOWN
    season: str|None = None
    vacation_on: bool = False
    vacation_until: datetime|None = None

@dataclass
class WavinLimit:
    min: float
    max: float

@dataclass
class WavinSentioRoom:
    adaptiveMode: bool
    room_id: str
    name: str
    mode: WavinSentioRoomMode = WavinSentioRoomMode.UNKNOWN
    status: WavinSentioRoomStatus = WavinSentioRoomStatus.UNKNOWN
    temp_span_air: WavinLimit|None = None
    temp_limit_floor: WavinLimit|None = None
    temp_limit_floor_eco: WavinLimit|None = None
    temp_limit_floor_comfort: WavinLimit|None = None
    temp_limit_floor_extra_comfort: WavinLimit|None = None
    
    
    
