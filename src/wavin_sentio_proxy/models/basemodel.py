from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class WavinProxyDatapointKey(Enum):
    """
    Datapoints that can be read.
    """
    MODBUS_MODE = "modbus_mode"


class WavinProxySetpointKey(Enum):
    """
    Setpoints that can be read/written.
    """
    MODBUS_PASSWORD = "modbus_password"

@dataclass(kw_only=True)
class WavinProxyDatapoint:
    read_address: int
    signed: bool
    """indication of the data being signed or unsigned"""
    divider: Optional[int|None] = None
    """Applied to the register value in the order: 1: divider, 2: offset, 3: modifier"""
    offset: Optional[int|None] = None
    """Applied to the register value in the order: 1: divider, 2: offset, 3: modifier"""
    read_modifier: Optional[Callable[[float|int], float|int]|None] = None
    """Modifier applied to value after it has been parsed by the system. can be used to alter hours to days etc. or round floating values
    Applied to the register value in the order: 1: divider, 2: offset, 3: modifier"""
    read_obj: Optional[int|None] = None
    """default is 0"""

@dataclass(kw_only=True)
class WavinProxySetpoint(WavinProxyDatapoint):
    max: int
    """max value in the register"""
    min: int
    """min value in the register"""
    write_address: int
    
    step: Optional[int|None] = None
    """step size in register value, if unset will default to the divider"""
    write_modifier: Optional[Callable[[float|int], float|int]|None] = None
    """Modifier applied to value before it has been parsed back to register type. can be used to alter hours to days etc. or round floating values"""
    write_obj: Optional[int|None] = None
    """default is 0"""

@dataclass
class WavinProxyPointConfig:
    unit_of_measurement: str|None
    read: bool

class WavinProxyUnits:
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    MONTHS = "months"
    YEARS = "years"
    CELSIUS = "celsius"
    BOOL = "bool"
    BITMASK = "bitmask"
    PPM = "ppm"
    """CONCENTRATION PARTS PER MILLION"""
    RPM = "rpm"
    """REVOLUTIONS PER MINUTE"""
    # INT = "int"
    # FLOAT = "float"
    PCT = "percent"
    TEXT = "text"
    UNDEFINED = None
    
DEFAULT_CONFIGS:Dict[WavinProxyDatapointKey|WavinProxySetpointKey, WavinProxyPointConfig] = {
            WavinProxyDatapointKey.MODBUS_MODE: WavinProxyPointConfig(unit_of_measurement=WavinProxyUnits.UNDEFINED, read=True),
            WavinProxySetpointKey.MODBUS_PASSWORD: WavinProxyPointConfig(unit_of_measurement=WavinProxyUnits.UNDEFINED, read=False),
        }

class WavinModelBase:
    
    _attr_manufacturer:str = ""
    _attr_model_name:str = "Basemodel"
    
    datapoints: Dict[WavinProxyDatapointKey, WavinProxyDatapoint] = {}
    setpoints: Dict[WavinProxySetpointKey, WavinProxySetpoint] = {}
    _configs: Dict[WavinProxyDatapointKey|WavinProxySetpointKey, WavinProxyPointConfig] = {}
    _valueMap: Dict[WavinProxyDatapointKey|WavinProxySetpointKey, Dict[float | int, float | int | str]] = {}

    def __init__(self) -> None:
        return

    def get_model_name(self) -> str:
        return self._attr_model_name

    def get_manufacturer(self) -> str:
        return self._attr_manufacturer

    def model_provides_datapoint(self, datapoint: WavinProxyDatapointKey) -> bool:
        return datapoint in self.datapoints

    def get_datapoints_for_read(self) -> List[WavinProxyDatapointKey]:
        return [key for key, value in self._configs.items() if key in self.datapoints and value.read == True]

    def model_provides_setpoint(self, datapoint: WavinProxySetpointKey) -> bool:
        return datapoint in self.setpoints

    def get_setpoints_for_read(self) -> List[WavinProxySetpointKey]:
        return [key for key, value in self._configs.items() if key in self.setpoints and value.read == True]

    def get_unit_of_measure(self, key:WavinProxyDatapointKey|WavinProxySetpointKey) -> str|None:
        if key in self._configs: return self._configs[key].unit_of_measurement
        return WavinProxyUnits.UNDEFINED
  
    def set_default_configs(self) -> None:
        """Sets the point configurations to the standard setup, will not override already assigned records"""
    #     # only keep the points supported by the unit
    #     self._configs = {key: value for key, value in DEFAULT_CONFIGS.items() if key in self._setpoints or key in self._datapoints}

    # def addMissingDefaultConfigs(self):
        # Update self._configs with missing items from DEFAULT_CONFIGS
        self._configs.update({
            key: value for key, value in DEFAULT_CONFIGS.items()
            if key not in self._configs and (key in self.setpoints or key in self.datapoints)
        })
    
    @staticmethod
    def modifier_flip_bool(value:float|int) -> float|int:
        """Flips the true/false state 
        - 1 -> 0
        - 0 -> 1"""
        return 1-value
    
    @staticmethod
    def modifier_seconds_to_minutes(value:float|int) -> float|int:
        return round(value/60)
    
    @staticmethod
    def modifier_hours_to_days(value:float|int) -> float|int:
        return round(value/24)