#! python2
import tweepy
from bs4 import BeautifulSoup
import requests
import urllib
from ConfigParser import SafeConfigParser
# read config data
parser = SafeConfigParser()
parser.read('tweepyconfig.ini')
consumer_key = parser.get('blitbot_twitter','consumer_key')
consumer_secret = parser.get('blitbot_twitter','consumer_secret')
access_token = parser.get('blitbot_twitter','access_token')
access_secret = parser.get('blitbot_twitter','access_secret')
page_link ='https://www.metal-archives.com/band/random'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
name = page_content.find(class_='band_name').get_text()
for a in page_content.find(class_='band_name'):
	ma_band_link = a['href']
query = name + " " + 'band'
# get youtube video
video = ""
with requests.session() as s:
	url = 'http://www.youtube.com/results'
	params = {'search_query': query}
	r = s.get(url, params=params)
	soup = BeautifulSoup(r.content, 'lxml')
	for a in soup.select('.yt-lockup-title > a[title]'):
		if '&list=' not in a['href']:
			video = 'http://www.youtube.com' + a['href'], a['title']
			break
link = video[0]
title = video[1]
# post to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

api.update_status("It's Metal Monday! The metal band of the week is " + name + "\n" + ma_band_link + "\n" + link)