import logging
from flask import Blueprint, jsonify, request
from managers.scraper import get_text_from_url
from cache import redis

logger = logging.getLogger(__name__)
snippet = Blueprint('snippet', __name__)

@snippet.route('/snippet')
def snippets():
    url = request.args.get('url')
    max_age = request.args.get('max_age')
    if not url or not max_age:
        logger.error("Missing required parameters.")
        return 'Missing required parameter.', 400

    if redis.exists(url):
        snippet = redis.get(url)
        return jsonify({ 'snippet': snippet })

    text = get_text_from_url(url)
    redis.delete(url)
    redis.set(url, text)
    redis.expire(url, max_age)
    return jsonify({ 'snippet': text })
