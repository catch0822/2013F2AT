# -*- coding: utf-8 -*-
import json, sys
from common import connect

flickr_url = 'http://api.flickr.com/services/rest/'
flickr_key = 'c588daa85452f53eb3babe7a893a359d'
base_params = 'method=flickr.photos.search&format=json&nojsoncallback=1&extras=geo,tags,date_taken,description&has_geo=true&api_key={key}'.format(key=flickr_key)
DEFAULT_MAX_PAGE_NUM = 3

def connect_facebook(keyword):
    photos = []
    is_end_of_page = False
    page = 1
    while is_end_of_page == False:
        url = generate_url(keyword, str(i), field)
        json = connect(url)
        for p in json['photos']['photo']:
            photos.append(p)
        pages = json['photos']['pages']
        if pages > page and page < DEFAULT_MAX_PAGE_NUM:
            page = page + 1
        else:
            is_end_of_page = True
    print 'total size : ' + str(len(photos))
    return photos

def generate_url(keyword, page):
    return "{prefix}?{base_param}&{field}={keyword}&page={page}".format(prefix=flickr_url, base_param=base_params, key=flickr_key, keyword=keyword, page=page, field=field)

"""
TODO this script should support

search check-in/post/photos information from your friends with special places

extension : try to parsing the fan and his content this user followed.

Example : 
  python facebook_parser.py FILE_NAME KEYWORD1 KEYWORD2

Note:

Post analysis : range from 0 to 10000 gap = 1000

SELECT message, description, source_id FROM stream WHERE 
    source_id IN (SELECT uid2 FROM friend WHERE uid1=me()) and (strpos(message,'正')>=0 or strpos(description,'正')>=0) limit 1000 offset 

Photo analysis

SELECT src, caption, owner FROM photo WHERE strpos(caption,"人")>=0 and owner IN (SELECT uid2 FROM friend WHERE uid1=me() limit 10 offset 850)

Find near places

distance(latitude, longitude, "37.75377496892", "-122.42077080676")
SELECT distance(latitude,longitude,"37.75377496892", "-122.42077e,author_uid, latitude, longitude,timestamp,page_id,page_type FROM location_post WHERE author_uid IN (SELECT uid2 FROM friend WHERE uid1=me() LIMIT 10)



PAGE information
SELECT page_id, name, fan_count, description, store_number, talking_about_count, were_here_count, checkins,pic_cover  FROM page WHERE name = "國家地理125年經典影像大展"
select uid, page_id from page_fan where page_id=372858399503276 and uid in (select uid2 from friend where uid1=me() limit 1000)


SELECT name, categories FROM page WHERE page_id IN (SELECT page_id FROM page_fan WHERE uid IN (SELECT uid2 FROM friend WHERE uid1=me() LIMIT 10))
"""
if __name__ == '__main__':
    target = sys.argv[1]
    token = sys.argv[2]
    keywords = sys.argv[3:]
    f = open(file_name, 'w')
    result = []
    for k in keywords:
        result = result + connect_facebook(k)
    f.write(json.dumps(result))
    f.close()
