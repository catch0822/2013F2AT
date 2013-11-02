# -*- coding: utf-8 -*-
import json, sys
from common import connect

flickr_url = 'http://api.flickr.com/services/rest/'
flickr_key = 'c588daa85452f53eb3babe7a893a359d'
base_params = 'method=flickr.photos.search&format=json&nojsoncallback=1&extras=geo,tags,date_taken,description&has_geo=true&api_key={key}'.format(key=flickr_key)

def parser_content(filename, keywords):
    process('text_' + filename, keywords, "text")
    process('tag_' + filename, keywords, "tag")

def connect_flickr(keyword, field):
    url = generate_url(keyword, str(1), field)
    return connect(url)

def generate_url(keyword, page, field):
    return "{prefix}?{base_param}&{field}={keyword}&page={page}".format(prefix=flickr_url, base_param=base_params, key=flickr_key, keyword=keyword, page=page, field=field)

def process(file_name, keywords, field):
    for k in keywords:
        f = open(k + '_' + file_name, 'w')
        f.write(json.dumps(connect_flickr(k, field)))
        f.close()
"""
This function can parser the search the flickr photo result

Example : 
  python flickr_parser.py FILE_NAME KEYWORD1 KEYWORD2 ...

TODO :
  1. parsing the real imageop
"""
if __name__ == '__main__':
    target = sys.argv[1]
    keywords = sys.argv[2:]
    process("text_" + target, keywords, "text")
    process("tag_" + target, keywords, "tag")
