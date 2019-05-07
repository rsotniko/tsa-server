import json

from flask import request, jsonify
from flask_api import FlaskAPI
import uuid
import tensorflow as tf
from tf.tfmodel import KerasModelHolder

keras_model = KerasModelHolder('../tsa.h5').load().model
keras_model.summary()
graph = tf.get_default_graph()

def create_app(config_name):
    from twitter.model import TweetStore
    from twitter.search import TwitterApiClient
    from tf.tweet_analyzer import TweetAnalyzer

    app = FlaskAPI(__name__, instance_relative_config=True)
    store = TweetStore()
    twitter_api_client = TwitterApiClient()
    tweet_analyzer = TweetAnalyzer(keras_model)

    @app.route('/keras/summary', methods=['GET'])
    def get_keras_model_summary():
        if request.method == "GET":
            response = jsonify(json.loads(keras_model.to_json()))
            response.status_code = 200
            return response
        return None

    @app.route('/tweets', methods=['GET'])
    def get_data_set():
        if request.method == "GET":
            response = jsonify(store.tweets)
            response.status_code = 200
            return response
        return None

    @app.route('/tweets', methods=['POST'])
    def insert_data_set():
        if request.method == "POST":
            store.tweets = request.get_json()
            response = jsonify({
                'result': 'OK'
            })
            response.status_code = 201
            return response
        return None

    @app.route('/predictions/data', methods=['POST'])
    def insert_data_to_analyze():
        if request.method == "POST":
            tweets = request.get_json()
            request_id = str(uuid.uuid4())
            store.request_ids_to_tweets[request_id] = tweets
            # later should be async
            store.request_ids_to_predictions[request_id] = tweet_analyzer.analyze_tweets(tweets)
            response = jsonify({
                'requestId': request_id
            })
            response.status_code = 201
            return response
        return None

    @app.route('/predictions/<request_id>', methods=['GET'])
    def get_data_analyzed(request_id):
        if request.method == "GET":
            predictions = store.request_ids_to_predictions[request_id]
            response = jsonify(predictions)
            response.status_code = 200
            return response
        return None

    @app.route('/realTweets', methods=['GET'])
    def get_search_results():
        if request.method == "GET":
            keywords = request.args['keywords']
            if 'author' in request.args:
                author = request.args['author']
            if 'from' in request.args:
                from_timestamp = request.args['from']
            if 'to' in request.args:
                to_timestamp = request.args['to']
            tweets = list(map(
                lambda t: t.__dict__,
                twitter_api_client.search(keywords)))
            store.tweets = tweets
            response = jsonify(tweets)
            response.status_code = 200
            return response
        return None

    return app
