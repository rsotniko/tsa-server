from flask_api import FlaskAPI
from flask import request, jsonify, abort


def create_app(config_name):
    from app.models import TweetStore

    app = FlaskAPI(__name__, instance_relative_config=True)
    store = TweetStore()

    @app.route('/', methods=['GET'])
    def get_data_set():
        if request.method == "GET":
            response = jsonify(store.tweets)
            response.status_code = 200
            return response
        return 'Hello, World!'

    @app.route('/', methods=['POST'])
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
