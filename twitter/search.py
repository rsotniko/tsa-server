from typing import List
from twython import Twython
# import pandas as pd
import json
from twitter.model import Tweet
import os



class TwitterApiClient:
	def __init__(self):
		print(os.getcwd())
		with open("../twitter_credentials.json", "r") as file:
			self.creds = json.load(file)
		self.searchCount = 100
		self.twython = Twython(
			self.creds['CONSUMER_KEY'],
			self.creds['CONSUMER_SECRET'])
		self.tweetLanguage = 'en'

	def search(self, keywords):
		query = {
			'q': keywords,
			'count': self.searchCount,
			'lang': self.tweetLanguage
		}
		found_tweets: List[Tweet] = []
		statuses = self.twython.search(**query)['statuses']
		for status in statuses:
			found_tweets.append(Tweet(
				author=status['user']['screen_name'],
				text=status['text'],
				timestamp=status['created_at']))
		return found_tweets



