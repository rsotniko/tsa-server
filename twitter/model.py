class Tweet:
	def __init__(self, author, timestamp, text):
		self.author = author
		self.timestamp = timestamp
		self.text = text


class TweetStore:

	def __init__(self, tweets: list = []):
		self.tweets = tweets
		self.request_ids_to_tweets = {}
		self.request_ids_to_predictions = {}


