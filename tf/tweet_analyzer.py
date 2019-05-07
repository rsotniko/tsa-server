from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
from keras.models import load_model
import tensorflow as tf

keras_model = load_model("../tsa.h5")
graph = tf.get_default_graph()

class TweetAnalyzer:

	def __init__(self):
		with open('../tokenizer.pickle', 'rb') as handle:
			self.tokenizer = pickle.load(handle)

	def analyze_tweets(self, tweets):
		def analyze_tweet(tweet):
			maxlen = 118
			tokens = self.tokenizer.texts_to_sequences([tweet["text"]])
			tokens = pad_sequences(tokens, maxlen=maxlen)
			global graph, keras_model
			with graph.as_default():
				sentiment = keras_model.predict(np.array(tokens), batch_size=1, verbose=2)[0][0]
			return {"tweet": tweet, "prediction": False if round(sentiment) == 0 else True}

		return list(map(analyze_tweet, tweets))

