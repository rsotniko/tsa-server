import json

from flask_api import FlaskAPI
from flask import request, jsonify, abort


def create_app(config_name):
    from app.models import TweetStore
    from app.tfmodel import KerasModelHolder

    app = FlaskAPI(__name__, instance_relative_config=True)
    store = TweetStore()
    keras_model = KerasModelHolder('../tsa1.h5').load().model
    # keras_model.summary()

    @app.route('/keras/summary', methods=['GET'])
    def get_keras_model_summary():
        if request.method == "GET":
            response = jsonify(json.loads(keras_model.to_json()))
            response.status_code = 200
            return response
        return 'Hello, World!'

    @app.route('/tweets', methods=['GET'])
    def get_data_set():
        if request.method == "GET":
            response = jsonify(store.tweets)
            response.status_code = 200
            return response
        return 'Hello, World!'

    @app.route('/tweets', methods=['POST'])
    def insert_data_set():
        if request.method == "POST":
            store.tweets = request.get_json()
            response = jsonify({
                'result': 'OK'
            })
            response.status_code = 201
            return response
        return 'Hello, World!'
    return app
