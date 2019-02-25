import logging
from flask import Flask, request, jsonify
from redis import Redis, RedisError
from managers.scraper import get_text_from_url

redis = Redis(host="redis", port=6379)
app = Flask(__name__)

@app.route("/")
def hello_world():
    app.logger.debug("hello debug")
    return "Wrong route, Mr. Potter! 10 points from Gryfinndor!"

@app.route('/snippet')
def snippets():
    # TODO: make sure both params are there
    url = request.args.get('url')
    max_age = request.args.get('max_age')
    text = get_text_from_url(url)
    # app.logger.info("text: ", text)
    app.logger.info('URL: %s', url)
    # app.logger.debug("ho")
    redis.delete(url)
    redis.set(url, text)
    redis.expire(url, max_age)
    return jsonify({ 'snippet': text })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)