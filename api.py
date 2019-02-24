import responder
from redis import Redis, RedisError
from managers.scraper import get_text_from_url

api = responder.API(debug=True)
redis = Redis(host="redis", port=6379)

@api.route("/")
def hello_world(req, resp):
    resp.text = "Wrong route, Mr. Potter! 10 points from Gryfinndor!"

@api.route('/snippet')
def snippets(req, resp):
    # TODO: make sure both params are there
    # url = req.params['url']
    # max_age = req.params['max_age']
    # text = get_text_from_url(url)
    # redis.delete(url)
    # redis.hmset(url, text)
    # redis.expire(url, max_age)
    resp.text = "hi"

if __name__ == "__main__":
    # api.run(debug=True, port=80)
    options = {'debug':True}
    api.serve(**options)