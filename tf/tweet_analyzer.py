from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf

graph = tf.get_default_graph();


class TweetAnalyzer:

	def __init__(self, kerasModel):
		self.kerasModel = kerasModel
		with open('../tokenizer.pickle', 'rb') as handle:
			self.tokenizer = pickle.load(handle)

	def analyze_tweets(self, tweets):
		def analyze_tweet(tweet):
			global graph
			with graph.as_default():
				maxlen = 118
				tokens = self.tokenizer.texts_to_sequences([tweet["text"]])
				tokens = pad_sequences(tokens, maxlen=maxlen)
				sentiment = self.kerasModel.predict(np.array(tokens), batch_size=1, verbose=2)[0][0]
				return {"tweet": tweet, "prediction": sentiment}

		return list(map(analyze_tweet, tweets))

