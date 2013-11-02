
# -*- coding: utf-8 -*-
import json, sys, urllib, time
from common import connect
from google_news_parser import parse_news
from weather_parser import parse_weather

def conenct_fql_page(page_id):
    url = generate_page_info_url(page_id)
    return connect(url)

def conenct_fql(keyword):
    url = generate_url(keyword)
    return connect(url)


fql_prefix = 'https://graph.facebook.com/fql'
fb_graphic_prefix = 'https://graph.facebook.com/'
facebook_token = 'access_token=CAACEdEose0cBAC8usDHBamXbcrPKkZBlSCtgea8YL17ZCZBkjdluInUVt5gp51MYyz6EK5rPDcZAr1BimiJRZBljEDrXinBYPAdCiPQBorKLW3jS1wzvPgue2ynE329fpCUG4aaJmZAnNfHREIZCZAsMJQebf9hlw7yOuaSeGgqZBU468BSZCaGByFGOddiZBZCh45QZD'

def generate_page_url(page_id):
    query = 'SELECT email,uid,pic,pic_big,username,pic_small,pic_cover FROM user WHERE uid IN (SELECT uid FROM page_fan WHERE page_id={page_id} AND uid IN (SELECT uid2 FROM friend WHERE uid1=me()))'.format(page_id=page_id)
    return '{fql_prefix}?q={query}&{token}'.format(query=urllib.quote(query), fql_prefix=fql_prefix, token=facebook_token)

def generate_page_info_url(page_id):
    return '{prefix}{page_id}?method=GET&format=json&suppress_http_code=1&&{token}'.format(page_id=page_id, prefix=fb_graphic_prefix, token=facebook_token)

def generate_url(keyword):
    query = 'select page_id,name,fan_count,description,store_number,talking_about_count,were_here_count,checkins,pic_cover FROM page WHERE name="{keyword}"'.format(keyword=keyword.encode("utf-8"))
    return '{fql_prefix}?q={query}&{token}'.format(query=urllib.quote(query), fql_prefix=fql_prefix, token=facebook_token)

def proc_weather(lat, lon, type, id):
    if lat == None or lat == '' or lon == None or lon == '':
        lat = 25.057111
        lon = 121.614302
    weather = parse_weather(lat, lon)
    filename = '../data/weathers/{type}/{id}.json'.format(type=type, id=id)
    fw = open(filename, 'w')
    fw.write(json.dumps(weather))
    fw.close()

def proc_news(keyword, type, id):
    news = parse_news(keyword)
    if len(news) > 0:
        filename = '../data/news/{type}_{id}.json'.format(type=type, id=id)
        fw = open(filename, 'w')
        fw.write(json.dumps(news))
        fw.close()

"""
This function can parser the search the flickr photo result
"""
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    all_arts_num = 0
    keywords_num = 0
    for i in range(99,100):
        f = open('../data/' + str(i), 'r')
        content = f.read()
        json_content = json.loads(content, encoding="utf-8")
        total = len(json_content)
        all_arts_num = all_arts_num + total
        for j in range(8, total):
            title = json_content[j]['title']
            print "@{page} {current}/{total} title : {title}".format(title=title, current=j+1, total=total, page=str(i))
            #info = json_content[j]['showInfo']
            #if len(info) > 0 :
            #    print '{lat} , {lon}'.format(lat=info[0]['latitude'], lon=info[0]['longitude'])
            #    proc_weather(info[0]['latitude'], info[0]['longitude'], i, j)

            #proc_weather(json_content[j]['latitude'], json_content[j]['longitude'], i, j)
            proc_news(title, i, j)
            #conenct_fql(title)
            #time.sleep(0.5)
        
    #print "total arts = " + str(all_arts_num)
    #print "total keywords = " + str(keywords_num)
