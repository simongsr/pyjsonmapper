# pyjsonmapper
A simple and hackable mapper from json to python objects... and viceversa!

## Introduction by example

```python
#!/usr/bin/env python3.6
import json
from pprint import pprint

from field import String, Array, Integer
from model import Model


class Address(Model):
    type = String()
    value = String()

    def __repr__(self):
        return f'Address{{ type="{self.type}" value="{self.value}" }}'


class Entry(Model):
    first_name = String()
    last_name = String()
    address = Array(Address)
    age = Integer(defaultvalue=21)

    def __repr__(self):
        return f'Entry{{ first_name="{self.first_name}" last_name="{self.last_name}" address=[{self.address}] age={self.age} }}'


with open('src/pyjsonmapper/address_book.json', 'r') as fp:
    address_book = Entry.load(fp)

with open('src/pyjsonmapper/address_book.json', 'r') as fp:
    raw_address_book = json.load(fp)

address_book1 = Entry.load(raw_address_book)

print(address_book == address_book1)
pprint(Entry.raw(address_book))


```

