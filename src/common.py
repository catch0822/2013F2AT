# -*- coding: utf-8 -*-
import urllib, urllib2, json, sys

def connect(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = response.read()
    return json.loads(content)
