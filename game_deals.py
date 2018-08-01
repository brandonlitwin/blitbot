# !/usr/bin/env python2
import os
assert os.path.exists('/home/blitwin/tweepyconfig.ini')
import tweepy
import ConfigParser
import praw
# read config data
#parser = SafeConfigParser()
parser = ConfigParser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),"tweepyconfig.ini"))
consumer_key = parser.get('blitbot_twitter','consumer_key')
consumer_secret = parser.get('blitbot_twitter','consumer_secret')
access_token = parser.get('blitbot_twitter','access_token')
access_secret = parser.get('blitbot_twitter','access_secret')
cli_id = parser.get('reddit','cli_id')
cli_s = parser.get('reddit','cli_s')
reddit_pass = parser.get('reddit','reddit_pass')
reddit_user = parser.get('reddit','reddit_user')
u_agent = 'gamedeals script by /u/' + reddit_user
#print(cli_id,cli_s,reddit_pass,reddit_user)
reddit = praw.Reddit(client_id=cli_id,
                     client_secret=cli_s,
                     password=reddit_pass,
                     user_agent=u_agent,
                     username=reddit_user)
subreddit = reddit.subreddit('gamedeals')
for submission in subreddit.hot(limit=1):
    if (submission.score >= 100):
        print(submission.title,submission.url)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
api.update_status("I love deals! Here's today's best game deal.\n " + submission.title + "\n" + submission.url)
