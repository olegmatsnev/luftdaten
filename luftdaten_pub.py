#!/usr/bin/python

import requests
from sqlalchemy import create_engine
import datetime as dt

url = '' # insert link to sensors output in *.json format

db_config = {'user': '', # insert database credentials, ip address of the server and port number
'pwd': '',
'host': '',
'port': ,
'db': ''}

connection_string = 'mysql://{}:{}@{}:{}/{}'.format(db_config['user'],
db_config['pwd'],
db_config['host'],
db_config['port'],
db_config['db'])

reading = requests.get(url).json()
pm10 = float(reading['sensordatavalues'][0]['value'])
pm25 = float(reading['sensordatavalues'][1]['value'])

engine = create_engine(connection_string)
query_10 = '''INSERT INTO luftdaten_pm10(value, date) VALUES ('{}', '{}');'''.format(pm10, dt.datetime.now())
query_25 = '''INSERT INTO luftdaten_pm25(value, date) VALUES ('{}', '{}');'''.format(pm25, dt.datetime.now())
engine.execute(query_10)
engine.execute(query_25)
