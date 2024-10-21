from typing import Any, List, NotRequired, TypedDict

class WavinSentioOutdoorAttributeData(TypedDict):
    temperature: NotRequired[float|None]
    warnings: NotRequired[List[Any]|None]

class WavinSentioLocationAttributeData(TypedDict):
    dst: bool
    """Daylight saving time"""
    mode: str
    season: str
    errExtDeviceFail: NotRequired[int|None]
    hcSwitchState: NotRequired[str|None]
    localTimeOffset: NotRequired[int|None]
    outdoor: NotRequired[WavinSentioOutdoorAttributeData|None]
    timezone: NotRequired[str|None]
    timezoneOffset: NotRequired[int|None]
    vacationOn: NotRequired[bool|None]
    vacationUntil: NotRequired[str|None]

class WavinSentioLocationData(TypedDict):
    attributes: WavinSentioLocationAttributeData
    name: str
    registrationKey: str
    serialNumber: int
    ulc: str
    """Unique location code/Location ID"""
    locationName: NotRequired[str|None]
    sortKey: NotRequired[int|None]
    temporaryPassword: NotRequired[str|None]
    temporaryPasswordExpiration: NotRequired[str|None]
    temporaryPasswordSerialNumber: NotRequired[str|None]
    temporaryPasswordSupport: NotRequired[bool|None]

class WavinSentioLimitData(TypedDict):
    maximum: int
    minimum: int
    
class WavinSentioSchedulerIntervalData(TypedDict):
    profile: str
    start: int
    
class WavinSentioSchedulerData(TypedDict):
    days: List[str]
    intervals: List[WavinSentioSchedulerIntervalData]
    
class WavinSentioRoomData(TypedDict):
    adaptiveMode: bool
    blockMode: List[str]
    co2: NotRequired[float|None]
    co2WarnLevel: NotRequired[float|None]
    code: str
    dryerBlocking: NotRequired[str|None]
    dryerStatus: NotRequired[str|None]
    hasCO2Level: bool
    humidityCurrent: float
    humidityDesired: float
    humidityNotifyEnabled: bool
    humidityNotifyHigh: NotRequired[float|None]
    humiditySpanMax: float
    humiditySpanMin: float
    hysteresisHumidity: float
    hysteresisTempAir: float
    hysteresisTempFloor: float
    isDummy: bool
    """True if the room is a dummy room (no sensor and thermostats installed)"""
    mode: str
    name: str
    override: NotRequired[str|None]
    overrideUntil: NotRequired[str|None]
    profile: str
    scheduler: List[WavinSentioSchedulerData]
    schedulerEachDay: bool
    schedulerStatus: str
    season: str
    sensorFunctionFloor: str
    sensorFunctionHumidity: str
    sortKey: int
    status: str
    """idle, heating"""
    tempAirCurrent: float
    tempAlarmLow: float
    tempComfort: float
    tempCurrent: float
    tempDesired: float
    tempEco: float
    tempExtra: float
    tempFloorCurrent: float
    tempLimit: WavinSentioLimitData
    tempLimitComfort: WavinSentioLimitData
    tempLimitEco: WavinSentioLimitData
    tempLimitExtra: WavinSentioLimitData
    tempManual: float
    tempNotifyHigh: NotRequired[float|None]
    tempNotifyHighEnabled: bool
    tempNotifyLow: NotRequired[float|None]
    tempNotifyLowEnabled: bool
    tempSpan: WavinSentioLimitData
    tempStandBy: float
    tempVacationAway: float
    thermoStatus: str
    """on=thermostat locked, off=thermostat unlocked"""
    vacationEx: bool
    warnCO2AboveLevel: bool
    warnings: List[Any]

locations_data_example = '''[
    {
        "attributes": {
            "dst": true,
            "errExtDeviceFail": 0,
            "hcSwitchState": "notSupported",
            "localTimeOffset": 7200,
            "mode": "ready",
            "outdoor": {
                "temperature": null,
                "warnings": []
            },
            "season": "winter",
            "timezone": "Factory",
            "timezoneOffset": 3600,
            "vacationOn": false,
            "vacationUntil": null
        },
        "locationName": null,
        "name": "Home",
        "registrationKey": "XXXXX-XXXXX-XXXX",
        "serialNumber": XXXXXXXXX,
        "sortKey": 1,
        "temporaryPassword": null,
        "temporaryPasswordExpiration": null,
        "temporaryPasswordSerialNumber": "XXXX-XX-XXXX-XXXX",
        "temporaryPasswordSupport": true,
        "ulc": "XXXXX"
    }
]'''

rooms_data_example = '''[
    {
        "adaptiveMode": false,
        "blockMode": [
            "other"
        ],
        "co2": null,
        "co2WarnLevel": null,
        "code": "XXXXXXXXX",
        "dryerBlocking": "other",
        "dryerStatus": "idle",
        "hasCO2Level": false,
        "humidityCurrent": 61.9,
        "humidityDesired": 62,
        "humidityNotifyEnabled": false,
        "humidityNotifyHigh": null,
        "humiditySpanMax": 80,
        "humiditySpanMin": 50,
        "hysteresisHumidity": 3,
        "hysteresisTempAir": 0.1,
        "hysteresisTempFloor": 0.1,
        "isDummy": false,
        "mode": "ready",
        "name": "Laundry Room",
        "override": "none",
        "overrideUntil": "1970-01-01T00:00:00.000Z",
        "profile": "manual",
        "scheduler": [
            {
                "days": [
                    "mo"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "tu"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "we"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "th"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "fr"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "sa"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            },
            {
                "days": [
                    "su"
                ],
                "intervals": [
                    {
                        "profile": "eco",
                        "start": 0
                    }
                ]
            }
        ],
        "schedulerEachDay": false,
        "schedulerStatus": "disabled",
        "season": "winter",
        "sensorFunctionFloor": "display",
        "sensorFunctionHumidity": "display",
        "sortKey": 1,
        "status": "idle",
        "tempAirCurrent": 22.2,
        "tempAlarmLow": 3,
        "tempComfort": 20,
        "tempCurrent": 22.2,
        "tempDesired": 22,
        "tempEco": 18,
        "tempExtra": 23,
        "tempFloorCurrent": 22.1,
        "tempLimit": {
            "maximum": 27,
            "minimum": 22
        },
        "tempLimitComfort": {
            "maximum": 27,
            "minimum": 22
        },
        "tempLimitEco": {
            "maximum": 27,
            "minimum": 22
        },
        "tempLimitExtra": {
            "maximum": 27,
            "minimum": 22
        },
        "tempManual": 22,
        "tempNotifyHigh": null,
        "tempNotifyHighEnabled": false,
        "tempNotifyLow": null,
        "tempNotifyLowEnabled": false,
        "tempSpan": {
            "maximum": 30,
            "minimum": 10
        },
        "tempStandBy": 6,
        "tempVacationAway": 16,
        "thermoStatus": "off",
        "vacationEx": false,
        "warnCO2AboveLevel": false,
        "warnings": [
        ]
    }
   ]'''
