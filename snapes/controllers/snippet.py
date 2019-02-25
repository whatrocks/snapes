import logging
from flask import Blueprint, jsonify, request, current_app as app
from snapes.managers.scraper import get_text_from_url

logger = logging.getLogger(__name__)
snippet = Blueprint('snippet', __name__)

@snippet.route('/')
def index():
    return "10 points from Gryfinndor!"

@snippet.route('/snippet')
def snippets():
    url = request.args.get('url')
    max_age = request.args.get('max_age')
    if not url or not max_age:
        logger.error("Missing required parameters.")
        return 'Missing required parameter.', 400

    if app.redis.exists(url):
        logger.info('Found %s in cache!', url)
        snippet = app.redis.get(url)
        return jsonify({ 'snippet': snippet })

    logger.info("Fetching snippet from the internet...")
    text = get_text_from_url(url)
    app.redis.delete(url)
    app.redis.set(url, text)
    app.redis.expire(url, max_age)
    return jsonify({ 'snippet': text })
