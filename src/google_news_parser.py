# -*- coding: utf-8 -*-
import json, sys, urllib, feedparser
import pprint
google_news_url = 'https://news.google.com/news/feeds'

def get_source_url(content):
    return content.split('cluster=')[-1]

def rss2json(rss):
    news = []
    for e in rss['entries']:
        news.append({ 'title':e.title, 'link':e.link, 'description':e.description, \
            'pubDate':e.published, 'id':e.id, 'source':get_source_url(e.id) })
    return news

def parse_news(keyword):
    url = generate_url(keyword)	
    d = feedparser.parse( url )
    return rss2json(d)

# current rss feed is focus on the taiwan !
def generate_url(keyword):
    p = { 'q' : keyword, 'output' : "rss", "ned" : "tw"}    
    return "{prefix}?{params}".format(prefix=google_news_url, params=urllib.urlencode(p))

"""
This function can parse the google news with customized keyword

Example : 
  python google_news_parser.py FILE_NAME KEY_WORD
"""
if __name__ == '__main__':
    target = sys.argv[1]
    keyword = sys.argv[2]
    f = open(target, 'w')
    f.write(json.dumps(parse_news(keyword)))
    f.close()
