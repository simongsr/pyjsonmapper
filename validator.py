#!/usr/bin/env python3.6
from datetime import datetime, date
from typing import Any

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


class ValidationError(Exception):
    pass


def __is_type(*datatypes):
    def wrapper(value: Any) -> None:
        if not isinstance(value, datatypes):
            raise ValidationError(
                f'Expected type of value was one of '
                f'{[t.__name__ for t in datatypes]}, got '
                f'{type(value).__name__}')
    return wrapper


is_string = __is_type(str)
is_number = __is_type(int, float)
is_boolean = __is_type(bool)
is_datetime = __is_type(datetime, date)
