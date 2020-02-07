#!/usr/bin/env python3.6
from datetime import datetime

from pyjsonmapper.field import String, Float, Integer, Object, Array, Boolean
from pyjsonmapper.model import Model
from pyjsonmapper.validator import is_datetime

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)


class MagicNumber(Model):
    number = Integer()

    def __repr__(self):
        return f'''MagicNumber{{
            number = {self.number}
        }}'''


n1 = MagicNumber.load('{ "number": 1 }')
n2 = MagicNumber.load('{ "number": 1 }')
n3 = MagicNumber.load('{ "number": 2 }')

print(n1 == n2)
print(n1 == n1)
print(n1 != n2)
print(n1 == n3)


class Address(Model):
    zip_code = String()

    def __repr__(self):
        return f'''Address{{
            zip_code = {self.zip_code}
        }}'''


class Prova(Model):
    name = String()
    nickname = String(null=True)
    handsome = Boolean()
    age = Integer()
    pi = Float()
    address = Object(Address)
    magic_numbers = Array(MagicNumber)
    number_list = Array()
    timestamp = String(validators=(is_datetime, ),
                              converter=lambda t: datetime.fromtimestamp(t / 1e3))

    def __repr__(self) -> str:
        return f'''Prova{{
            name = {self.name}
            nickname = {self.nickname}
            handsome = {self.handsome}
            age = {self.age}
            pi = {self.pi}
            address = {self.address}
            magic_numbers = {self.magic_numbers}
            number_list = {self.number_list}
            timestamp = {self.timestamp}
        }}'''


prova = Prova.load('''{
    "name": "Simone",
    "handsome": true,
    "age": 33,
    "pi": 3.14,
    "address": {
        "zip_code": "04100"
    },
    "magic_numbers": [
        {
            "number": 1
        },
        {
            "number": 2
        },
        {
            "number": 3
        },
        {
            "number": 5
        },
        {
            "number": 7
        },
        {
            "number": 11
        },
        {
            "number": 13
        },
        {
            "number": 17
        },
        {
            "number": 19
        }
    ],
    "number_list": [1, 2, 3],
    "timestamp": 1
}''')
print(prova)
print(prova.address.zip_code)
print(type(prova.number_list), prova.number_list)

# prova.name = 42

print(Prova.dump(prova, indent=True))
