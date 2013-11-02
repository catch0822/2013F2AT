# -*- coding: utf-8 -*-
import json, sys
from common import connect

flickr_url = 'http://api.flickr.com/services/rest/'
flickr_key = 'c588daa85452f53eb3babe7a893a359d'
base_params = 'method=flickr.photos.search&format=json&nojsoncallback=1&extras=geo,tags,date_taken,description&has_geo=true&api_key={key}'.format(key=flickr_key)

def parse(lat, lon, r):
    url = generate_url(lat, lon, r, 1)
    return connect(url)

def generate_url(lat, lon, radius, page):
    return "{prefix}?{base_param}&page={page}&lat={lat}&lon={lon}&radius={radius}".format(prefix=flickr_url, base_param=base_params, key=flickr_key, lat=lat, lon=lon, radius=radius, page=page)

"""
This function can parser the search the flickr photo result

Example : 
  python flickr_parser.py FILE_NAME LATITUDE LONGTITUDE RANGE
"""
if __name__ == '__main__':
    target = sys.argv[1]
    latitude = sys.argv[2]
    longtitude = sys.argv[3]
    distance = sys.argv[4]
    f = open(target, 'w')
    result = parse(latitude, longtitude, distance)
    f.write(json.dumps(result))
    f.close()
