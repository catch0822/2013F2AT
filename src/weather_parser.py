# -*- coding: utf-8 -*-
import json, sys
from common import connect

def parse_weather(lat, lon):
    url = generate_url(lat, lon)
    place = connect(url)
    woeid = place['query']['results']['Result']['woeid']
    return connect(get_weather_url(woeid))

def get_weather_url(woeid):
    return "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D" + woeid+ "&format=json&diagnostics=true"

def generate_url(lat, lon):
    return "http://query.yahooapis.com/v1/public/yql?format=json&q=select%20*%20from%20geo.placefinder%20where%20text%3D%22{latitude}%2C{longtitude}%22%20and%20gflags%3D%22R%22".format(latitude=lat, longtitude=lon)

"""
This function can parser the weather infomation form Yahoo! Weather

Example : 
  python weather_parser.py FILE_NAME LATITUDE LONGTITUDE
"""
if __name__ == '__main__':
    target = sys.argv[1]
    latitude = sys.argv[2]
    longtitude = sys.argv[3]
    f = open(target, 'w')
    result = parse_weather(latitude, longtitude)
    f.write(json.dumps(result))
    f.close()
