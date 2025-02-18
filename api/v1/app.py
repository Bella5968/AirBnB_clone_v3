#!/usr/bin/python3
""" Flask App status route"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from models import storage
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ app that calls the storage close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """error handler"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """Main function"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
