# -*- coding: utf-8 -*-
import json, sys
from common import connect

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

if __name__ == '__main__':
    f = open('101places.csv','r')
    for l in f.readlines():
    	print utf_8_encoder(l)
