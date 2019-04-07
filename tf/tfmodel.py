import tensorflow as tf


class KerasModelHolder:

	def __init__(self, model_file_name):
		self.model_file_name = model_file_name
		self.model = None

	def load(self):
		self.model = tf.keras.models.load_model(self.model_file_name)
		return self

