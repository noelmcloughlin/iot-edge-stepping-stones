#!/usr/bin/env python

from tinydb import TinyDB, Query
db = TinyDB('db.json')

## get a list of temps from the DB
temps = [float(item['temperature']) for item in db]
print(min(temps))
print(max(temps))
print(sum(temps)/len(temps))
