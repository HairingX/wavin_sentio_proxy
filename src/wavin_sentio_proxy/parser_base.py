from datetime import date, datetime, time
from typing import Any, List, TypeVar


class ParserBase:
    """
    Base class for parsers, providing methods to parse various general types of values, including strings, integers, booleans, dates, times, and datetimes.
    """
    #bool
    def _parse_bool(self, value: Any) -> bool:
        if isinstance(value, bool): return value
        return value == True

    def _parse_nullable_bool(self, value: Any) -> bool | None:
        if value is None: return None
        if isinstance(value, bool): return value
        return value == True

    #int
    def _parse_int(self, value: Any) -> int:
        if value is None: return -1
        if isinstance(value, int): return value
        return int(value)

    def _parse_int_list(self, value: Any) -> List[int]:
        if value and isinstance(value, list):
            if isinstance(value[0], int):
                return [int(val) for val in value] # type: ignore
        return list[int]()

    def _parse_nullable_int(self, value: Any) -> int | None:
        if value is None: return None
        if isinstance(value, int): return value
        return int(value)

    #float
    def _parse_float(self, value: Any) -> float:
        if value is None: return -1
        if isinstance(value, float): return value
        return float(value)

    def _parse_float_list(self, value: Any) -> List[float]:
        if value and isinstance(value, list):
            if isinstance(value[0], float):
                return [float(val) for val in value] # type: ignore
        return list[float]()

    def _parse_nullable_float(self, value: Any) -> float | None:
        if value is None: return None
        if isinstance(value, float): return value
        return float(value)


    #str
    def _parse_str(self, value: Any) -> str:
        if value is None: return ""
        return str(value)

    def _parse_nullable_str(self, value: Any) -> str | None:
        if value is None: return None
        return str(value)

    #time
    def _parse_time(self, value: Any, fix_timezone: bool = False) -> time:
        newval = self._parse_nullable_time(value, fix_timezone)
        if newval is None: return time.min
        return newval

    def _parse_nullable_time(self, value: Any, fix_timezone: bool = False) -> time | None:
        if value is None: return None
        if isinstance(value, time): return value
        if isinstance(value, datetime): return value.time()
        value = value.split("T")[-1] # remove date part if present
        result = time.fromisoformat(value)
        if fix_timezone: return self._fix_timezone(result)
        return result

    #date
    def _parse_date(self, value: Any) -> date:
        newval = self._parse_nullable_date(value)
        if newval is None: return date.min
        return newval

    def _parse_nullable_date(self, value: Any) -> date | None:
        if value is None: return None
        if isinstance(value, date): return value
        if isinstance(value, datetime): return value.date()
        value = value.split("T")[0] # remove time part if present
        return date.fromisoformat(value)

    #datetime
    def _parse_datetime(self, value: Any, fix_timezone: bool = False) -> datetime:
        """
        args:
        - value: the value to parse
        - fix_timezone: whether to fix the timezone or not (Aula sometimes send timezone +00:00 for dates which has timezone corrected time)
        """
        newval = self._parse_nullable_datetime(value, fix_timezone)
        if newval is None: return datetime.min
        return newval

    def _parse_nullable_datetime(self, value: Any, fix_timezone: bool = False) -> datetime | None:
        if value is None: return None
        if isinstance(value, datetime): return value
        if isinstance(value, date): return datetime.combine(value, time.min)
        if not "T" in value: # no time part in the value
            parsed_date = self._parse_nullable_date(value)
            if not parsed_date: return None
            return datetime.combine(parsed_date, time.min)
        result = datetime.fromisoformat(value)
        if fix_timezone: return self._fix_timezone(result)
        return result.astimezone(self._get_now().tzinfo)

    TIME_TYPE = TypeVar("TIME_TYPE", datetime, time)
    def _fix_timezone(self, value: TIME_TYPE) -> TIME_TYPE:
        """
        Overridable - Fix timezone of a datetime or time object to the current timezone.
        """
        return value

    def _get_now(self) -> datetime:
        """
        Overridable - Get the current datetime.
        """
        return datetime.now()