# -*- coding: utf-8 -*-
import json, sys, urllib, time
from common import connect
from google_news_parser import parse_news
from weather_parser import parse_weather

def conenct_fql(keyword):
    url = generate_url(keyword)
    return connect(url)

def generate_url(keyword):
    prefix = 'https://graph.facebook.com/fql'
    token = 'access_token=CAACEdEose0cBACtQWfoH5ZA3WUM1mflArtc6wbZAyZCoWTtNrkePRZBP4zM0qJZBGMAmwAbYDoG5DUNRsyTbyYO30ZCMSpGpMgijTZATzBoUTciH1Lu6i9VdmZCJb5WsjZAfyBozXPhVPZAlsqZBHKL0FS3YX77zCp1R8ZC4yM9xkciqei3uDCHAI9EFjILzwszGFzQiX9GiJiVX5AZDZD'
    query = 'select page_id,name,fan_count,description,store_number,talking_about_count,were_here_count,checkins,pic_cover FROM page WHERE name="{keyword}"'.format(keyword=keyword.encode("utf-8"))
    return '{prefix}?q={query}&{token}'.format(query=urllib.quote(query), prefix=prefix, token=token)

def proc_weather(lat, lon, type, id):
    if lat == None or lat == '' or lon == None or lon == '':
        return None
    else:
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
    for i in range(7,9):
        f = open('../data/' + str(i), 'r')
        content = f.read()
        json_content = json.loads(content, encoding="utf-8")
        total = len(json_content) - 1
        all_arts_num = all_arts_num + total
        for j in range(270, total):
            title = json_content[j]['title']
            print "@{page} {current}/{total} title : {title}".format(title=title, current=j, total=total, page=str(i))
            info = json_content[j]['showInfo']
            if len(info) > 0 :
                print '{lat} , {lon}'.format(lat=info[0]['latitude'], lon=info[0]['longitude'])
                proc_weather(info[0]['latitude'], info[0]['longitude'], i, j)
            #proc_news(title, i, j)
            #conenct_fql(title)
            time.sleep(0.5)
    #print "total arts = " + str(all_arts_num)
    #print "total keywords = " + str(keywords_num)
