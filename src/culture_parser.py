# -*- coding: utf-8 -*-
from flickr_parse_by_geo import parse
from flickr_parser import parser_content
from google_news_parser import parse_news
from weather_parser import parse_weather
import json

# TODO the json with unicode
if __name__ == '__main__':
    content = json.loads('[{"version":"1.4","UID":"521ba66de44d6c43b4cf6aac","title":"國家地理125年經典影像大展","category":"6","showInfo":[{"time":"2013/10/29 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/10/30 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/10/31 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/01 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/02 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/03 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/04 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/05 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/06 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/07 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/08 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/09 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/10 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/11 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/12 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/13 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/14 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/15 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/16 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/17 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/18 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/19 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/20 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/21 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/22 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/23 23:59:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"},{"time":"2013/11/24 18:00:00","location":"臺北市中正區八德路一段1號","locationName":"華山文化創意產業園區","onSales":"Y","price":"","latitude":"25.044023","longitude":"121.529017"}],"showUnit":"國家地理雜誌/美國;","discountInfo":"","descriptionFilterHtml":"今年九月，「國家地理125年經典影像大展」即將來台展出，本展回顧《國家地理》雜誌自1888年創刊之經典攝影作品，展現《國家地理》125年持續不斷的「探索」精神。百年盛事，不容錯過！","imageUrl":"","masterUnit":["時藝多媒體傳播股份有限公司"],"subUnit":[],"supportUnit":[],"otherUnit":[],"webSales":"","sourceWebPromote":"www.mediasphere.com.tw/NGM125","comment":"","editModifyDate":"","sourceWebName":"全國藝文活動資訊系統","startDate":"2013/09/18","endDate":"2013/11/24","status":"success","total":"1"}]')
    info = content[0]['showInfo'][0]
    lat = info['latitude']
    lon = info['longitude']
    #title = content[0]['title']
    #keywords = content[0]['showUnit'].split('/')
    keywords = ['國家地理雜誌']

    f = open('target/google_news.json', 'w')
    f.write(json.dumps(parse_news('國家地理125年經典影像大展')))
    f.close()

    f = open('target/flickr_geo.json', 'w')
    f.write(json.dumps(parse(lat, lon, 1)))
    f.close()

    f = open('target/yahoo_weather.json', 'w')
    f.write(json.dumps(parse_weather(lat, lon)))
    f.close()

    print parser_content('culture.json',keywords)