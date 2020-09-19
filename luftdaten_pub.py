#!/usr/bin/python

import requests
from sqlalchemy import create_engine
import datetime as dt
import config

url = config.json_output # insert link to sensor's output in *.json format
connection_string = 'mysql://' + config.user +':' + config.password + '@' + config.host + ':' + config.port + '/' + config.db
reading = requests.get(url).json()
pm10 = float(reading['sensordatavalues'][0]['value'])
pm25 = float(reading['sensordatavalues'][1]['value'])

engine = create_engine(connection_string)
query_10 = '''INSERT INTO luftdaten_pm10(value, date) VALUES ('{}', '{}');'''.format(pm10, dt.datetime.now())
query_25 = '''INSERT INTO luftdaten_pm25(value, date) VALUES ('{}', '{}');'''.format(pm25, dt.datetime.now())
engine.execute(query_10)
engine.execute(query_25)
