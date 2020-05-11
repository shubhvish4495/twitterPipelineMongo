import tweepy
import json
from dateutil import parser
import time
import os
import subprocess
import configuration as cfg
import mongoDbOperations as dbOperation

class Streamlistener(tweepy.StreamListener):
	

	def on_connect(self):
		print("You are connected to the Twitter API")


	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""
	def on_data(self,data):
		
		try:
			raw_data = json.loads(data)
			print(raw_data)

			if 'text' in raw_data:
				 
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				dbOperation.insertTweets(username, created_at, tweet, retweet_count, place, location)
				print("Tweet colleted at: {} ".format(str(created_at)))
		except Error as e:
			print(e)



auth = tweepy.OAuthHandler(cfg.CONSUMER_KEY, cfg.CONSUMER_SECRET)
auth.set_access_token(cfg.ACCESS_TOKEN, cfg.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api =tweepy.API(auth, wait_on_rate_limit=True)

# create instance of Streamlistener
listener = Streamlistener(api = api)
stream = tweepy.Stream(auth, listener = listener)

track = ['covid-19']
#track = ['nba', 'cavs', 'celtics', 'basketball']
# choose what we want to filter by
stream.filter(track = track, languages = ['en'])