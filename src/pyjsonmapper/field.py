#!/usr/bin/env python3.6
from abc import ABC
from typing import Any

from validator import is_string, is_number, is_boolean

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


class Field(ABC):

    def __init__(self, validators=(), null=False, defaultvalue=None, **kwargs) -> None:
        self.validators = list(validators or [])
        self.null = null or False
        self.defaultvalue = defaultvalue
        self.__value = defaultvalue
        self.is_initialized = False

    def validate(self, value) -> None:
        if self.null and value is None:
            return
        if self.is_initialized:
            for validator in self.validators:
                validator(value)

    def get_value(self) -> Any:
        return self.__value

    def set_value(self, value) -> None:
        value = (not self.null and value is None) and self.defaultvalue or value
        self.is_initialized = True
        self.validate(value)
        self.__value = value


class ScalarField(Field):

    def __init__(self, serializer, defaultvalue, validators=(), null=False, converter=lambda v: v) -> None:
        super().__init__(validators=validators, null=null, defaultvalue=defaultvalue)
        self.converter = converter
        self.serializer = serializer

    def get_value(self):
        return self.serializer(super().get_value())

    def set_value(self, value) -> None:
        super().set_value(self.converter(value))


class StringField(ScalarField):

    def __init__(self, validators=(is_string, ), null=False, defaultvalue='', converter=lambda v: v) -> None:
        super().__init__(str, defaultvalue, validators=validators, null=null, converter=converter)


class FloatField(ScalarField):

    def __init__(self, validators=(is_number, ), null=False, defaultvalue=0.0, converter=lambda v: v) -> None:
        super().__init__(float, defaultvalue, validators=validators, null=null, converter=converter)


class IntegerField(ScalarField):

    def __init__(self, validators=(is_number, ), null=False, defaultvalue=0, converter=lambda v: v) -> None:
        super().__init__(int, defaultvalue, validators=validators, null=null, converter=converter)


class BooleanField(ScalarField):

    def __init__(self, validators=(is_boolean, ), null=False, defaultvalue=False, converter=lambda v: v) -> None:
        super().__init__(bool, defaultvalue, validators=validators, null=null, converter=converter)


class ObjectField(Field):

    def __init__(self, model, validators=(), null=False, **kwargs) -> None:
        super().__init__(validators=validators, null=null, **kwargs)
        self.model = model

    def set_value(self, value) -> None:
        if self.model is not None:
            model_instance = self.model.load(value)
            super().set_value(model_instance)
        else:
            super().set_value(value)


class ArrayField(Field):

    def __init__(self, model=None, validators=(), null=False, **kwargs) -> None:
        super().__init__(validators=validators, null=null, **kwargs)
        self.model = model

    def set_value(self, value) -> None:
        if self.model is not None:
            model_instance_set = self.model.load(value)
            super().set_value(model_instance_set)
        else:
            super().set_value(value)


class FieldFactory(ABC):
    pass


def __scalar_field_factory_builder(field_cls):
    class Factory(FieldFactory):

        def __init__(self, defaultvalue=None, **kwargs) -> None:
            self.defaultvalue = defaultvalue
            self.kwargs = kwargs

        def __call__(self):
            return field_cls(defaultvalue=self.defaultvalue, **self.kwargs)
    return Factory


String = __scalar_field_factory_builder(StringField)
Float = __scalar_field_factory_builder(FloatField)
Integer = __scalar_field_factory_builder(IntegerField)
Boolean = __scalar_field_factory_builder(BooleanField)


class Object(FieldFactory):

    def __init__(self, model=None, **kwargs):
        self.model = model
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return ObjectField(self.model, **self.kwargs)


class Array(FieldFactory):

    def __init__(self, model=None, **kwargs):
        self.model = model
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return ArrayField(self.model, **self.kwargs)
