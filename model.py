#!/usr/bin/env python3.6
import inspect
import json
from abc import ABC
from typing import Any

from field import FieldFactory

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


class Model(ABC):

    @classmethod
    def __init(cls):
        try:
            _ = cls.__is_initialized
            return
        except AttributeError:
            pass

        def get_func(fieldname):

            def getter(self):
                return getattr(self, f'__{fieldname}').get_value()

            def setter(self, value):
                getattr(self, f'__{fieldname}').set_value(value)

            return getter, setter

        cls.__field_factories = {
            fieldname: fieldfactory
            for fieldname, fieldfactory in
            inspect.getmembers(cls, lambda m: isinstance(m, FieldFactory))
        }
        for fieldname, fieldfactory in cls.__field_factories.items():
            setattr(cls, fieldname, property(*get_func(fieldname)))
        cls.__is_initialized = True

    def __new__(cls) -> Any:
        instance = super().__new__(cls)
        cls.__init()
        for fieldname, fieldfactory in cls.__field_factories.items():
            setattr(instance, f'__{fieldname}', fieldfactory())
        return instance

    def __init__(self, **kwargs) -> None:
        for fieldname, fieldvalue in kwargs.items():
            getattr(self, f'__{fieldname}').set_value(fieldvalue)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Model):
            return False
        for fieldname in type(self).__field_factories:
            if self.getvalue(fieldname) != o.getvalue(fieldname):
                return False
        return True

    def getvalue(self, fieldname):
        return getattr(self, f'__{fieldname}').get_value()

    @classmethod
    def load(cls, something):

        def load_object(x):
            instance = cls()
            for fieldname, _ in cls.__field_factories.items():
                getattr(instance, f'__{fieldname}').set_value(x.get(fieldname))
            return instance

        if isinstance(something, str):
            something = json.loads(something)
        elif hasattr(something, 'read') and callable(something.read):
            something = json.load(something)

        if isinstance(something, dict):
            return load_object(something)
        elif isinstance(something, list):
            return [load_object(x) for x in something]
        else:
            raise something

    @classmethod
    def dump(cls, something, indent=None) -> str:
        if isinstance(indent, bool):
            indent = (indent) and 4 or None

        def dump_object(x):
            if isinstance(x, Model):
                return {
                    fname: dump_object(getattr(x, f'__{fname}').get_value())
                    for fname in type(x).__field_factories
                }
            elif isinstance(x, list):
                return [dump_object(y) for y in x]
            else:
                return x

        if isinstance(something, Model):
            something = dump_object(something)
        elif isinstance(something, list):
            something = [dump_object(x) for x in something]
        return json.dumps(something, indent=indent)
