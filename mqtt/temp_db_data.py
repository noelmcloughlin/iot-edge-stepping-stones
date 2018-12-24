#!/usr/bin/env python

from tinydb import TinyDB, Query
import time,datetime
db = TinyDB('db.json')

temps=""
for item in db:
    if "t" in item:
        temps+= str(float(item['t']))

def min_temp():
    return min(temps)

def max_temp():
    return max(temps)

def mean_temp():
    return sum(temps)/len(temps)

def temp_items(start,end):
    temps = Query()
    return db.search((temps.timestamp >= start) & (temps.timestamp <= end))
